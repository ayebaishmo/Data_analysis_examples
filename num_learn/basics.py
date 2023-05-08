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

