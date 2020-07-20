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
			hero = none
			print(str(e))

		return hero

	def set_hero(self, hid, hero):
		self.hero_names[hid] = hero[0]
		self.hero_align[hid] = hero[1]
		self.hero_alive[hid] = hero[2]
		self.hero_sex[hid] = hero[3]
		self.hero_iden[hid] = hero[4]
		
	def delete_hero(self):
		del(self.hero_names[hid])
		del(self.hero_align[hid])
		del(self.hero_alive[hid])
		del(self.hero_sex[hid])
		del(self.hero_iden[hid])


if __name__ == "__main__":
	hdb = _hero_database()

	hdb.load_heroes('heroes.dat')
	
	heroes = hdb.get_heroes()
	for h in heroes:
		hero = hdb.get_hero(h)
		print(hero[0])


