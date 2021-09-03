import distances
import sample

x1 = sample.Sample(1, [1, 2, 3], 'a')
x2 = sample.Sample(2, [7, 10, 3], 'b')
x3 = sample.Sample(3, [1, 6, 6], 'c')
sample_list = [x1, x2, x3]

x = distances.Distances(sample_list)
print(x.distances)
print(f'Distance between 1 and 1: {x.get_distance(x1, x1)}')
print(f'Distance between 1 and 2: {x.get_distance(x1, x2)}')
print(f'Distance between 2 and 1: {x.get_distance(x2, x1)}')

# import math


# def nCr(n, r):
#     f = math.factorial
#     return f(n) / (f(r) * f(n - r))
#
#
# print(nCr(281, 2))
# import distances
# import sample
# x1 = sample.Sample(1, [1, 2, 3], 'a')
# x2 = sample.Sample(2, [7, 10, 3], 'b')
# x3 = sample.Sample(3, [1, 2, 3], 'c')
# samp_list = [x1, x2, x3]
# x = distances.Distances(samp_list)
# print(x.get_distance(x3, x2))


# x = {1: 1, 2: 2, 3: 3}
# print(sum(x.values()))
# print(len(x))

# x = [1, 2, 3]
# y = [4, 5, 6]
# for i in range(len(x)):
#     for j in range(i +1, len(y)):
#         print(i, j)

# import sample
# x = sample.Sample(1, [1, 2, 3], 'a')
# y = sample.Sample(2, [1, 2, 8], 'b')
# print(x.compute_euclidean_distance(y))

# import link
# import cluster
# import sample
# liste = ['a', 'a', 'c']
# print(max(set(liste), key=liste.count))

# import distances
#
# gene1 = [1,2]
# gene2 = [2,3]
# gene3 = [7,10]
# gene4 = [1,2]
# sample1 = sample.Sample(1,gene1,"1")
# sample2 = sample.Sample(2,gene2,"2")
# sample3 = sample.Sample(3,gene3,"3")
# sample4 = sample.Sample(4,gene4,"4")
# list1 = [sample1,sample2]
# list2 = [sample3,sample4]
#
# dist = distances.Distances(list1)
# print(dist.get_distance(sample1,sample2))
#
# # cluster1 = cluster.Cluster(1,list1)
# # cluster2 = cluster.Cluster(2,list2)
# # mylink = link.CompleteLink()
# # print(mylink.compute(cluster1,cluster2))
#
#
#
#
#
#

#
# class Distances:
#     """creates a dictionary which will use us as a matrix for calculating distance between 2 samples.
#     instead of calculating multiple times, the matrix will store the information needed."""
#     def __init__(self, samples):
#         self.distances = {sample.s_id: [] for sample in samples}  # initializing dictionary
#         self.s_ids = list(self.distances.keys())
#         self.idtosample = {sample.s_id: [] for sample in samples}
#         for sample in samples:
#             self.idtosample[sample.s_id] = sample
#         length = len(samples)
#         for i in self.s_ids:
#             for j in self.s_ids:
#                 self.distances[i].append(self.idtosample[i].compute_euclidean_distance(self.idtosample[j]))
#         self.translate = {}
#         for i in range(length):
#             self.translate[self.s_ids[i]] = i
#
#     def get_distance(self, first_point, second_point):
#         """return euclidean distance for any 2 given samples based on the matrix calculated"""
#         return self.distances[first_point.s_id][self.translate[second_point.s_id]]