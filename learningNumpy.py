import numpy as np
"""a = np.array([1,2,3])
print(a)"""

# More than one dimension
"""b = np.array([[1,2],[4,5]])
print(b)"""

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
a = np.array([[2,3,4],[4,5,6]])
b = a.shape = (3,2)
print(a)