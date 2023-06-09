# An array is central data structure of an array
# One of the ways to innitialize an array is from python nested list
# numpy.array is function used to create a numpy array
import numpy as np

# HOW TO CREATE A NUMPY ARRAY USING ARRAY ATTRIBUTES
"""# How to create a basic array
a = np.array([1,2,3,4,5])

# or
b = np.array([[1,2,3],[6,7,8],[9,10,11]])

print(a)
print(b)"""

#  You can also create an array with zeros
"""b= np.zeros(10)
print(b)"""

# Or an array filled with ones
"""c = np.ones(4)
print(c)"""

# Or an empty array
"""d = np.empty(2)
print(d)"""

# You can also create an with range of values
"""e = np.arange(9)
print(e)"""

# And even an array that contains a range of evenly spaced intervals. To do this, you will specify the first number, last number, and the step size.
"""f = np.arange(3,15,3)
print(f)"""

# You can also use np.linspace() to create an array with values that are spaced linearly in a specified interval:
"""g = np.linspace(0, 10, num =5)
print(g)"""

# While the Default data type is np.float64 you can specify which data type you want using dtype keyword
"""k = np.ones(5, dtype = np.int64)
print(k)"""

"""--------------------------------------------------------------------------------"""

# ADDING REMOVING AND SORTING ELEMENTS
# This section covers np.sort(), np.concatenate()
# Sorting an element is simple with np.sort(). You can specify the axis, kind, and order when you call the function.
"""arr = np.array([2,8,1,3,8,6,0,4])
sortedarr = np.sort(arr)
print(sortedarr)"""

# Concatenating the array
"""a = np.array([1,2,3,4,5])
b = np.array([7,8,9,10])
c = np.concatenate((a,b))
print(c)"""

# Concatnate with dimension array
"""a = np.array([[1,2,3],[7,8,9]])
b = np.array([[4,5,6]])
c = np.concatenate((a,b), axis = 0)
print(c)"""


# HOW DO YOU KNOW THE SHAPE AND SIZE OF AN ARRAY
"""This section covers ndarray.ndim, ndarray.size, ndarray.shape

ndarray.ndim will tell you the number of axes, or dimensions, of the array.

ndarray.size will tell you the total number of elements of the array. This is the product of the elements of the array’s shape.

ndarray.shape will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3)."""

"""arr = np.array([
                [[0,1,2,3],
                 [4,5,6,7]],

                [[8,9,10,11],
                 [12,13,14,15]],

                [[16,18,19,20],
                 [21,22,23,24]],
            ])
print(arr)"""

# To find the number od dimension
"""x = arr.ndim
print(x)"""

# To find the total number of elements in the array
"""y = arr.size
print(y)"""

# Find the shape pf the array
"""z = arr.shape
print(z)"""

# CAN YOU RESHAPE AN ARRAY
"""This section covers arr.reshape()
Yes!
Using arr.reshape() will give a new shape to an array without changing the data. 
Just remember that when you use the reshape method, the array you want to produce 
needs to have the same number of elements as the original array. If you start with an array 
with 12 elements, you’ll need to make sure that your new array also has a total of 12 elements."""
               
"""a = np.arange(6)
b = a.reshape(3,2)
print(b)"""
"""--------------------------------------------------------------------------------"""

# HOW TO CONVERT 1D ARRAY INTO A 2D ARRAY (HOW TO A NEW AXIS TO AN ARRAY)
"""This section covers np.newaxis, np.expand_dims

You can use np.newaxis and np.expand_dims to increase the dimensions of your existing array.

Using np.newaxis will increase the dimensions of your array by one dimension when used once. 
This means that a 1D array will become a 2D array, a 2D array will become a 3D array, and so on."""

"""a = np.array([1,2,3,4,5,6])
# Lets find out the shape of the array
print(a.shape)"""

# we can use np.newaxis to add a new axis
"""a2 = a[np.newaxis, :]
print(a2.shape)"""

"""You can explicitly convert a 1D array with either a row vector or a column vector using np.newaxis. 
For example, you can convert a 1D array to a row vector by inserting an axis along the first dimension:"""

"""row_vector = a[np.newaxis, :]
print(row_vector.shape)"""


# Or, for a column vector, you can insert an axis along the second dimension:
"""col_vector = a[:, np.newaxis]
print(col_vector.shape)"""

"""You can also expand an array by inserting a new axis at a
 specified position with np.expand_dims.
For example, if you start with this array:"""

"""b = np.expand_dims(a, axis=1)
print(b.shape)"""

# You can add an axis at index position 0 with:
"""c = np.expand_dims(a, axis=0)
c.shape
(1, 6)"""

"""--------------------------------------------------------------------------------"""



# INDEXING AND SLICING
"""data = np.array([1,2,3])

print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])"""

"""You may want to take a section of your array or specific array elements to use in further analysis or additional operations. To do that, you’ll need to subset, slice, and/or index your arrays.

If you want to select values from your array that fulfill certain conditions, it’s straightforward with NumPy.

For example, if you start with this array:"""
"""a = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])"""
#print(a)
# You can easily print out values all that are less than five
"""b = a[ a < 5]
print(b)"""

# You can also select numbers that are equal or greate than five
"""c = a[a >= 5]
print(c)"""

# You cam select elements that are divisible by 2
"""d = a[a%2==0]
print(d)"""

# Or you can select elements that satify two conditions the $ and | operators
"""e = a[(a > 2) & (a <11)]
print(e)"""

"""You can also make use of the logical operators & and | in order to return 
boolean values that specify whether or not the values in an array fulfill a 
certain condition.This can be useful with arrays that contain names or other categorical values."""

"""fiveUp = (a > 5) | (a==5)
print(fiveUp)"""

# You can also use np.nonzero() to select elements or indices from an array
"""f = np.nonzero(a < 5)
print(f)"""


"""In this example, a tuple of arrays was returned: one for each dimension. 
The first array represents the row indices where these values are found, and 
the second array represents the column indices where the values are found.
If you want to generate a list of coordinates where the elements exist, 
you can zip the arrays, iterate over the list of coordinates, and print them. For example:"""
"""list_of_coordinates= list(zip(a[0], a[1]))

for coord in list_of_coordinates:
    print(coord)"""
"""-------------------------------------------------------------------"""


# How to create an array from existing data 
"""This section covers slicing and indexing, np.vstack(), np.hstack(), np.hsplit(), .view(), copy()
You can easily create a new array from a section of an existing array."""
"""a = np.array([1,2,3,4,5,6,7,8,9,10])"""

# You can create a new array by deciding where you want to slice your array from 
"""arr1 = a[3:8]
print(arr1)"""

# You can also stack two existing arrays, both vertically and horizontally
# Let say you have two arrays ar1 ar2
"""ar1 = np.array([[1,1],
                [2,2]])
ar2 = np.array([[3,3],
                [4,4]])"""

# You can stack them vertcally with vstack
"""arrst = np.vstack((ar1, ar2))
print(arrst)"""

# Or horizontally with hstack
"""arrst2 = np.hstack((ar1, ar2))
print(arrst2)"""

"""You can split an array into several smaller arrays using hsplit. You can specify either 
the number of equally shaped arrays to return or the columns after which the division should occur.
Let’s say you have this array:"""
"""x = np.arange(1, 25).reshape(2, 12)
print(x)"""

# If you wanted to split this array into three equally shaped arrays, you would run:
"""y = np.hsplit(x,3)
print(y)
"""
# If you wantesd to split the array after the third and fourth column
"""z = np.hsplit(x, (3, 4))
print(z)"""

"""You can use the view method to create a new array object that looks at the same data as the original array (a shallow copy).

Views are an important NumPy concept! NumPy functions, as well as 
operations like indexing and slicing, will return views whenever possible. 
This saves memory and is faster (no copy of the data has to be made). 
However it’s important to be aware of this - modifying data in a view also modifies the original array!"""

# a = np.array =  ([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
"""Now we create an array b1 by slicing a and modify the first element of b1. This will modify the corresponding element in a as well"""
"""b1 = a[0:1]
print(b1)
b1[0] = 99
print(a)"""

# Using copy method will make a complete copy of the array and it's data 
"""b2 = a.copy()
print(b2)"""
"""-------------------------------------------------------------------------------"""


# BASIC ARRAY OPERATIONS
"""This section covers addition, subtraction, multiplication, division, and more"""
"""a = np.array([1,1])
b = np.array([2,2])
addition = a + b
print(addition)"""

# Another example
"""data = np.array([1,2])
ones = np.ones(2, dtype=int)
add = data + ones
print(add)"""

# You can do more than adding
"""sub = data - ones
print(sub)
mult = data * ones
print(mult)
divide = data / data
print(divide)
"""
# If you wantfind the sum of elements in array we use sum()
"""a = np.array([1,2,3,4])
b = a.sum()
print(b)"""

# To add rows or columns you would have to specify the axis
"""b = np.array([[1,1], [2,2]])
y = b.sum(axis = 0)
print(y)
k = b.sum(axis = 1)
print(k)"""
"""--------------------------------------------------------------"""


# BROADCASTING
"""There are times when you might want to carry out an operation between 
an array and a single number (also called an operation between a vector and a scalar) 
or between arrays of two different sizes. For example, your array (we’ll call it “data”) 
might contain information about distance in miles but you want to convert the information to kilometers."""
"""data = np.array([1.0, 2.0])
broad = data * 1.6
print(broad)
"""
"""NumPy understands that the multiplication should happen with each cell. 
That concept is called broadcasting. Broadcasting is a mechanism that allows 
NumPy to perform operations on arrays of different shapes. The dimensions of 
your array must be compatible, for example, when the dimensions of both arrays 
are equal or when one of them is 1. If the dimensions are not compatible, you will get a ValueError"""

"""-------------------------------------------------------------------------------------------"""


# MORE USEFUL ARRAY OPERATIONS
"""This section covers maximum, minimum, sum, mean, product, standard deviation, and more

NumPy also performs aggregation functions. In addition to min, max, and sum, 
you can easily run mean to get the average, prod to get the result of multiplying 
the elements together, std to get the standard deviation, and more."""

"""a = np.array([
    [0.45053314, 0.17296777, 0.34376245, 0.5510652],
    [0.54627315, 0.05093587, 0.40067661, 0.55645993],
    [0.12697628, 0.82485143, 0.26590556, 0.56917101]
])

p = a.sum()
print(p)

x = a.min()
print(x)"""

"""You can specify the axis you want the aggregation to be computed Forexample you can find the minimum value within
each column by specifying  axis = 0"""

"""y = a.min(axis = 0)
print(y)"""

# CREATING MATRICES
# You can pass Python lists of lists to create a 2-D array (or “matrix”) to represent them in NumPy.
"""data = np.array([[1,2],[3,4],[5,6]])
print(data)"""

# Indexing and slicing are useful when manipulating matrices
"""z = data[0,1]
p = data[1:3]
y = data[0:2,0]
print(z, p , y)"""

# You can aggregate matrices the same way you did with vectors

"""k = data.min()
l = data.max()
d = data.sum()
print(k, l, d)"""

"""You can aggregate all the values in a matrix and you can aggreagate them across columns or rows
using the axis parameter. To illustrate this point, lets look at a slightly modified data set"""

"""data = np.array([[1,2],[5,3],[4,6]])
print(data)

h = data.max(axis= 0)
f = data.max(axis= 1)
print(h, f)"""

"""Once you have created your matrices, you can add and multiply them using arithmetic operators if you have two 
matrices that same size"""

"""data = np.array([[1,2],[3,4]])
ones = np.array([[1,1],[1,1]])

addi = data + ones
print(addi)"""

"""You can also do arithmetic operation on matrices of different sizes, but only if one matrix has only
one column or one row. In this case, Numpy will use it's broadcast rules for the operation"""

"""data = np.array([[1,2],[3,4],[5,6]])
ones_row = np.array([[1,1]])
add = data  + ones_row
print(add)"""

"""Be aware tha numpy prints N dimensional arrays, the last axis is looped over the fatest while the first
axis is the lowest. For instance"""

"""data = np.ones((4,3,2))
print(data)"""

"""There are often instances where we want numpy to initialize the values of an array. Numpy offers fumctions
like ones() and zeros(), and random genrator class for random number generation for that. All you need to do 
os to pass in the number of elements you want to generate"""

"""x = np.ones(3)
print(x)
y = np.zeros(3)
print(y)

rng = np.random.default_rng()
p =rng.random(3)
print(p)
"""
"""You cam use ones(), zeros() and ramdom() to create a 2D array if you give them a tuple describing 
the dimensions of the matrix"""

"""q = np.ones((3,2))
print(q)
k = np.zeros((3,2))
print(k)

rng = np.random.default_rng()
R = rng.random((3,2))
print(R)"""

# GENERATING RANDOM NUMBERS
"""The use of random number generation is an important part of the configuration 
and evaluation of many numerical and machine learning algorithms. Whether you need to randomly 
initialize weights in an artificial neural network, split data into random sets, or randomly shuffle 
your dataset, being able to generate random numbers (actually, repeatable pseudo-random numbers) is essential.

With Generator.integers, you can generate random integers from low (remember that this is inclusive with NumPy) to high (exclusive).
 You can set endpoint=True to make the high number inclusive.

You can generate a 2 x 4 array of random integers between 0 and 4 with:"""

"""rng = np.random.default_rng()
R = rng.integers(5, size=(2,4))
print(R)"""
"""---------------------------------------------------------------------------------------------"""

# HOW TO GET UNIQUE ITEMS AND COUNTS
# This section covers np.unique(). You can find unique elements in an array easily with np.unique

"""a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a)
# you can use np.unique to print unique values from your array
print(unique_values)"""

"""To get the indices of unique values in numpy array (an array of first index position of unique values in
the array), just pass the return index arguement in np.values() as well as your array"""

"""a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values, indeces_list = np.unique(a, return_index=True)
print(indeces_list)"""

"""You can pass the return_counts argument in np.unique() along with your 
array to get the frequency count of unique values in a NumPy array."""
"""a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
occurance_count = np.unique(a, return_counts=True)
print(occurance_count)"""

# This also works with 2D array
"""a_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[1,2,3,4]])
unique_values = np.unique(a_2d)
print(unique_values)"""

"""If the axis argument isn’t passed, your 2D array will be flattened.

If you want to get the unique rows or columns, make sure to pass the axis argument. 
To find the unique rows, specify axis=0 and for columns, specify axis=1."""

"""a_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[1,2,3,4]])
unique_rows = np.unique(a_2d, axis=0)
print(unique_rows)"""

# To get the unique rows, index position, and occurrence count, you can use:
"""a_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[1,2,3,4]])
uniquerows, indeces, occurance_count = np.unique(a_2d, axis=0, return_counts=True, return_index=True)
print(uniquerows)
print(indeces)
print(occurance_count)"""
"""--------------------------------------------------------------------------------------------------"""


# TRANSPOSING AND RESHAPING A MATRIX
"""This section covers arr.reshape(), arr.transpose(), arr.T
It’s common to need to transpose your matrices. NumPy arrays have the property T
 that allows you to transpose a matrix."""

"""You may also need to switch the dimensions of a matrix. This can happen when, 
for example, you have a model that expects a certain input shape that is different from your dataset. 
This is where the reshape method can be useful. You simply need to pass in the new dimensions that you want for the matrix."""

"""arra = np.array([1,2,3,4,5,6])
shap = arra.reshape(3,2)
print(shap)

aga = shap.reshape(2,3)
print(aga)"""