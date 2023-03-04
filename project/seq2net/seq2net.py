import igraph
import pandas as pd
import numpy as np


def partner_split(arr, col, sstring):
    """
    Duplicate rows of a numpy array if there are multiple social partners
    --------
    Parameters
        arr: numpy ndarray
            array to apply partner_split to
        col: int
            the column containing the social behavior to split on
        sstring: str
            the string separating individual partner IDs
    --------
    Returns:
        newarr: numpy ndarray
            a modified copy of arr:
                rows including multiple social partners deleted
                pairs of duplicate rows appended for each deleted row
    """

    # mask/lookup table for rows with multiple partners
    mask = np.vstack([range(arr.shape[0]),
                      np.ones(arr.shape[0], dtype=bool)]).transpose()

    # iterate through and populate mask
    for i in range(arr.shape[0]):
        if (isinstance(arr[i, col], float)):    # account for possible nan
            mask[i, 1] = False
        else:                                   # true if more than one partner
            mask[i, 1] = (len(arr[i, col].split(sstring)) > 1)

    newarr = arr.copy()

    # iterate through again and split rows with multiple partners
    for i in range(arr.shape[0]):
        if mask[i, 1]:
            newids = newarr[i, col].split(sstring)

            # append new rows for each split ID
            for id in newids:
                row = newarr[i, :].copy()
                row[col] = id
                newarr = np.vstack([newarr, row])

    # delete all rows with multiple partners at once
    newarr = np.delete(newarr, mask[mask[:, 1] == 1, 0], axis=0)

    return(newarr)


def _subjtime(subj, data):
    """
    Create a lookup table of unique subjects and total obs time for each
    --------
    Arguments:
        subj: list
            a list of unique subjects from sequential sampling
        data: np ndarray
            array with names of subjects and durations of single observations
    --------
    Returns:
        subjtime: ndarray
            a two-row ndarray with names of subjects in the first row and total
            observation time for each subject in the second row
    """
    subjtime = np.zeros((2, len(subj)), dtype=object)

    for i in range(len(subj)):
        subjtime[0, i] = str(subj[i])

        mask = data[:, 0] == subj[i]
        subjtime[1, i] = str(data[mask, 1].sum())

    return(subjtime)


def _adj_matrix(data, times):
    """
    Create an adjacency matrix from sequential data with observation times
    --------
    Arguments:
        data: np ndarray
            the dataframe holding information on focal subjects, individual
            partners, and the duration of social behaviors (with columns in the
            order subj, dur, partner)
        times: np ndarray
            a lookup table of unique subjects and total observation times
    --------
    Returns:
        mat: np ndarray
            an adjacency matrix of directed, weighted social affiliation for
            a group of individuals
    """
    # instantiate adjacency matrix
    mat = np.zeros((times.shape[1], times.shape[1]), dtype=float)

    # step through all subject, partner pairs
    for i in range(times.shape[1]):
        for j in range(times.shape[1]):
            if(i == j):
                # no interactions with self are possible
                mat[i, j] = 0
            else:
                # create mask for rows with i as subj
                mask = data[:, 0] == times[0, i]

                # modify mask to include rows with j as partner
                for row in range(len(data)):
                    if mask[row]:
                        if data[row, 2] != times[0, j]:
                            mask[row] = False

                # social time for partners i and j
                ptime = data[mask, 1].sum()

                # normalized by total obs time for i and j
                norm_ptime = ptime/(float(times[1, i]) + float(times[1, j]))
                mat[i, j] = norm_ptime

    return(mat)

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
                the full sequential observation data to create networks from
        """

        self.data = data

    def get_adj_matrix(self, subj, soc, count=None):
        """
        Return the adjacency matrix from serial observations of behavior
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
            obs: np ndarray
                an adjacency matrix of directed, weighted social affiliation for
                a group of individuals
        """

        # keep relevant columns and add a count column of ones if count=None
        if count:
            cols = {'subj': self.data[subj],
                    'dur': self.data[count].astype(float),
                    'partners': self.data[soc]}
        else:
            cols = {'subj': self.data[subj],
                    'dur': np.ones(self.data[subj].size),
                    'partners': self.data[soc]}

        df = pd.DataFrame(cols)

        # create lookup table of unique subjects and total observation time
        unique = df.subj.unique().tolist()
        subjdur = pd.DataFrame({'subj': df.subj, 'dur': df.dur}).to_numpy()

        times = _subjtime(unique, subjdur)

        # split entries with multiple social partners
        df = pd.DataFrame(partner_split(df.to_numpy(), 2, ', '))
        df.columns = ['subj', 'dur', 'partners']
        
        # create matrix of total observed social behavior
        obs = _adj_matrix(df.to_numpy(), times)

        return(obs)

    def get_network(self, subj, soc, count=None):
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
        matrix = self.get_adj_matrix(subj, soc, count)

        # create igraph Graph
        g = igraph.Graph.Adjacency((matrix > 0).tolist())

        # add node labels
        subj = self.data.subj.unique().tolist()
        g.vs['label'] = subj

        # add edge weights
        g.es['weight'] = matrix[matrix.nonzero()]

        return(g)
