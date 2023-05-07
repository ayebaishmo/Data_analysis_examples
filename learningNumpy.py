"""An ndarray object, short for "n-dimensional array object," is a core data structure in the NumPy library for Python. It represents a multi-dimensional array of homogeneous data types and provides a powerful set of functions and methods for performing numerical operations on this array.

Ndarray objects can have any number of dimensions, from 0 (a scalar) to many, and are typically used for storing and manipulating large amounts of numerical data in scientific computing and data analysis applications. They are efficient and optimized for fast operations, making them a popular choice for numerical computations.

Some of the key features of ndarray objects include their ability to be sliced, indexed, and reshaped, as well as their support for a wide range of mathematical functions, linear algebra operations, and statistical operations. Ndarray objects are also used extensively in machine learning and artificial intelligence applications for tasks such as image and audio processing, natural language processing, and data analysis."""
import numpy as np
"""a = np.array([1,2,3])
print(a)"""

# More than one dimension
"""b = np.array([[1,2],[4,5]])
print(b)"""
"""----------------------------------------------------------------"""



#dtype paramenter
"""In NumPy, the dtype (short for "data type") parameter specifies the data type of the elements in an array. The data type determines how the elements are stored in memory and the operations that can be performed on them.

NumPy provides a wide range of data types, including numeric types (such as int, float, and complex), boolean types (bool), string types (str), and more. Each data type has a corresponding character code that can be used to specify the dtype parameter. For example, the character code 'i' specifies a signed integer, 'f' specifies a floating-point number, and 'c' specifies a complex number.

Here's an example of creating an array with a specific data type:"""
"""
d = np.array([1,2,3], dtype=complex)
print(d)"""

"""# create a 1-dimensional array of integers
a = np.array([1, 2, 3], dtype='i')

# create a 1-dimensional array of complex numbers
b = np.array([1+2j, 3+4j], dtype='c')

# create a 1-dimensional array of strings
c = np.array(['foo', 'bar', 'baz'], dtype='str')"""
"""-----------------------------------------------------------------"""


# DATA TYPE OBJECTS (dtype)
"""In NumPy, data type objects (or dtype objects) are a fundamental part of the library. They are used to specify the data type of elements in arrays, as well as to define the layout of structured arrays.

A dtype object contains information about the type of the data (e.g., integer, floating point, complex), the number of bytes required to store each element of the data type, the byte order (little-endian or big-endian), and other properties such as whether the data type is signed or unsigned.

NumPy provides a wide range of data type objects, including integer types (such as int8, int16, and int64), floating-point types (such as float32 and float64), complex types (such as complex64 and complex128), and others.

Here's an example of creating a dtype object and using it to define the data type of an array:"""
"""dt = np.dtype(np.int32)
print(dt)"""

# int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc
"""dt = np.dtype('i4')
print(dt)"""

# Using edian notation
"""dt = np.dtype('>i4')
print(dt)"""

# Structured data type
"""dt = np.dtype([('age', np.int8)])
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

"""mydtype = np.dtype([('name', 'S10'), ('age', 'i')])

a = np.array([('Alice', 25), ('Bob', 30), ('Charlie', 35)], dtype=mydtype)

print(a['name'])"""
"""In this example, we have defined a custom dtype object with two fields: a string field called 'name' with a maximum length of 10 characters ('S10'), and an integer field called 'age' ('i'). We have then used this custom dtype to create a structured array with three elements, where each element contains a name and an age. The 'name' field can be accessed using the ['name'] syntax, which returns an array of bytes representing the string values."""
"""-----------------------------------------------------------"""""



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