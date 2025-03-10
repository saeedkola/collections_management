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
# from erpnext.accounts.general_ledger import delete_gl_entries

class CollectionCounting(AccountsController):
	def validate(self):
		ce = frappe.get_doc('Collection Entry',self.collection_entry)
		self.machine_number = ce.machine_number
		self.expected_count = ce.coins_expected
		self.error = self.expected_count-self.coin_count

	# def on_submit(self):

	# 	self.make_gl_entries()
		
	# def make_gl_entries(self):
	# 	settings = frappe.get_single('Collections Settings')
	# 	gl_entries = []
		
	# 	#cash entry
	# 	gl_entries.append(
	# 		self.get_gl_dict({
	# 			"account": settings.cash_account,
	# 			"against": settings.collections_account,
	# 			"debit": self.coin_count,
	# 			"debit_in_account_currency": self.coin_count,
	# 			"voucher_no": self.name,
	# 			"voucher_type": self.doctype
	# 		})
	# 	)
		
	# 	#collections_entry 
	# 	gl_entries.append(
	# 		self.get_gl_dict({
	# 			"account": settings.collections_account,
	# 			"against": self.machine_number,
	# 			"credit": self.coin_count,
	# 			"credit_in_account_currency": self.coin_count,
	# 			"cost_center": settings.cost_center,
	# 			"voucher_no": self.name,
	# 			"voucher_type": self.doctype
	# 		})
	# 	)			
		
	# 	ce = frappe.get_doc('Collection Entry',self.collection_entry)
	# 	site = frappe.get_doc('Warehouse',ce.site)
		
	# 	if site.party and site.percentage:
	# 		#commissions account entry
	# 		gl_entries.append(
	# 			self.get_gl_dict({
	# 				"account": settings.commissions_account,
	# 				"against": site.party,
	# 				"debit": self.coin_count*site.percentage/100,
	# 				"debit_in_account_currency": self.coin_count*site.percentage/100,
	# 				"cost_center": settings.cost_center,
	# 				"voucher_no": self.name,
	# 				"voucher_type": self.doctype,
	# 				"remarks": "{}% of {} collected from Machine Number {} Bag Number {}".format(site.percentage, self.coin_count, ce.machine_number, self.collection_entry)
	# 			})
	# 		)
	# 		#commissions payable entry
	# 		gl_entries.append(
	# 			self.get_gl_dict({
	# 				"account": settings.commissions_payable,
	# 				"party_type": "Supplier",
	# 				"party": site.party,
	# 				"against": settings.commissions_account,
	# 				"credit" : self.coin_count*site.percentage/100,
	# 				"credit_in_account_currency": self.coin_count*site.percentage/100,
	# 				"voucher_no": self.name,
	# 				"voucher_type": self.doctype,
	# 				"remarks": "{}% of {} collected from Machine Number {} Bag Number {}".format(site.percentage, self.coin_count, ce.machine_number, self.collection_entry)

	# 			})
	# 		)
	# 	from erpnext.accounts.general_ledger import make_gl_entries
	# 	make_gl_entries(gl_entries, cancel=(self.docstatus == 2),
	# 		update_outstanding="Yes", merge_entries=False)		
	# def on_cancel(self):
	# 	delete_gl_entries(voucher_type=self.doctype, voucher_no=self.name)


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

