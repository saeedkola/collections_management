// Copyright (c) 2025, Element Labs and contributors
// For license information, please see license.txt

frappe.query_reports["Collection Detail"] = {
	"filters": [
		{
			"fieldname": "site",
			"label": __("Site"),
			"fieldtype": "Link",
			"options": "Location"
		}
	]
};
