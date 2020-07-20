import json

class _hero_database:
	def __init__(self):
		self.hero_names = dict()
		self.hero_align = dict()
		self.hero_alive = dict()
		self.hero_sex = dict()
		self.hero_iden = dict()

	def load_heroes(self, heroes_file):
		f = open(heroes_file)
		data = json.load(f)
		i = 0
		for hero in data:
			name = hero['name']
			align = hero['align']
			alive = hero['alive']
			sex = hero['sex']
			iden = hero['id']
			
			self.hero_names[i] = name
			self.hero_align[i] = align
			self.hero_alive[i] = alive
			self.hero_sex[i] = sex
			self.hero_iden[i] = iden

			i = i + 1

		f.close()

	def get_heroes(self):
		return self.hero_names.keys()

	def get_hero(self, hid):
		try:
			hname = self.hero_names[hid]
			halign = self.hero_align[hid]
			halive = self.hero_alive[hid]
			hsex = self.hero_sex[hid]
			hiden = self.hero_iden[hid]
			hero = list((hname, halign, halive, hsex, hiden))
		except Exception as e:
			hero = None
			print(str(e))

		return hero

	def set_hero(self, hid, hero):
		self.hero_names[hid] = hero[0]
		self.hero_align[hid] = hero[1]
		self.hero_alive[hid] = hero[2]
		self.hero_sex[hid] = hero[3]
		self.hero_iden[hid] = hero[4]
		
	def delete_hero(self, hid):
		del(self.hero_names[hid])
		del(self.hero_align[hid])
		del(self.hero_alive[hid])
		del(self.hero_sex[hid])
		del(self.hero_iden[hid])
		

def string_compare(s1, s2):
	match = {'match':'false'}
	i = 0
	
	while (i <= len(s1)-1) and (i <= len(s2)-1) and (s1[i] == s2[i]):
		i = i + 1
		
	if i >= 6:
		match['match'] = 'true'
		match['rate'] = i
		
	return match
	

def search_compare(string1, string2, match):
	if match['match'] == 'true':
		print('the term has been matched')
		return match


	if string1 != '':
		if string1[0] == string2[0]:
			match = string_compare(string1, string2)
			if match['match'] == 'true':
				return match
		else:
			match = search_compare(string1[1:], string2, match)

	return match

def sort_key(match):
	return int(match['rate'])
			

if __name__ == "__main__":
	hdb = _hero_database()

	hdb.load_heroes('heroes.dat')
	hero = hdb.get_hero(3)

	match_dict = search_compare(hero[0], "iron man",{'match':''})

	#match = string_compare("hello my good pal", "hello there best friend")
		
	print(json.dumps(match_dict))
	
	# heroes = hdb.get_heroes()
	# for h in heroes:
	#	hero = hdb.get_hero(h)
	#	print(hero[0])


