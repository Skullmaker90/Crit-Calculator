#!/usr/bin/python

import mysql_con, roll_calc
import locale
locale.setlocale(locale.LC_ALL, '')

def wh_info(wh_code):
	c = mysql_con.crit_db()
	wh_code = wh_code
	result = c.query(wh_code)
	try:
		x = ("\nName: " + str(result[0][0]) + "\n"
			"Leads to: " + str(result[0][1]) + "\n"
			"Max Stable Time: " + str(result[0][2]) + " Hours\n"
			"Max Mass: " + locale.format("%d", result[0][3], 1) + " kg\n"
			"Mass Regen: " + locale.format("%d", result[0][4], 1) + " Per Cycle\n"
			"Max Jump Mass: " + locale.format("%d", result[0][5], 1) + " kg\n")
		x = "<br />".join(x.split("\n"))
		return x

	except IndexError:
		return "Invalid WH code."
		# main()
def wh_calc(wh_code, params):
	c = mysql_con.crit_db()
	wh_code = wh_code
	result = c.query(wh_code)
	d = roll_calc.mass_calc(float(result[0][3]), params)
	return d.start_pass()
