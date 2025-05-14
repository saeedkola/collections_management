# Copyright (c) 2025, Element Labs and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	

	columns = [
		{
			"fieldname": "name",
			"label": "Asset Name",
			"fieldtype": "Link",
			"options": "Asset",
			"width": 150,
		},
		{
			"fieldname": "location",
			"label": "location",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"fieldname": "remarks",
			"label": "Remarks",
			"fieldtype": "Data",
			"width": 150,
		},

	]
	machines = frappe.get_all("Asset",filters=[
		["location","descendants of",filters.get("site")],
	],fields =["name","location"], order_by="location asc")
		
	data = machines
	return columns, data
