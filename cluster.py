class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        self.c_id = min(self.c_id, other.c_id)  # set cluster id to minimum of the two
        self.samples = self.samples + other.samples  # merge the lists of the samples
        # sort by the key: sample_id of the object sample
        self.samples = sorted(self.samples, key=lambda obj: obj.s_id)

    def print_details(self, silhouette):
        label_list = [x.label for x in self.samples]  # list of the labels of the points in the cluster
        dominant_label = max(set(label_list), key=label_list.count)
        print_assist = [x.s_id for x in self.samples]
        print(f"Cluster {self.c_id}: {print_assist}, dominant label = {dominant_label}, silhouette = {silhouette}")
