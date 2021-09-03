class Link:
    def compute(self, cluster, other):  # abstract function - overridden by single link and complete link
        pass


class SingleLink:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix

    def compute(self, cluster, other):
        # returns distance between the two most closest points of 2 clusters
        min_distance = 1 << 31
        range_cluster_one = len(cluster.samples)
        range_cluster_two = len(other.samples)
        for i in range(range_cluster_one):
            cluster_point = cluster.samples[i]
            for j in range(range_cluster_two):
                other_cluster_point = other.samples[j]
                distance = self.distance_matrix.get_distance(cluster_point, other_cluster_point)
                if distance < min_distance:
                    min_distance = distance

        return min_distance


class CompleteLink:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix

    def compute(self, cluster, other):
        # returns distance between the two furthest points of 2 clusters
        max_distance = 0
        range_cluster_one = len(cluster.samples)
        range_cluster_two = len(other.samples)
        for i in range(range_cluster_one):
            cluster_point = cluster.samples[i]
            for j in range(range_cluster_two):
                other_cluster_point = other.samples[j]
                distance = self.distance_matrix.get_distance(cluster_point, other_cluster_point)
                if distance > max_distance:
                    max_distance = distance
        return max_distance
