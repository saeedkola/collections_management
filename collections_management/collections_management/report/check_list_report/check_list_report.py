# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.site:
		filters.site = ""

	sqlq = """select name, q1.warehouse, coalesce(count,0) as count  from
			(
				select name,warehouse from tabAsset
				WHERE warehouse like '%{}%' AND warehouse != 'Machines - TSU'
			)q1
			left join
			(
				select a.machine_number, count(machine_number) as count
				from `tabCollection Entry` a
				where a.site like '%{}%' AND a.site != 'Machines - TSU' AND a.docstatus = 1 AND a.creation BETWEEN '{}' AND '{}'
				group by machine_number

			) q2
			ON q2.machine_number = q1.name
			ORDER BY count ASC""".format(filters.site,filters.site,filters.from_date,filters.to_date)
	columns = [
		"Machine No.:Link/Asset:100",
		"Site:Link/Warehouse:100",
		"No. Of Collections:Int:100"

	]
	data = frappe.db.sql(sqlq,as_list=1)
	return columns, data
