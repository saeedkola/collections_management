// Copyright (c) 2018, Element Labs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Collection Counting', {
	refresh: function(frm) {

	},
	coin_count: function(frm){
		frm.set_value('error',frm.doc.expected_count-frm.doc.coin_count);
	}
});

frappe.ui.form.on("Collection Counting", "onload", function(frm) {
    cur_frm.set_query("collection_entry", function() {
        return {
        	query: "collections_management.collections_management.doctype.collection_counting.collection_counting.collection_entry_query"  
        };
    });
});

