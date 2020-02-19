#In pandas-notebook project do the following exercise in pairs:
import numpy as np

#Create your first array with the elements [1,22.4,5,35,4,6.7,3,8,40] and print it. Experiment what the following functions do: ndim, shape, size and dtype.
my_array= np.array([1,22.4,5,35,4,6.7,3,8,40])
print (my_array)

#Create your first matrix with the elements [['a', 'b'],['c', 'd'],[3, 3]] and print it.
# Experiment what the following functions do: ndim, shape, size and dtype

my_matrix = np.array([['a', 'b'],['c', 'd'],[3, 3]])
#print (my_matrix)
#print(my_matrix.ndim)
#print(my_matrix.shape)
#print(my_matrix.size)
#print(my_matrix.dtype)
print (my_matrix, my_matrix.ndim, my_matrix.shape, my_matrix.size, my_matrix.dtype)

#Create numpy 1 dimension array using each of the functions arange and rand
print('Range_array:', np.arange(1, 9))
print('Random_array:', np.random.rand(3))

#Create numpy 2 dimensions matrix using each of the functions zeros and rand
print('Zero_array:', np.zeros((3,4)))
print('Random_array:', np.random.rand(3,3))

#Create an array containing 20 times the value 7. Reshape it to a 4 x 5 Matrix
new_array= np.array(7)
print(new_array.repeat(20).reshape(4,5))

#Create a 6 x 6 matrix with all numbers up to 36, then print:
#only the first element on it
#only the last 2 rows for it
#only the two mid columns and 2 mid rows for it
#the sum of values for each column
new_matrix = np.arange(36).reshape(6,6)
print (new_matrix)
print('First element:', new_matrix [0][0])
print('Last 2 rows:', new_matrix[-2:])
print('Two mid columns and 2 mid rows:', new_matrix[2:4, 2:4])
column_sums = [sum([row[i] for row in new_matrix]) for i in range(0,len(new_matrix[0]))]
print ('Sum of values for each column:', column_sums)