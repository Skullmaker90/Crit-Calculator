#!/usr/bin/python

class mass_calc(object):
	def __init__(self, hole_mass):
		self.int_dict = {'hole_mass': hole_mass, 'mass_remain': 0, 'total_hot_mass': 0, 'total_cold_mass': 0, 'hot_pass': 0, 'cold_pass': 0}
		self.mass_array = []
		self.hot_mass = int()
		self.cold_mass = int()

	def start_pass(self):
		a = self.int_dict
		a['total_hot_mass'] = self.get_hot_mass()
		a['total_cold_mass'] = self.get_cold_mass()
		mod = divmod(a['hole_mass'], a['total_hot_mass'])
		a['hot_pass'] = mod[0]
		a['mass_remain'] = mod[1]
		self.coarse_pass()

	def coarse_pass(self):
		a = self.int_dict
		if (a['hot_pass'] % 2 != 0 and a['cold_pass'] == 0):
			a['hot_pass'] = a['hot_pass'] + 1
			print("\n" + str(int(a['hot_pass'])) + " Combined Pass(es) Hot\n")
		elif (a['hot_pass'] % 2 == 0  and a['mass_remain'] / a['total_cold_mass'] > 1):
			print("\n" + str(int(a['hot_pass'])) + " Combined Passes Hot\n"
					"Then 1 Combined Pass Cold\n"
					"Then 1 Final Pass Hot.\n")
		elif (a['hot_pass'] % 2 != 0 and a['mass_remain'] / (a['total_cold_mass'] + (a['total_cold_mass'] * a['cold_pass'])) > 1):
			print("\n" + str(int(a['hot_pass'])) + " Combined Pass(es) Hot\n"
					"Then " + str(int(a['cold_pass'])) + " Combined Pass(es) Cold\n"
					"Then 1 Final Pass Hot.\n")
		elif ((a['hot_pass'] + a['cold_pass']) % 2 == 0 and a['cold_pass'] !=0 and a['mass_remain'] / a['total_cold_mass'] > 1):
			print("\n" + str(int(a['hot_pass'])) + " Combined Pass(es) Hot\n"
					"Then " + str(int(a['cold_pass'])) + " Combined Pass(es) Cold\n"
					"Then 1 Final Pass Hot.\n")
		else:
			self.fine_pass()
	
	def fine_pass(self):
		a = self.int_dict
		for ship in self.mass_array:
			if (a['hot_pass'] % 2 == 0 and a['mass_remain'] / ship[0] > 1 and a['mass_remain'] / ship[0] < 2):
				print("\n" + str(int(a['hot_pass'])) + " Combined Pass(es) Hot\n"
						"then 1 Pass Cold With " + ship[2] + "\n"
						"Then 1 Final Pass Hot.\n")
				return
		a['cold_pass'] = a['cold_pass'] + 1
		a['hot_pass'] = a['hot_pass'] - 1
		a['mass_remain'] = a['mass_remain'] + a['total_hot_mass'] - a['total_cold_mass']
		self.coarse_pass()


	def get_mass(self):
		ship_num = int(raw_input("How many ships you got?: "))
		for x in xrange(ship_num):
			y = float(raw_input("\nTotal ship mass in Tons (Check fitting window): ")) * 1000
			z = float(raw_input("Does your ship have an mwd?(1 for yes, 0 for no): "))
			zz = str(raw_input("Oh and what do you wanna name this ship?: "))
			self.mass_array.append([y, z, zz])
		self.start_pass()

	def get_hot_mass(self):
		for ship in self.mass_array:
        		self.hot_mass = self.hot_mass + ship[0]
        		if ship[1] == 1:
                		self.hot_mass = self.hot_mass + 50000000
		return self.hot_mass
	
	def get_cold_mass(self):
		for ship in self.mass_array:
			self.cold_mass = self.cold_mass + ship[0]
		return self.cold_mass
