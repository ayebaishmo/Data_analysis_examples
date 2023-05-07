"""An ndarray object, short for "n-dimensional array object," is a core data structure in the NumPy library for Python. It represents a multi-dimensional array of homogeneous data types and provides a powerful set of functions and methods for performing numerical operations on this array.

Ndarray objects can have any number of dimensions, from 0 (a scalar) to many, and are typically used for storing and manipulating large amounts of numerical data in scientific computing and data analysis applications. They are efficient and optimized for fast operations, making them a popular choice for numerical computations.

Some of the key features of ndarray objects include their ability to be sliced, indexed, and reshaped, as well as their support for a wide range of mathematical functions, linear algebra operations, and statistical operations. Ndarray objects are also used extensively in machine learning and artificial intelligence applications for tasks such as image and audio processing, natural language processing, and data analysis."""
import numpy as np
"""a = np.array([1,2,3])
print(a)"""

# More than one dimension
"""b = np.array([[1,2],[4,5]])
print(b)"""

"""In NumPy, the minimum dimension refers to the smallest number of dimensions required to represent an array.

For example, a 1-dimensional array (also known as a vector) has a minimum dimension of 1, a 2-dimensional array (also known as a matrix) has a minimum dimension of 2, and so on.

When creating an array in NumPy, the minimum dimension can be specified using the ndmin parameter. By default, ndmin is set to 0, which means that NumPy will infer the minimum dimension based on the input data. However, ndmin can be set to a higher value to ensure that the resulting array has at least the specified number of dimensions.

Here's an example of creating an array with a minimum dimension of 2:"""
# Minimum dimension

"""c = np.array([1,2,3,4,5], ndmin = 2)
print(c)"""

#dtype paramenter
"""
d = np.array([1,2,3], dtype=complex)
print(d)"""

# DATA TYPE OBJECTS (dtype)
"""dt = np.dtype(np.int32)
print(dt)"""

# int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc
"""dt = np.dtype('i4')
print(dt)"""

# Using edian notation
"""dt = np.dtype('>i4')
print(dt)"""

# Structured data type
"""# dt = np.dtype([('age', np.int8)])
print(dt)"""

# Applying it in ndarray object
"""dt = np.dtype([('age', np.int8)])
q = np.array([(10,),(20,),(30)], dtype=dt)
print(q)"""

# File name can be used to access content of age column
"""dt = np.dtype([('age', np.int8)])
a = np.array([(10,),(20,),(30,)], dtype=dt)
print(a['age'])"""

# Structured datatype
"""student=np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)"""


"""student=np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18,75)], dtype=student)
print(a)"""

# Array attributes
# This array attribute can return a tuple consisting of array dimensions. It can also be used to resize the array

"""a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a.shape
print(b)"""

# Resizing the ndarray
"""a = np.array([[2,3,4],[4,5,6]])
a.shape = (3,2)
print(a)"""

# Numpy also provides reshape function to resize an array
"""a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)"""

# This array attribute returns the number of array dimension
"""a = np.arange(24)
print(a)"""

# The array above is one dimesional array
# Below we are reshaping it

"""a.ndim
b = a.reshape(2,4,3)
print(b)"""