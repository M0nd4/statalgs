import numpy

a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[1, 2], [3, 4], [5, 6]])
c = numpy.dot(a, b)
d = numpy.dot(b, a)
e = d * 2
f = numpy.diag(c)
g = numpy.diag(c).sum()
