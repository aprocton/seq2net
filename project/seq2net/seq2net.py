# import igraph
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
                    'count': self.data[count],
                    'partners': self.data[soc]}
        else:
            cols = {'subj': self.data[subj],
                    'count': np.ones(self.data[subj].size),
                    'partners': self.data[soc]}

        return cols
