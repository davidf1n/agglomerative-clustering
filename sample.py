class Sample:
    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label

    def compute_euclidean_distance(self, other):
        current_sum = 0
        length = len(self.genes)
        for i in range(length):  # go through each index of the vector
            current_sum += (self.genes[i] - other.genes[i]) ** 2  # sum the squared difference
        return current_sum ** 0.5  # return sqrt
