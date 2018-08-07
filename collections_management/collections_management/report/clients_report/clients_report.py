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
			a.site,
			a.creation,
			a.machine_number,
			a.previous_reading,
			a.meter_reading,	
			b.coin_count
		from `tabCollection Entry` a right join `tabCollection Counting` b 
		ON a.name = b.collection_entry
		where a.machine_number like '%{}%'
		and coalesce(a.site, '<NULL>') like '%{}%'
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

	data = frappe.db.sql(sqlq, as_list=1)
	
	return columns, data
