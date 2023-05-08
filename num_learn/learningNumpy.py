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

"""In NumPy, array attributes are properties of NumPy arrays that provide information about the array's shape, size, data type, and other characteristics. Here are some common array attributes in NumPy:

shape: This attribute returns a tuple that specifies the dimensions of the array. For example, if a is a 2D array with shape (3, 4), a.shape will return (3, 4).

ndim: This attribute returns the number of dimensions of the array. For example, if a is a 2D array, a.ndim will return 2.

size: This attribute returns the total number of elements in the array. For example, if a is a 2D array with shape (3, 4), a.size will return 12.

dtype: This attribute returns the data type of the elements in the array. For example, if a is an array of 32-bit integers, a.dtype will return int32.

itemsize: This attribute returns the number of bytes required to store each element of the array. For example, if a is an array of 32-bit integers, a.itemsize will return 4.

data: This attribute returns a buffer containing the actual elements of the array. For example, if a is an array, a.data will return a buffer object that provides access to the memory buffer containing the array's elements."""

# Here's an example that demonstrates some of these attributes:

"""a = np.array([[1,2,3], [4,5,6]], dtype=np.int32)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.data)
"""
"""In this example, we have created a 2D array a with shape (2, 3) and 
data type int32. We have then printed out several of its attributes using the dot notation."""
"""------------------------------------------------------------------------------"""


# Functions and methods in numpy 
"""NumPy provides a wide range of functions and methods that allow you to perform various operations on arrays and matrices. Here are some of the most commonly used functions and methods in NumPy:

Creation Functions: NumPy provides several functions for creating arrays of various shapes and sizes, including:

np.array(): Creates an array from a list or tuple.

np.zeros(): Creates an array filled with zeros.

np.ones(): Creates an array filled with ones.

np.empty(): Creates an array without initializing its values.

np.arange(): Creates an array with a range of values.

np.linspace(): Creates an array with a specified number of evenly spaced values between two endpoints.

Array Manipulation Functions: NumPy provides several functions for manipulating arrays, including:

np.reshape(): Reshapes an array into a new shape.

np.transpose(): Transposes an array.

np.concatenate(): Concatenates two or more arrays.

np.split(): Splits an array into multiple sub-arrays.

Mathematical Functions: NumPy provides several mathematical functions that operate on arrays, including:

np.sum(): Calculates the sum of an array.

np.mean(): Calculates the mean of an array.

np.std(): Calculates the standard deviation of an array.

np.max(): Finds the maximum value in an array.

np.min(): Finds the minimum value in an array.

np.exp(): Calculates the exponential of an array.

np.log(): Calculates the natural logarithm of an array.

np.dot(): Calculates the dot product of two arrays.

Linear Algebra Functions: NumPy provides several functions for linear algebra operations, including:

np.linalg.inv(): Calculates the inverse of a matrix.

np.linalg.det(): Calculates the determinant of a matrix.

np.linalg.eig(): Calculates the eigenvalues and eigenvectors of a matrix.

np.linalg.solve(): Solves a system of linear equations.

np.linalg.norm(): Calculates the norm of a matrix or vector.

These are just a few examples of the many functions and methods provided by NumPy. 
For a more comprehensive list of functions and methods, you can refer to the NumPy documentation."""