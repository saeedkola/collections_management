# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.machine_number:
		filters.machine_number = ""
	if not filters.site:
		filters.site = ""
	sqlq = """select 
			a.site as "Site:Link/Warehouse:100",
			a.creation as "Collected On :Date:150",
			a.machine_number as "Machine No.:Link/Asset:100",
			a.previous_reading as "Previous Reading::100",
			a.meter_reading as "Meter Reading::100",	
			b.coin_count as "Counted Coins:Int:100"
		from `tabCollection Entry` a right join `tabCollection Counting` b 
		ON a.name = b.collection_entry
		where a.machine_number like '%{}%'
		and a.site like '%{}%'
		and a.creation BETWEEN '{}' AND '{}'
		""".format(filters.machine_number,filters.site,filters.from_date,filters.to_date)
	

	columns = [
		"Site:Link/Warehouse:100",
		"Collected On :Date:150",
		"Machine No.:Link/Asset:100",
		"Previous Reading::100",
		"Meter Reading::100",
		"Counted Coins:Int:100"
	]

	data = frappe.db.sql(sqlq)
	
	return columns, data
