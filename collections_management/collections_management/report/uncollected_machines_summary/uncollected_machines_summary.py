# Copyright (c) 2013, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from collections_management.events import get_warehouse_wise_uncollected_since


def execute(filters=None):
	if not filters.num_days:
		filters.num_days = 15
	data = get_warehouse_wise_uncollected_since(no_of_days=filters.num_days, response_format="list")
	columns = [
		"Site:Link/Warehouse:200",
		"Collected #:Int:100",
		"Uncollected #:Int:100",
		"Total #:Int:100"

	]
	return columns, data
