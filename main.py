import sys
import data
import agglomerative_clustering
import distances


def main(argv):
    dataset = data.Data(argv[1])
    samples = dataset.create_samples()
    links = ["single link:", "complete link:"]
    distance_matrix = distances.Distances(samples)
    for link in links:
        print(link)
        agg_object = agglomerative_clustering.AgglomerativeClustering(link, samples, distance_matrix)
        agg_object.run(7)  # min 7 clusters as required in assignment

        sil_dict = agg_object.compute_summary_silhoeutte()
        for cluster in agg_object.clusters:
            cluster.print_details(sil_dict[cluster.c_id])  # printing each clusters details
        silhouette = round(agg_object.silhoeutte_final_sum_divided_by_size, 3)
        ri = round(agg_object.compute_rand_index(), 3)
        print(f"Whole data: silhouette = {silhouette} , RI = {ri}")
        print()


if __name__ == '__main__':
    main(sys.argv)
