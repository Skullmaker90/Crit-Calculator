#!/usr/bin/python

import locale
locale.setlocale(locale.LC_ALL, '')

class mass_calc(object):
	def __init__(self, hole_mass, params):
		self.int_dict = {'hole_mass': hole_mass, 'mass_remain': 0, 'total_hot_mass': 0, 'total_cold_mass': 0, 'hot_pass': 0, 'cold_pass': 0}
		self.mass_array = params
		self.hot_mass = int()
		self.cold_mass = int()

	def start_pass(self):
		a = self.int_dict
		a['total_hot_mass'] = self.get_hot_mass()
		a['total_cold_mass'] = self.get_cold_mass()
		mod = divmod(a['hole_mass'], a['total_hot_mass'])
		a['hot_pass'] = mod[0]
		a['mass_remain'] = mod[1]
		return self.coarse_pass()

	def coarse_pass(self):
		a = self.int_dict
		print(a['mass_remain'])
		if (a['hot_pass'] % 2 != 0 and a['cold_pass'] == 0):
			a['hot_pass'] = a['hot_pass'] + 1
			x = ("\n" + str(int(a['hot_pass'])) + " Combined Pass(es) Hot\n"
				"With a remainder of: " + locale.format("%d", a['mass_remain'], 1) + " kg\n")
			x = "<br />".join(x.split("\n"))
			return x
		elif (a['hot_pass'] % 2 == 0  and a['mass_remain'] / a['total_cold_mass'] > 1):
			x = ("\n" + str(int(a['hot_pass'])) + " Combined Passes Hot\n"
					"Then 1 Combined Pass Cold\n"
					"Then 1 Final Pass Hot.\n"
					"With a remainder of: " + locale.format("%d", a['mass_remain'], 1) + " kg\n")
			x = "<br />".join(x.split("\n"))
			return x
		elif (a['hot_pass'] % 2 != 0 and a['mass_remain'] / (a['total_cold_mass'] + (a['total_cold_mass'] * a['cold_pass'])) > 1):
			x = ("\n" + str(int(a['hot_pass'])) + " Combined Pass(es) Hot\n"
					"Then " + str(int(a['cold_pass'])) + " Combined Pass(es) Cold\n"
					"Then 1 Final Pass Hot.\n"
					"With a remainder of: " + locale.format("%d", a['mass_remain'], 1) + " kg\n")
			x = "<br />".join(x.split("\n"))
			return x
		elif ((a['hot_pass'] + a['cold_pass']) % 2 == 0 and a['cold_pass'] !=0 and a['mass_remain'] / a['total_cold_mass'] > 1):
			x = ("\n" + str(int(a['hot_pass'])) + " Combined Pass(es) Hot\n"
					"Then " + str(int(a['cold_pass'])) + " Combined Pass(es) Cold\n"
					"Then 1 Final Pass Hot.\n"
					"With a remainder of: " + locale.format("%d", a['mass_remain'], 1) + " kg\n")
			x = "<br />".join(x.split("\n"))
			return x
		else:
			return self.fine_pass()
	
	def fine_pass(self):
		a = self.int_dict
		for ship in self.mass_array:
			if (a['hot_pass'] % 2 == 0 and a['mass_remain'] / int(ship[1]) > 1 and a['mass_remain'] / int(ship[1]) < 2):
				x = ("\n" + str(int(a['hot_pass'])) + " Combined Pass(es) Hot\n"
					"then 1 Pass Cold With " + str(ship[0]) + "\n"
						"Then 1 Final Pass Hot.\n"
						"With a remainder of: " + locale.format("%d", a['mass_remain'], 1) + " kg\n")
				x = "<br />".join(x.split("\n"))
				return x
		a['cold_pass'] = a['cold_pass'] + 1
		a['hot_pass'] = a['hot_pass'] - 1
		a['mass_remain'] = a['mass_remain'] + a['total_hot_mass'] - a['total_cold_mass']
		return self.coarse_pass()

	def get_hot_mass(self):
		for ship in self.mass_array:
			ship[1] = int(ship[1]) * 1000
        		self.hot_mass = self.hot_mass + int(ship[1])
        		if str(ship[2]) == 'on':
                		self.hot_mass = self.hot_mass + 50000000
		return self.hot_mass
	
	def get_cold_mass(self):
		for ship in self.mass_array:
			self.cold_mass = self.cold_mass + int(ship[1])
		return self.cold_mass
