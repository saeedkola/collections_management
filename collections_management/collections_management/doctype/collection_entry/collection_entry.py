# -*- coding: utf-8 -*-
# Copyright (c) 2018, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CollectionEntry(Document):
	def validate(self):
		# Validate asset field
		assets = frappe.db.count("Asset",{'name':self.machine_number})
		if assets:
			# get previous entry of the machine
			last_transaction = frappe.get_all("Collection Entry",
				fields=["meter_reading"],
				filters = {
					"machine_number": self.machine_number,
					"name": ("!=", self.name),
					"docstatus" : 1
				},
				order_by = "creation DESC")
			# if not last_transaction:
			# 	frappe.throw("Cannot find previous")
			if last_transaction:
				self.previous_reading = last_transaction[0].meter_reading
				if self.entry_type == 'Collection Entry':
					self.coins_expected = self.meter_reading-last_transaction[0].meter_reading
					if self.coins_expected == 0:
						frappe.throw('Duplicate Entry')
				else:
					self.coins_expected = 0
			else:
				self.coins_expected = self.meter_reading
		else:
			frappe.throw("Machine Number Does Not Exist")
