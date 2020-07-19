import cherrypy
import re, json
import time
from heroes_library import _hero_database

class HeroController(object):

	def __init__(self, hdb=None, am=None):
		if hdb is None:
			self.hdb = _hero_database()
		else:
			self.hdb = hdb

		self.hdb.load_heroes('marvel-wikia-data_json.json')

	def GET_KEY(self, hero_id):
		output = {'result' : 'success'}
		hero_id = int(hero_id)
		time.sleep(5)
		try:
			hero = self.hdb.get_hero(hero_id)
			if hero is not None:
				output['id'] = hero_id
				output['name'] = hero[0]
				output['align'] = hero[1]
				output['alive'] = hero[2]
				output['sex'] = hero[3]
				output['iden'] = hero[4]
			else:
				output['result'] = 'error'
				output['message'] = str(ex)

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def GET_QUERY(self, query):
		output = {'result':'success', 'hero_list':list()}

		query = str(query)

		try:
			for hid in self.hdb.get_heroes():
				hero = self.hdb.get_hero(hid)
				match_dict = search_compare(hero[0], query, {'match':''})
				if match_dict['match'] == 'true':
					hd = {}
					hd['id'] = hero_id
					hd['name'] = hero[0]
					hd['align'] = hero[1]
					hd['alive'] = hero[2]
					hd['sex'] = hero[3]
					hd['iden'] = hero[4]
					output['hero_list'].append(hd)

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
			
		

	def PUT_KEY(self, hero_id):
		output = {'result' : 'success'}
		hero_id = int(hero_id)
		data = json.loads(cherrypy.request.body.read())

		hero = list()
		hero.append(data['name'])
		hero.append(data['align'])
		hero.append(data['alive'])
		hero.append(data['sex'])
		hero.append(data['iden'])

		self.hdb.set_hero(hero_id, hero)

		return json.dumps(output)

	def DELETE_KEY(self, hero_id):
		output = {'result': 'success'}
		hero_id = int(hero_id)
		self.hdb.delete_hero(hero_id)

		return json.dumps(output)

	def GET_INDEX(self):
		output = {'result': 'success'}
		output['heroes'] = []
		try:
			for hid in self.hdb.get_heroes():
				hero = self.hdb.get_hero(hid)
				dhero = {'id':hid, 'name':hero[0], 'align':hero[1], 'alive':hero[2], 'sex':hero[3], 'iden':hero[4]}
				output['heroes'].append(dhero)
			
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST_INDEX(self):
		output = {'result':'success'}
		data = json.loads(cherrypy.request.body.read().decode('utf-8'))
		i = max(self.hdb.get_heroes()) + 1
		output['id'] = i
		if len(data.keys()) > 1:
			try:
				name = data['name']
				align = data['align']
				alive = data['alive']
				sex = data['sex']
				identity = data['iden']
				herolist = list()
				herolist.append(name)
				herolist.append(align)
				herolist.append(alive)
				herolist.append(sex)
				herolist.append(identity)
				self.hdb.set_hero(i, herolist)

			except Exception as ex:
				print(ex)
				output['result'] = 'error'
				output['message'] = str(ex)

		return json.dumps(output)

	def DELETE_INDEX(self):
		output = {'result' : 'success'}
		try:
			hidlist = list(self.hdb.get_heroes())
			for hid in hidlist:
				self.hdb.delete_hero(hid)

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

