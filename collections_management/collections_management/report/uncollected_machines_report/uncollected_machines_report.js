// Copyright (c) 2016, Element Labs and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Uncollected Machines Report"] = {
	"filters": [
		{
        	"fieldname"	:"site",
        	"label"		: __("Site"),
        	"fieldtype"	: "Link",
        	"options"	: "Location"
        },
        {
        	"fieldname"	:"num_days",
        	"label"		: __("Past no. of days"),
        	"fieldtype"	: "Int",
        	"reqd"		: 1,
        	"default"	: 15
        }
	]
}