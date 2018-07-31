# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.site:
		filters.site = ""
	if not filters.collected_by:
		filters.collected_by = ""
	if not filters.counted_by:
		filters.counted_by = ""
	sqlq = """select 
			a.creation,
			a.name,
			a.machine_number,	
			a.site,
			a.meter_reading,	
			a.previous_reading,
			a.coins_expected,
			b.coin_count,
			b.error,
			a.owner,
			b.owner,
			b.modified
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
