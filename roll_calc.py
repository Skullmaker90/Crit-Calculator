#!/usr/bin/python

class mass_calc(object):
	def __init__(self, hole_mass):
		self.hole_mass = hole_mass
		self.cold_pass = 0
		self.hot_pass = 0

	def init_pass(self, hole_mass, hot_mass, ship_mass):
		self.a, self.b, self.c = hole_mass, hot_mass, ship_mass
		self.mod = divmod(self.a, self.b)
		self.hot_pass = self.mod[0]
		self.remainder = self.mod[1]
		self.solve_pass()

	def solve_pass(self):
		if (self.hot_pass % 2 != 0 and self.cold_pass == 0):
			self.hot_pass = self.hot_pass + 1
			print(str(int(self.hot_pass)) + " Pass(es) Hot\n")
		elif (self.hot_pass % 2 == 0  and self.remainder / self.c > 1):
			print(str(int(self.hot_pass)) + " Pass(es) Hot\n"
					"Then 1 Pass Cold\n"
					"Then 1 Final Pass Hot.\n")
		elif (self.hot_pass % 2 != 0 and self.remainder / (self.c + (self.c * self.cold_pass)) > 1):
			print(str(int(self.hot_pass)) + " Pass(es) Hot\n"
					"Then " + str(int(self.cold_pass)) + " Pass(es) Cold\n"
					"Then 1 Final Pass Hot.")
		elif ((self.hot_pass + self.cold_pass) % 2 == 0 and self.cold_pass !=0 and self.remainder / self.c > 1):
			print(str(int(self.hot_pass)) + " Pass(es) Hot\n"
					"Then " + str(int(self.cold_pass)) + " Pass(es) Cold\n"
					"Then 1 Final Pass Hot")
		else:			
			self.cold_pass = self.cold_pass + 1
			self.hot_pass = self.hot_pass - 1
			self.remainder = self.remainder + self.b - self.c
			self.solve_pass()

	def mass_calc(self):
		self.ship_mass = float(raw_input("Total ship mass in Tons (Check fitting window): ")) * 1000
		self.mwd_mass = float(raw_input("Total number of mwd's: ")) * 50000000
		self.total_hot_mass = (self.ship_mass + self.mwd_mass)
		self.init_pass(self.hole_mass, self.total_hot_mass, self.ship_mass)
