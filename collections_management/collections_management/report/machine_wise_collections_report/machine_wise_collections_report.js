// Copyright (c) 2016, Element Labs and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Machine-Wise Collections Report"] = {
	"filters": [
		{
        	"fieldname"	:"site",
        	"label"		: __("Site"),
        	"fieldtype"	: "Link",
        	"options"	: "Location"
        },
        {
        	"fieldname"	:"from_date",
        	"label"		: __("From Date"),
        	"fieldtype"	: "Datetime",
        	"reqd"		: 1,
        	"default"	: frappe.datetime.add_months(frappe.datetime.get_today(), -1)
        },
        {
        	"fieldname"	:"to_date",
        	"label"		: __("To Date"),
        	"fieldtype"	: "Datetime",
        	"reqd"		: 1,
        	"default"	: frappe.datetime.get_today()
        }
	]
}
