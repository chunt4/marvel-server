# test_api.py

import unittest
import requests
import json
from heroes_library import _hero_database

class TestLibrary(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:51031'
	print("testing for server: " + SITE_URL)
	HEROES_URL = SITE_URL + '/heroes/'

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_load_heroes(self):
		hdb = _hero_database()
		hdb.load_heroes('heroes.dat')
		i = 3
		self.assertEqual(hdb.hero_names[i], 'iron man (anthony \\\"tony\\\" stark)')
		self.assertEqual(hdb.hero_align[i], 'good characters')
		self.assertEqual(hdb.hero_alive[i], 'living characters')
		self.assertEqual(hdb.hero_sex[i], 'male characters')
		self.assertEqual(hdb.hero_iden[i], 'public identity')

	def test_get_heroes(self):
		hdb = _hero_database()
		hdb.load_heroes('heroes.dat')
		herolist = list(hdb.get_heroes())
		#complist = ['spider-man (peter parker)', 'captain america (steven rogers)', 'wolverine (james \\\"logan\\\" howlett)', 'iron man(anthony \\\"tony\\\" stark)']
		i = 0
		for hero in herolist:
			self.assertEqual(hero, i)
			i = i + 1

	def test_get_hero(self):
		hdb = _hero_database()
		hdb.load_heroes('heroes.dat')
		hid = 3
		hero = hdb.get_hero(hid)
		self.assertEqual(hero[0], 'iron man (anthony \\\"tony\\\" stark)')
		self.assertEqual(hero[1], 'good characters')
		self.assertEqual(hero[2], 'living characters')
		self.assertEqual(hero[3], 'male characters')
		self.assertEqual(hero[4], 'public identity')

	def test_search_hero(self):
		hdb = _hero_database()
		hdb.load_heroes('heroes.dat')
		query = "iron man"

	def test_set_hero(self):
		hdb = _hero_database()
		hdb.load_heroes('heroes.dat')
		hero = ['chris hunt', 'bad characters', 'dead characters', 'female characters', 'secret identity']
		i = max(hdb.get_heroes()) + 1
		hdb.set_hero(i, hero)
		self.assertEqual(hdb.get_hero(i)[0], hero[0])
		self.assertEqual(hdb.get_hero(i)[1], hero[1])
		self.assertEqual(hdb.get_hero(i)[2], hero[2])
		self.assertEqual(hdb.get_hero(i)[3], hero[3])
		self.assertEqual(hdb.get_hero(i)[4], hero[4])

	def test_delete_hero(self):
		hdb = _hero_database()
		hdb.load_heroes('heroes.dat')
		hero = ['jack bigej', 'good characters', 'dead characters','female characters', 'public identity']
		i = max(hdb.get_heroes()) + 1
		hdb.set_hero(i, hero)
		hdb.delete_hero(i)
		self.assertEqual(hdb.get_hero(i), None)
		#self.assertEqual(hdb.get_hero(i)[1], None)
		#self.assertEqual(hdb.get_hero(i)[2], None)
		#self.assertEqual(hdb.get_hero(i)[3], None)
		#self.assertEqual(hdb.get_hero(i)[4], None)

if __name__ == "__main__":
	unittest.main()
				
