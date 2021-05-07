# Name : ashita boyina
# Roll No : 2019028
# Group : 01

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
		self.assertAlmostEqual(changeBase(782, "SGD", "PLN", "2016-04-18"), 2196.7, delta = 0.1)
		self.assertAlmostEqual(changeBase(314, "INR", "CAD", "2014-05-21"), 5.8, delta = 0.05)
		self.assertAlmostEqual(changeBase(200, "INR", "BRL","2018-02-22"), 10.05, delta = 0.1)
		self.assertAlmostEqual(changeBase(2708, "EEK", "ZAR","2009-12-01"), 1915.3, delta = 0.1)
		self.assertAlmostEqual(changeBase(1992, "EEK", "ZAR","2000-05-09"), 803.8, delta = 0.1)        
		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.




if __name__=='__main__':
	unittest.main()