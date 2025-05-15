// …same file: your_app/public/js/collection_details.js
frappe.pages['collection-details'].on_page_load = function (wrapper) {
    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: __("Collection Details"),
        single_column: true,
    });

    // ── fields ─────────────────────────────────────────
    const site_field = page.add_field({
        fieldtype: "Link",
        fieldname: "site",
        label: __("Site"),
        options: "Location",
        reqd: 1,
    });
    const date_field = page.add_field({
        fieldtype: "Date",
        fieldname: "date",
        label: __("Date"),
        default: frappe.datetime.get_today(),
    });

    // ── PDF (already present) ─────────────────────────
    page.set_primary_action(__("Export PDF"), () => {
        const site = site_field.get_value();
        if (!site) return frappe.msgprint(__("Please pick a Site first"));
        const date = date_field.get_value();

        frappe.call({
            method: "collections_management.collections_management.page.collection_details.collection_details.get_collection_pdf",
            args: { site, date },
            freeze: true,
            freeze_message: __("Building PDF…"),
        }).then(r => {
            if (r.message) {
                const url = "/api/method/frappe.core.doctype.file.file.download_file?file_url="
                          + encodeURIComponent(r.message);
                window.open(url);
            }
        });
    });

    // ── NEW  Excel button ─────────────────────────────
    page.add_inner_button(__("Export Excel"), () => {
        const site = site_field.get_value();
        if (!site) return frappe.msgprint(__("Please pick a Site first"));
        const date = date_field.get_value();

        frappe.call({
            method: "collections_management.collections_management.page.collection_details.collection_details.get_collection_excel",
            args: { site, date },
            freeze: true,
            freeze_message: __("Building Excel…"),
        }).then(r => {
            if (r.message) {
                const url = "/api/method/frappe.core.doctype.file.file.download_file?file_url="
                          + encodeURIComponent(r.message);
                window.open(url);
            }
        });
    });
};
