// Copyright (c) 2018, Element Labs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Collections Settings', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		frm.set_query("collections_account",function(){
			return {
				"filters":{
					"account_type":"Income Account"
				}
			}
		});
		frm.set_query("cash_account",function(){
			return {
				"filters":{
					"account_type":"Cash"
				}
			}
		});
		frm.set_query("cost_center",function(){
			return {
				"filters":{
					"is_group": 0
				}
			}
		});
		frm.set_query("commissions_payable",function(){
			return {
				"filters":{
					"account_type":"Payable"
				}
			}
		});
		frm.set_query("commissions_account",function(){
			return {
				"filters":{
					"account_type":"Expense Account"
				}
			}
		});
	}
});
