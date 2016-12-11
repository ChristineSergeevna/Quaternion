from functools import partialmethod

class Quaternion:
	def __init__(self, x = 0, y = 0, z = 0, v = 0):
		self.__components = [x, y, z, v]

	def copy(self):
		return Quaternion(*self.__components)

	def __repr__(self):
		return "Quaternion[{0}]".format(",".join(map(str, self.__components)))

	def __getitem__(self, key):
		return self.__components[key]

	def __iter__(self):
		return self.__components.__iter__()

	def __setitem__(self, key, value):
		self.__components[key] = value

	__componentGetter = lambda key: lambda self: self.__getitem__(key)	 
	__componentSetter = lambda key: lambda self, value: self.__setitem__(key, value)	 

	x = property(__componentGetter(0), __componentSetter(0))
	y = property(__componentGetter(1), __componentSetter(1))
	z = property(__componentGetter(2), __componentSetter(2))
	v = property(__componentGetter(3), __componentSetter(3))

	del __componentGetter
	del __componentSetter

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z and self.v == other.v

	def __add__(self, other):
		return Quaternion(*[a + b for a, b in zip(self, other)])

	def __neg__(self):
		return Quaternion(*[-a for a in self])

	def __sub__(self, other):
		return self + (-other)