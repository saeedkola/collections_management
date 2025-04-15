# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.site:
		filters.site = ""
	if not filters.collected_by:
		filters.collected_by = ""
	sqlq = """select creation,name,entry_type,machine_number,site,
			meter_reading,previous_reading,coins_expected,owner
		from `tabCollection Entry`
		where site like '%{}%'
		and owner like '%{}%'
		and docstatus = 1
		and creation BETWEEN '{}' AND '{}'
		""".format(filters.site,filters.collected_by,filters.from_date,filters.to_date)
	if filters.machine_number:
		sqlq+="""and machine_number = '{}'""".format(filters.machine_number)
	

	columns = [
		"Collected On:Datetime:150",
		"Bag No.:Link/Collection Entry:100",
		"Entry Type ::100",
		"Machine No.:Link/Asset:100",
		"Site:Link/Location:100",
		"Meter Reading::100",
		"Previous Reading::100",
		"Expected Coins:Currency:100",
		"Collected By::100"
	]

	data = frappe.db.sql(sqlq,as_list=1)
	
	return columns, data
