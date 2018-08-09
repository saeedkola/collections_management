# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.site:
		filters.site = ""

	sqlq = """select name, q1.warehouse, collected_by,bag_number,counted_by  from
			(
				select name,warehouse from tabAsset
				WHERE warehouse like '%{}%'
			)q1
			left join
			(
				select a.machine_number,a.site,a.owner as collected_by, a.name as bag_number,b.owner as counted_by
				from `tabCollection Entry` a
				left join `tabCollection Counting` b
				ON a.name = b.collection_entry
				where a.site like '%{}%' AND a.creation BETWEEN '{}' AND '{}'

			) q2
			ON q2.machine_number = q1.name
			ORDER BY name DESC""".format(filters.site,filters.site,filters.from_date,filters.to_date)
	columns = [
		"Machine No.:Link/Asset:100",
		"Site:Link/Warehouse:100",
		"Collected By::100",
		"Bag Number:Link/Collection Entry:100",
		"Counted By::100"

	]
	data = frappe.db.sql(sqlq,as_list=1)
	return columns, data
