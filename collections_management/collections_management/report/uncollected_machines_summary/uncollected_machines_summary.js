// Copyright (c) 2016, Element Labs and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Uncollected Machines Summary"] = {
	"filters": [
        {
        	"fieldname"	:"num_days",
        	"label"		: __("Past no. of days"),
        	"fieldtype"	: "Int",
        	"reqd"		: 1,
        	"default"	: 15
        }
	]
}
