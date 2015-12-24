#!/usr/bin/python

import MySQLdb

class crit_db(object):
	def __init__(self):
		try:
			self.a = MySQLdb.connect(user="critcalc", passwd="", db="evedump")
			self.b = self.a.cursor()
		except:
			self.b.close()

	def query(self, wh):
		self.wh = wh
		self.b.execute("SELECT * FROM wormholeStats WHERE Name = '%s'" % (self.wh,))
		return self.b.fetchall()
