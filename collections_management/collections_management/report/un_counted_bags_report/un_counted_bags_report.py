# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters.site:
		filters.site =""

    sqlq = """select t1.name as "Bag Number:Link/Collection Entry:100", 
		t1.machine_number as "Machine Numer:Link/Asset:100",
		t1.site as "Site: Link/Warehouse: 100",
		t1.owner as "Collected By::100",
		t1.creation as "Collected On:Datetime:100"
		from `tabCollection Entry` t1
		left join `tabCollection Counting` t2 on t2.collection_entry = t1.name
		where t2.name IS NULL 
		and t1.entry_type = "Collection Entry"
		and t1.creation BETWEEN '{}' AND '{}'
		and t1.site like '%{}%'
    """.format(filters.from_date,filters.to_date,filters.site)
    
    data = frappe.db.sql(sqlq,as_list=1)
    
    columns = [
    "Bag Number:Link/Collection Entry:100",
    "Machine Number:Link/Asset:100",
    "Site:Link/Warehouse:100",
    "Collected By::100",
    "Collected On:Datetime:100"
    ]
	
	return columns, data
