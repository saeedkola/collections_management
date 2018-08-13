# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.site:
		filters.site = ""
	if not filters.collected_by:
		filters.collected_by = ""
	sqlq = """select 
			creation as "Collected On :Date:150",
			name as "Bag No.:Link/Collection Entry:100",
			entry_type,
			machine_number as "Machine No.:Link/Asset:100",
			site as "Site:Link/Warehouse:100",
			meter_reading as "Meter Reading::100",
			previous_reading as "Previous Reading::100",
			coins_expected as "Expected Coins::100",
			owner as "Collected By::100"
		from `tabCollection Entry`
		where site like '%{}%'
		and owner like '%{}%'
		and docstatus = 1
		and creation BETWEEN '{}' AND '{}'
		""".format(filters.site,filters.collected_by,filters.from_date,filters.to_date)
	if filters.machine_number:
		sqlq+="""and machine_number = '{}'""".format(filters.machine_number)
	

	columns = [
		"Collected On :Datetime:150",
		"Bag No.:Link/Collection Entry:100",
		"Entry Type ::100",
		"Machine No.:Link/Asset:100",
		"Site:Link/Warehouse:100",
		"Meter Reading::100",
		"Previous Reading::100",
		"Expected Coins:Currrency:100",
		"Collected By::100"
	]

	data = frappe.db.sql(sqlq,as_list=1)
	
	return columns, data
