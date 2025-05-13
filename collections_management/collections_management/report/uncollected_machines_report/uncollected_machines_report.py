# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from collections_management.events import get_uncollected_machines_since

def execute(filters=None):
	if not filters.site:
		filters.site = None
	if not filters.num_days:
		filters.num_days = 15

	data = get_uncollected_machines_since(no_of_days=filters.num_days,response_format="list",site_filter=filters.site)
	columns = [
		"Machine No.:Link/Asset:100",
		"Site:Link/Warehouse:200",
		"Last Collected:Datetime:150",
		"Days since Last Collected:Int:100"

	]

	return columns, data
