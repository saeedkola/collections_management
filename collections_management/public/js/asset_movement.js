frappe.ui.form.on('Asset Movement', {
    validate: function(frm) {
        if (!frm.doc.custom_reason) {
            frappe.throw(__('Reason is required.'));
        }
        if (!frm.doc.custom_user) {
            frappe.throw(__('User is required.'));
        }
        if (!frm.doc.custom_attachment) {
            frappe.throw(__('Attachment is required.'));
        }
    }
});wsl