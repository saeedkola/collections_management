import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Machine No"), "fieldname": "machine_no", "fieldtype": "Link", "options": "Asset", "width": 150},
        {"label": _("Source Warehouse"), "fieldname": "source_warehouse", "fieldtype": "Link", "options": "Warehouse", "width": 180},
        {"label": _("Target Warehouse"), "fieldname": "target_warehouse", "fieldtype": "Link", "options": "Warehouse", "width": 180},
        {"label": _("Reason"), "fieldname": "custom_reason", "fieldtype": "Data", "width": 150},
        {"label": _("Transaction Date"), "fieldname": "transaction_date", "fieldtype": "Date", "width": 150},
    ]

    conditions = ""

    if filters.get("machine_no"):
        conditions += " AND (m.asset = %(machine_no)s OR i.asset = %(machine_no)s)"
    if filters.get("source_warehouse"):
        conditions += " AND (m.source_warehouse = %(source_warehouse)s OR i.source_location = %(source_warehouse)s)"
    if filters.get("target_warehouse"):
        conditions += " AND (m.target_warehouse = %(target_warehouse)s OR i.target_location = %(target_warehouse)s)"
    if filters.get("from_date") and filters.get("to_date"):
        conditions += " AND DATE(m.transaction_date) BETWEEN %(from_date)s AND %(to_date)s"
    elif filters.get("from_date"):
        conditions += " AND DATE(m.transaction_date) >= %(from_date)s"
    elif filters.get("to_date"):
        conditions += " AND DATE(m.transaction_date) <= %(to_date)s"
        
    data = frappe.db.sql(f"""
        SELECT
            IF(m.asset IS NOT NULL, m.asset, i.asset) AS machine_no,
            IF(m.source_warehouse IS NOT NULL, m.source_warehouse, i.source_location) AS source_warehouse,
            IF(m.target_warehouse IS NOT NULL, m.target_warehouse, i.target_location) AS target_warehouse,
            m.transaction_date AS transaction_date,
            m.custom_reason AS custom_reason
        FROM
            `tabAsset Movement` m
        LEFT JOIN
            `tabAsset Movement Item` i ON i.parent = m.name
        WHERE 1=1 {conditions}
        ORDER BY m.creation DESC
    """, filters, as_dict=True)

    return columns, data
