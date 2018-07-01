// Copyright (c) 2018, Element Labs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Collection Settings', {
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
	}
});
