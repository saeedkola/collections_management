# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe


def execute():
	# Submitting a Collection Entry scanned all of `tabCollection Entry` twice:
	# once in CollectionEntry.validate() for the previous meter reading, and once
	# for the duplicate check the mobile app runs before it posts.
	#
	# index_name is passed explicitly so this matches the indexes already applied
	# by hand on production; without it frappe derives `<fields>_index` and would
	# add a second, redundant copy of each.
	frappe.db.add_index(
		"Collection Entry",
		["machine_number", "docstatus", "creation"],
		index_name="idx_machine_docstatus_creation",
	)
	frappe.db.add_index(
		"Collection Entry",
		["machine_number", "meter_reading"],
		index_name="idx_machine_meter",
	)
