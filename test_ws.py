# test_ws.py
# NOTE: Must restart server before running test script

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

	# test get request with hero_id
	def test_heroes_get(self):
		hero_id = 3
		r = requests.get(self.HEROES_URL + str(hero_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['name'], 'iron man (anthony \\\"tony\\\" stark)')
		self.assertEqual(resp['align'], 'good characters')
		self.assertEqual(resp['alive'], 'living characters')
		self.assertEqual(resp['sex'], 'male characters')
		self.assertEqual(resp['iden'], 'public identity')

	# test put request with hero_id
	def test_heroes_put(self):
		hero_id = 25

		r = requests.get(self.HEROES_URL + str(hero_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['name'], 'nicholas fury (earth-616)')
		self.assertEqual(resp['align'], 'neutral characters')

		h = {}
		h['name'] = 'Professor Kumar'
		h['align'] = 'good characters'
		h['alive'] = 'living characters'
		h['sex'] = 'female characters'
		h['iden'] = 'public identity'
		r = requests.put(self.HEROES_URL + str(hero_id), data = json.dumps(h))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.HEROES_URL + str(hero_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['name'], h['name'])
		self.assertEqual(resp['align'], h['align'])
		self.assertEqual(resp['alive'], h['alive'])
		self.assertEqual(resp['sex'], h['sex'])
		self.assertEqual(resp['iden'], h['iden'])

	# test index get request
	def test_heroes_index_get(self):
		r = requests.get(self.HEROES_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())

		testhero = {}

		heroes = resp['heroes']

		for hero in heroes:
			if hero['id'] == 128:
				testhero = hero

		self.assertEqual(testhero['name'], 'wong (earth-616)')
		self.assertEqual(testhero['align'], 'good characters')
		self.assertEqual(testhero['alive'], 'living characters')
		self.assertEqual(testhero['sex'], 'male characters')
		self.assertEqual(testhero['iden'], 'no dual identity')

	def test_movies_index_post(self):

		h = {}
		h['name'] = 'Java Man'
		h['align'] = 'bad characters'
		h['alive'] = 'living characters'
		h['sex'] = 'male characters'
		h['iden'] = 'no dual identity'

		r = requests.post(self.HEROES_URL, data = json.dumps(h))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['id'], 16376)

		r = requests.get(self.HEROES_URL + str(resp['id']))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['name'], h['Java Man'])
		self.assertEqual(resp['align'], h['bad characters'])
		self.assertEqual(resp['alive'], h['living characters'])
		self.assertEqual(resp['sex'], h['male characters'])
		self.assertEqual(resp['iden'], h['no dual identity'])

	# test delete request with hero_id
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

	def test_movies_index_delete(self):
		h = {}
		r = requests.delete(self.HEROES_URL, data = json.dumps(h))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.HEROES_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		heroes = resp['heroes']
		self.assertFalse(heroes)


if __name__ == "__main__":
	unittest.main()
