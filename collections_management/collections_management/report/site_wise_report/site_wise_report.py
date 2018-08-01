# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	sqlq = """select 
		a.site as "Site::100",
		SUM(a.coins_expected) as "Total Expected Coins:Int:100",
		SUM(b.coin_count) as "Total Counted Coins:Int:100",
		SUM(b.error) as "Error:Int:100",
		COUNT(a.machine_number) as "No of Collections::100",
		AVG(b.coin_count) as "AVG Coins per Collection::150"
	from `tabCollection Entry` a right join `tabCollection Counting` b 
	ON a.name = b.collection_entry
	where a.creation BETWEEN '{}' AND '{}'
	GROUP BY a.site""".format(filters.from_date,filters.to_date)

	columns = [
		"Site:Link/Warehouse:100",
		"Total Expected Coins:Int:100",
		"Total Counted Coins:Int:100",
		"Error:Int:100",
		"No of Collections::100",
		"AVG Coins per Collection::150"
	]

	data = frappe.db.sql(sqlq)
	return columns, data