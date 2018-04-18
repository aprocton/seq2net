import igraph


class SequenceData:
    """
    Converts sequential behavior data (e.g. from focal animal sampling) to
    igraph network objects
    """
    def __init__(self, data):
        self.data = data

    def network(self):
        """Return the social network"""
        pass
