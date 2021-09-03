import distances
import sample

# Random samples to check the code
x1 = sample.Sample(1, [1, 2, 3], 'a')
x2 = sample.Sample(2, [7, 10, 3], 'b')
x3 = sample.Sample(3, [1, 6, 6], 'c')
sample_list = [x1, x2, x3]

x = distances.Distances(sample_list)
print(x.distances)
print(f'Distance between 1 and 1: {x.get_distance(x1, x1)}')
print(f'Distance between 1 and 2: {x.get_distance(x1, x2)}')
print(f'Distance between 2 and 1: {x.get_distance(x2, x1)}')
