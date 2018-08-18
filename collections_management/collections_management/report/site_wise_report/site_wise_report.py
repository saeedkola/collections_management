# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	sqlq = """select 
	q2.warehouse, 
	q1.coins_expected, 
	q1.coin_count, 
	q1.error, 
	q1.no_of_collections, 
	q2.number, 
	q1.avg_count from
		(
		select warehouse,count(name) as number from tabAsset GROUP BY warehouse
		)q2
		left join
		(
		select a.site,
		 	SUM(a.coins_expected) as coins_expected,
			SUM(b.coin_count) as coin_count,
			SUM(b.error) as error,
			COUNT(a.machine_number) as no_of_collections,
			AVG(b.coin_count) as avg_count
		from `tabCollection Entry` a 
		right join `tabCollection Counting` b 
		ON a.name = b.collection_entry
		where a.creation BETWEEN '{}' AND '{}'
		GROUP BY a.site
		)q1
		ON q1.site = q2.warehouse""".format(filters.from_date,filters.to_date)

	columns = [
		"Site:Link/Warehouse:200",
		"Total Expected Coins:Int:100",
		"Total Counted Coins:Int:100",
		"Error:Int:100",
		"No of Collections::100",
		"No of Machines on Site:Int:100"
		"AVG Coins per Collection::100",
		
	]

	data = frappe.db.sql(sqlq,as_list=1)
	return columns, data