from quaternion import Quaternion
import unittest

class TestRepr(unittest.TestCase):
	
	def test_zero(self):
		q = Quaternion()
		self.assertEqual(str(q), "Quaternion[0,0,0,0]")

	def test_1to4(self):
		q = Quaternion(1, 2, 3, 4)
		self.assertEqual(str(q), "Quaternion[1,2,3,4]")


class TestGettersAndSetters(unittest.TestCase):

	def test_indexsetters(self):
		q = Quaternion()
		for i in range(4):
			q[i] = i + 1
		# Строкое представление должно совпасть
		self.assertEqual(str(q), str(Quaternion(1,2,3,4)))

	def test_indexgetters(self):
		q = Quaternion(1, 2, 3, 4)
		for i in range(4):
			self.assertEqual(q[i], i + 1)

	def test_iterator(self):
		q = Quaternion(1, 2, 3, 4)
		for (i, v) in enumerate(q):
			self.assertEqual(v, i + 1)

	def test_namedgetters(self):
		q = Quaternion(1, 2, 3, 4)
		for c, i in zip(['x', 'y', 'z', 'v'], range(1, 5)):
			self.assertEqual(q.__getattribute__(c), i)

	def test_namedgetters(self):
		q = Quaternion()
		for c, i in zip(['x', 'y', 'z', 'v'], range(1, 5)):
			q.__setattr__(c, i)
		self.assertEqual(str(q), str(Quaternion(1,2,3,4)))

class TestRelational(unittest.TestCase):

	def test_equal(self):
		q1 = Quaternion(1, 2, 3, 4)
		q2 = Quaternion(1, 2, 3, 4)
		self.assertEqual(q1, q2)

	def test_equal_float(self):
		q1 = Quaternion(1.0 / 4.0)
		q2 = Quaternion(0.05 * 5.0 + 1e-32)
		self.assertEqual(q1, q2)

class TestAlgebra(unittest.TestCase):

	def test_sum(self):
		q1 = Quaternion(1, 2, 3, 4)
		q2 = Quaternion(4, 3, 2, 1)
		for v in q1 + q2:
			self.assertEqual(v, 5)

	def test_neg(self):
		q1 = Quaternion(1, 2, 3, 4)
		q2 = q1.copy()
		for a, b in zip(-q1, q2):
			self.assertEqual(a, -b)

	def test_sub(self):
		q1 = Quaternion(2, 4, 8, 16)
		q2 = Quaternion(-2, 1, 3, 10)
		self.assertEqual(q1 - q2, Quaternion(4, 3, 5, 6))

unittest.main()