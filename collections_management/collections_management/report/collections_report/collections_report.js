// Copyright (c) 2016, Element Labs and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Collections Report"] = {
	"filters": [
		{
            "fieldname"	:"machine_number",
            "label"		: __("Machine Number"),
            "fieldtype"	: "Link",
            "options"	: "Asset"            
        },
        {
        	"fieldname"	:"site",
        	"label"		: __("Site"),
        	"fieldtype"	: "Link",
        	"options"	: "Warehouse"
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
        },
        {
        	"fieldname"	:"collected_by",
        	"label"		: __("Collection Agent"),
        	"fieldtype"	: "Link",
        	"options" 	: "User" 
        }
	]
}
