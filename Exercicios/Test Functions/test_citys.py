import unittest 
from city_pais import City_Pais

class Testcity(unittest.TestCase):
    def test_city(self):
        flag = City_Pais("Brasil", "Salvador")
        self.assertEqual(flag, "Brasil, Salvador")
unittest.main()