// Copyright (c) 2018, Element Labs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Collection Counting', {
	refresh: function(frm) {

	},
	coin_count: function(frm){
		// frm.set_value('error',frm.doc.expected_count-frm.doc.coin_count);
	},
	barcode: function(frm){
		frm.set_value('collection_entry',frm.doc.barcode);
		frm.refresh_field('collection_entry');
	}
});

frappe.ui.form.on('Collection Counting', {
    onload(frm) {
        // Limit the link‑field list to un‑counted collection entries
        frm.set_query('collection_entry', () => {
            return {
                query: 'collections_management.api.get_uncounted_collection_entries'
            };
        });
    }
});

