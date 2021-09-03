import cluster
import link


class AgglomerativeClustering:
    def __init__(self, link, samples, distance_matrix):
        self.link = link  # LINK TYPE
        self.clusters = []
        self.samples = samples
        self.distance_matrix = distance_matrix  # runtime assist
        self.silhoeutte_final_sum_divided_by_size = 0  # final calculation assist
        length = len(samples)
        # initializes the clusters list to be have one sample in each cluster 'bottoms up'
        for i in range(length):
            current_cluster = cluster.Cluster(samples[i].s_id, [samples[i]])
            self.clusters.append(current_cluster)

    def find_cluster_point(self, sample):
        """for a given point the function will return the cluster the point is part of at any given moment"""
        for cluster_ in self.clusters:
            for point in cluster_.samples:
                if point.s_id == sample.s_id:
                    return cluster_
        else:
            return -1

    def in_function(self, point):
        """calculates the average distance from a point to all the points in the same cluster"""
        point_cluster = self.find_cluster_point(point)  # finds the cluster in which the point is part of
        sum_dist = 0
        cluster_size = len(point_cluster.samples)  # size of cluster
        if cluster_size > 1:
            for sample in point_cluster.samples:  # iterate over all the list of samples and calc dist
                sum_dist += self.distance_matrix.get_distance(point, sample)

            return sum_dist / (cluster_size - 1)
        else:
            return 0

    def out_function(self, point):
        """calculates the minimum average distance from a point to a cluster
         (calcs the average for each cluster and then finds the min)"""
        min_dist = 1 << 32
        point_cluster_id = self.find_cluster_point(point).c_id
        for cluster_ in self.clusters:
            if cluster_.c_id != point_cluster_id:  # calc distance to clusters, excluding the cluster the points in
                sum_dist = 0
                for sample in cluster_.samples:  # iterate over all the list of samples in cluster and calc dist
                    sum_dist += self.distance_matrix.get_distance(point, sample)
                cluster_size = len(cluster_.samples)
                distance = sum_dist / cluster_size

                if distance < min_dist:  # maintain min value
                    min_dist = distance
        return min_dist

    def compute_silhoeutte(self):
        """computes the silhoeutte for each sample, returns dict: keys = object sample, value = silhoeutte of key"""
        silhoeutte_dict = {}
        key_list_obj = []  # builds a list of all the sample id's
        for cluster_ in self.clusters:
            for sample in cluster_.samples:
                key_list_obj.append(sample)

        for sample_id in key_list_obj:
            in_ = self.in_function(sample_id)
            if in_ == 0:
                silhoeutte_dict[sample_id.s_id] = 0  # as defined in paper
            else:
                out = self.out_function(sample_id)
                max_in_out = max(in_, out)
                silhoeutte_dict[sample_id.s_id] = (out - in_) / max_in_out
        return silhoeutte_dict

    def compute_summary_silhoeutte(self):
        """computes the silhoeutte for each cluster, returns dict: keys = cluster_id, value = cluster silhoeutte"""
        silhoeutte_all_points = self.compute_silhoeutte()
        #  in order to save run time using the compute_silhoeutte once, modifing the value we will need later
        self.silhoeutte_final_sum_divided_by_size = sum(silhoeutte_all_points.values()) / len(silhoeutte_all_points)
        summary_silhoeutte_dict = {}
        for cluster in self.clusters:
            size_cluster = len(cluster.samples)
            sum_silhoeutte_for_cluster = 0
            for point in cluster.samples:
                sum_silhoeutte_for_cluster += silhoeutte_all_points[point.s_id]
            summary_silhoeutte_dict[cluster.c_id] = round((sum_silhoeutte_for_cluster / size_cluster), 3)
        return summary_silhoeutte_dict

    def compute_rand_index(self):
        """computes rand index as required in assignment (accuracy)"""
        fp = 0  # false positive counter
        fn = 0  # false negative counter
        tp = 0  # true positive counter
        tn = 0  # true negative counter
        n = len(self.samples)  # total amount of samples
        for i in range(n):
            cluster_id_point1 = self.find_cluster_point(self.samples[i]).c_id
            for j in range(i + 1, n):
                cluster_id_point2 = self.find_cluster_point(self.samples[j]).c_id
                label_check = (self.samples[i].label == self.samples[j].label)
                cluster_id_check = (cluster_id_point1 == cluster_id_point2)
                if label_check and cluster_id_check:  # >>> tp
                    tp += 1
                elif (not label_check) and (not cluster_id_check):  # >>> tn
                    tn += 1
                elif (not label_check) and cluster_id_check:  # >>> fp
                    fp += 1
                elif label_check and (not cluster_id_check):  # >>> fn
                    fn += 1
        return (tp + tn) / (tp + tn + fp + fn)

    def run(self, max_clusters):
        if self.link == "single link:":
            dist_method = link.SingleLink(self.distance_matrix)
        else:
            dist_method = link.CompleteLink(self.distance_matrix)

        while len(self.clusters) > max_clusters:
            min_distance = 1 << 31
            min_cluster_one_index = 0
            min_cluster_two_index = 0
            length = len(self.clusters)  # amount of clusters
            for i in range(length):
                for j in range(i + 1, length):
                    distance = dist_method.compute(self.clusters[i], self.clusters[j])
                    if distance < min_distance:  # maintaining min distance between clusters
                        min_cluster_one_index = i
                        min_cluster_two_index = j
                        min_distance = distance
            #  merge the two closest clusters
            self.clusters[min_cluster_one_index].merge(self.clusters[min_cluster_two_index])
            #  deletes the spare merged cluster
            del self.clusters[min_cluster_two_index]

