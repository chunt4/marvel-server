# test_ws.py

import unittest
import requests
import json

class TestHeroes(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:51031'
	print("testing for server: " + SITE_URL)
	HEROES_URL = SITE_URL + '/heroes/'

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	# test get request
	def test_heroes_get(self):
		hero_id = 3
		r = requests.get(self.HEROES_URL + str(hero_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['name'], 'iron man (anthony \\\"tony\\\" stark)')
		self.assertEqual(resp['align'], 'good characters')

	# test delete request
	def test_heroes_delete(self):
		hero_id = 4
		
		h = {}
		r = requests.delete(self.HEROES_URL + str(hero_id), data = json.dumps(h))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.HEROES_URL + str(hero_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'error')

if __name__ == "__main__":
	unittest.main()

