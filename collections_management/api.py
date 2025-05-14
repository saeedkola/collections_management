import frappe

@frappe.whitelist()
def get_uncounted_collection_entries(doctype, txt, searchfield, start, page_len, filters):
    """
    Link‑field query that returns Collection Entry names that do **not**
    yet appear in any submitted/draft Collection Counting document.

    Called automatically by frm.set_query() on the client side.
    """
    return frappe.db.sql(
        """
        SELECT ce.name, ce.machine_number, ce.meter_reading
        FROM `tabCollection Entry` AS ce
        WHERE ce.name NOT IN (
              SELECT cc.collection_entry
              FROM `tabCollection Counting` AS cc
              WHERE cc.collection_entry IS NOT NULL
        )
        AND (ce.name LIKE %(txt)s OR ce.machine_number LIKE %(txt)s)
        AND ce.entry_type = "Collection Entry"
        AND ce.docstatus = 1
        ORDER BY ce.modified DESC
        LIMIT %(start)s, %(page_len)s
        """,
        {
            "txt": f"%{txt}%",
            "start": start,
            "page_len": page_len,
        },
    )
