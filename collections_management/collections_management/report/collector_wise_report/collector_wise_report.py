# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):

	sqlq = """select 
		a.modified_by,
		SUM(a.coins_expected),
		SUM(b.coin_count),
		SUM(b.error),
		COUNT(a.modified_by)
	from `tabCollection Entry` a right join `tabCollection Counting` b 
	ON a.name = b.collection_entry
	where a.creation BETWEEN '{}' AND '{}'
	GROUP BY a.modified_by""".format(filters.from_date,filters.to_date)

	columns = [
		"Collected By::100",
		"Total Expected Coins:Currency:100",
		"Total Counted Coins:Currency:100",
		"Error:Currency:100",
		"No of Collections::100"
	]

	data = frappe.db.sql(sqlq,as_list=1)
	return columns, data
