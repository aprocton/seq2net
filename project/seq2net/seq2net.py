#import igraph
import pandas as pd
import numpy as np


class SequentialData:
    """
    Converts sequential behavior data (e.g. from focal animal sampling) to
    igraph network objects
    """
    def __init__(self, data):
        """
        Return a new SequenceData object with a dataframe containing data
        --------
        Parameters:
            data: pandas DataFrame
                the full sequential observation data to convert to networks
        """

        self.data = data

    def network(self, subj, soc, count=None):
        # TODO: add interval variable
        """
        Return the social network from serial observations of behavior
        --------
        Parameters:
            subj: char
                the name of the column containing the name of the subject
            soc: char
                the name of the column containing social partners for a
                given behavior
            count: char
                the name of the dataframe column containing the count of
                observations of the behavior
        --------
        Returns:
            network: igraph Network object
                the weighted network of interactions estimated using the
                behavior recorded in var
        """

        # subset data and add a count column of ones if count=None
        if count:
            cols = {'subj': self.data[subj],
                    'dur': self.data[count].astype(float),
                    'partners': self.data[soc]}
        else:
            cols = {'subj': self.data[subj],
                    'dur': np.ones(self.data[subj].size),
                    'partners': self.data[soc]}

        df = pd.DataFrame(cols)

        # create dictionary of unique subjects and total observation time
        subj = {}

        for id in pd.Series.unique(df.subj):
            subj[id] = df.loc[df.subj == id, 'dur'].sum()

        # split entries with multiple social partners
        df = pd.DataFrame(partner_split(df.as_matrix(), 1))
        df.columns = ['dur', 'partners', 'subj']

        # create matrix of total observed social behavior
        obs = df.pivot_table(values='dur',
                             index='subj',
                             columns='partners',
                             aggfunc='sum')

        # filter matrix to only include interactions between subjects
        obs = obs.filter(items=subj.keys(), axis=1)

        return(obs)


def partner_split(arr, col):
    # mask/lookup table for rows with multiple partners
    mask = np.vstack([range(arr.shape[0]), np.ones(arr.shape[0], dtype=bool)]).transpose()

    # iterate through and populate mask
    for i in range(arr.shape[0]):
        if (isinstance(arr[i, col], float)):     # account for possible nan
            mask[i, 1] = False
        else:                                    # true if more than one partner
            mask[i, 1] = (len(arr[i, col].split(', ')) > 1)

    newarr = arr.copy()

    # iterate through again and split rows with multiple partners
    for i in range(arr.shape[0]):
        if mask[i, 1]:
            newids = newarr[i, col].split(', ')

            # append new rows for each split ID
            for id in newids:
                row = newarr[i, :]
                row[col] = id
                newarr = np.vstack([newarr, row])

    # delete all rows with multiple partners at once 
    newarr = np.delete(newarr, mask[mask[:, 1],0], axis=0)
    
    return(newarr)
