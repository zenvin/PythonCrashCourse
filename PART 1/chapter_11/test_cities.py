import unittest
from city_function import formattedCityCountry

class NameTestCase(unittest.TestCase):

	def testCityCountry(self):
		formatted_name = formattedCityCountry('santiago', 'chile')
		self.assertEqual(formatted_name, 'Santiago, Chile')	

	def testCityCountryPopulation(self):
		formatted_name = formattedCityCountry('santiago', 'chile', '800,000')
		self.assertEqual(formatted_name, 'Santiago, Chile, 800,000')	

if __name__ == '__main__':
    unittest.main()