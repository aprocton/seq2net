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
                    'count': self.data[count].astype(float),
                    'partners': self.data[soc]}
        else:
            cols = {'subj': self.data[subj],
                    'count': np.ones(self.data[subj].size),
                    'partners': self.data[soc]}

        df = pd.DataFrame(cols)

        # create dictionary of unique subjects and total observation time
        subj = {}

        for id in pd.Series.unique(df.subj):
            subj[id] = df.loc[df.subj == id, 'count'].sum()

        # split entries with multiple social partners

        # create matrix of total observed social behavior
        obs = df.pivot_table(values='count',
                             index='subj',
                             columns='partners',
                             aggfunc='sum')

        # filter matrix to only include interactions between subjects
        obs = obs.filter(items=subj.keys(), axis=1)

        return(obs)
