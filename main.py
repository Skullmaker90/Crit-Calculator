#!/usr/bin/python

import mysql_con, roll_calc
import locale
locale.setlocale(locale.LC_ALL, '')

def wh_info(db_con):
	c = db_con
	sys = raw_input("System: ")
	result = c.query(sys)
	try:
		print("\nName: " + str(result[0][0]) + "\n"
			"Leads to: " + str(result[0][1]) + "\n"
			"Max Stable Time: " + str(result[0][2]) + " Hours\n"
			"Max Mass: " + locale.format("%d", result[0][3], 1) + " kg\n"
			"Mass Regen: " + locale.format("%d", result[0][4], 1) + " Per Cycle\n"
			"Max Jump Mass: " + locale.format("%d", result[0][5], 1) + " kg\n")
	except IndexError:
		print("Invalid WH code.")
		main()
	d = roll_calc.mass_calc(float(result[0][3]))
	d.mass_calc()

def main():
	db_con = mysql_con.crit_db()
	wh_info(db_con)
main()
