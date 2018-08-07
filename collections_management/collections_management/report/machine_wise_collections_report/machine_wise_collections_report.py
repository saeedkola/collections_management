# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.site:
		filters.site =""
	sqlq = """select 
		a.machine_number as "Machine No.:Link/Asset:100",
		a.site as "Site::100",
		SUM(a.coins_expected) as "Total Expected Coins:Int:100",
		SUM(b.coin_count) as "Total Counted Coins:Int:100",
		SUM(b.error) as "Error:Int:100",
		COUNT(a.machine_number) as "No of Collections::100",
		AVG(b.coin_count) as "AVG Coins per Collection::150"
	from `tabCollection Entry` a right join `tabCollection Counting` b 
	ON a.name = b.collection_entry
	where a.creation BETWEEN '{}' AND '{}'
	and a.site like '%{}%'
	GROUP BY a.machine_number, a.site""".format(filters.from_date,filters.to_date,filters.site)

	columns = [
		"Machine No.:Link/Asset:100",
		"Site:Link/Warehouse:100",
		"Total Expected Coins:Currency:100",
		"Total Counted Coins:Currency:100",
		"Error:Currency:100",
		"No of Collections::100",
		"AVG Coins per Collection::150"
	]

	data = frappe.db.sql(sqlq,as_list=1)
	return columns, data
