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
	if not filters.counted_by:
		filters.counted_by = ""
	sqlq = """select 
			a.creation as "Collected On :Date:150",
			a.name as "Bag No.:Link/Collection Entry:100",
			a.machine_number as "Machine No.:Link/Asset:100",	
			a.site as "Site:Link/Warehouse:100",
			a.meter_reading as "Meter Reading::100",	
			a.previous_reading as "Previous Reading::100",
			a.coins_expected as "Expected Coins:Int:100",
			b.coin_count as "Counted Coins:Int:100",
			b.error as "Error:Int:100",
			a.owner as "Collected By::100",
			b.owner as "Counted By::100",
			b.modified as "Counted On:Date:150"
		from `tabCollection Entry` a right join `tabCollection Counting` b 
		ON a.name = b.collection_entry
		where a.site like '%{}%'
		and a.owner like '%{}%'
		and b.owner like '%{}%'
		and a.creation BETWEEN '{}' AND '{}'
		""".format(filters.site,filters.collected_by,filters.counted_by,filters.from_date,filters.to_date)
	if filters.machine_number:
		sqlq+="""and machine_number = '{}'""".format(filters.machine_number)
	

	columns = [
		"Collected On :Date:150",
		"Bag No.:Link/Collection Entry:100",
		"Machine No.:Link/Asset:100",
		"Site:Link/Warehouse:100",
		"Meter Reading::100",
		"Previous Reading::100",
		"Expected Coins:Int:100",
		"Counted Coins:Int:100",
		"Error:Int:100",
		"Collected By::100",
		"Counted By::100",
		"Counted On:Date:150"
	]

	data = frappe.db.sql(sqlq)
	
	return columns, data
