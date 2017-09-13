
import unittest

def subtract_one(input_integer):
	return input_integer - 1


class FunctionTest(unittest.TestCase): #write a test that subtracts
	
	def setUp(self):
		pass

	def test_subtr_function(self):
		self.assertEqual(subtract_one(3), 2, "Testing if my subtract_one function gives me good output")

	def test_neg_numbers(self):
		self.assertEqual(subtract_one(0), 0, "Testing function with 0")

unittest.main(verbosity=2)