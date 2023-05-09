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
