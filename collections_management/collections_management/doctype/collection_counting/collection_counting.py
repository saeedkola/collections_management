# -*- coding: utf-8 -*-
# Copyright (c) 2018, Element Labs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe,erpnext
from frappe.model.document import Document
from frappe import _
from frappe.utils import money_in_words
from frappe.utils.csvutils import getlink
from erpnext.controllers.accounts_controller import AccountsController


class CollectionCounting(AccountsController):
	def validate(self):
		ce = frappe.get_doc('Collection Entry',self.collection_entry)
		self.machine_number = ce.machine_number
		self.expected_count = ce.coins_expected
		self.error = self.expected_count-self.coin_count-self.commissions_paid



@frappe.whitelist()
def collection_entry_query(doctype, txt, searchfield, start, page_len, filters):
	from erpnext.controllers.queries import get_match_cond
	condition = ""

	return frappe.db.sql("""select t1.name, t1.machine_number, t1.site from `tabCollection Entry` t1
			left join `tabCollection Counting` t2 on t2.collection_entry = t1.name
			where t2.name IS NULL and t1.entry_type = "Collection Entry"
			and (t1.`{key}` LIKE %(txt)s
				{condition} {match_condition}
			or t1.machine_number LIKE %(txt)s
				{condition} {match_condition}
				)
			order by t1.idx desc, t1.name"""
			.format(condition=condition, match_condition=get_match_cond(doctype), key=searchfield), {
				'txt': "%%%s%%" % frappe.db.escape(txt)
			})

