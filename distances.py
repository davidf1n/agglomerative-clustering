class Distances:
    """creates a dictionary which will be used as a lower triangular matrix for calculating distance between 2 samples.
    instead of calculating multiple times, the matrix will store the information needed."""
    def __init__(self, samples):
        self.distances = {sample.s_id: [] for sample in samples}  # initializing dictionary
        self.s_ids = list(self.distances.keys())
        self.idtosample = {sample.s_id: [] for sample in samples}
        for sample in samples:
            self.idtosample[sample.s_id] = sample
        length = len(samples)
        for i in self.s_ids:
            for j in self.s_ids:
                if j < i :
                    self.distances[i].append(self.idtosample[i].compute_euclidean_distance(self.idtosample[j]))
        self.translate = {}
        for i in range(length):
            self.translate[self.s_ids[i]] = i

    def get_distance(self, first_point, second_point):
        """return euclidean distance for any 2 given samples based on the matrix calculated"""
        if first_point.s_id == second_point.s_id:
            return 0
        elif first_point.s_id < second_point.s_id:
            return self.distances[second_point.s_id][self.translate[first_point.s_id]]
        else:
            return self.distances[first_point.s_id][self.translate[second_point.s_id]]


