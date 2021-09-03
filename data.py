import pandas
import sample


class Data:
    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        sample_list = []
        gene_types = list(self.data.keys())[2:]
        for index, s_id in enumerate(self.data['samples']):  # go through each entry
            sample_genes_values = []
            for gene in gene_types:  # collect gene values for each sample
                sample_genes_values.append(self.data[gene][index])
            # add them all and create object
            label = self.data['type'][index]
            new_sample = sample.Sample(s_id, sample_genes_values, label)
            sample_list.append(new_sample)
        return sample_list

