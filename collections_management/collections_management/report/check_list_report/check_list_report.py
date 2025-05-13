# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.site:
		filters.site = ""
	settings = frappe.get_single("Collections Settings")

	excluded_locations = []
	for location in settings.excluded_locations:
		excluded_locations.append(location.location)

	excluded_locations = "'{}'".format("','".join(excluded_locations))
	having_clause = ""
	if filters.no_of_collections:
		having_clause = "HAVING count = {}".format(filters.no_of_collections)

	sqlq = """select name, q1.location, coalesce(count,0) as count  from
			(
				select name,location from tabAsset
				WHERE location like '%{site}%' AND location not in ({excluded_locations})
			)q1
			left join
			(
				select a.machine_number, count(machine_number) as count
				from `tabCollection Entry` a
				where a.site like '%{site}%' AND a.site not in ({excluded_locations}) AND a.docstatus = 1 AND a.creation BETWEEN '{from_date}' AND '{to_date}'
				group by machine_number

			) q2
			ON q2.machine_number = q1.name
			{having}
			ORDER BY count ASC""".format(site=filters.site,excluded_locations=excluded_locations,from_date=filters.from_date,to_date=filters.to_date,having=having_clause)
	columns = [
		"Machine No.:Link/Asset:100",
		"Site:Link/Location:100",
		"No. Of Collections:Int:100"

	]
	data = frappe.db.sql(sqlq,as_list=1)
	return columns, data
