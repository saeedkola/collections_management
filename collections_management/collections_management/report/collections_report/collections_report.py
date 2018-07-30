# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.machine_number:
		filters.machine_number = ""
	if not filters.site:
		filters.site = ""
	if not filters.collected_by:
		filters.collected_by = ""
	sqlq = """select 
			creation as "Collected On :Date:150",
			name as "Bag No.:Link/Collection Entry:100",
			machine_number as "Machine No.:Link/Asset:100",	
			site as "Site:Link/Warehouse:100",
			meter_reading as "Meter Reading::100",	
			previous_reading as "Previous Reading::100",
			coins_expected as "Expected Coins:Int:100",			
			owner as "Collected By::100"
		from `tabCollection Entry`
		where machine_number like '%{}%'
		and site like '%{}%'
		and owner like '%{}%'
		and creation BETWEEN '{}' AND '{}'
		""".format(filters.machine_number,filters.site,filters.collected_by,filters.from_date,filters.to_date)
	

	columns = [
		"Collected On :Date:150",
		"Bag No.:Link/Collection Entry:100",
		"Machine No.:Link/Asset:100",
		"Site:Link/Warehouse:100",
		"Meter Reading::100",
		"Previous Reading::100",
		"Expected Coins:Int:100",
		"Collected By::100"
	]

	data = frappe.db.sql(sqlq)
	
	return columns, data
