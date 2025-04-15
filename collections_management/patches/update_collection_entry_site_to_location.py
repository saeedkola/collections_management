import frappe

def execute():
    _update_collection_entry_sites()

def _update_collection_entry_sites():
    # Step 1: Get all existing Location names
    location_names = set(
        frappe.get_all("Location", pluck="name")
    )

    # Step 2: Get all Collection Entries with " - TSU" suffix
    entries = frappe.get_all("Collection Entry", fields=["name", "site"])

    updated_count = 0
    for entry in entries:
        site = entry.site

        if not site or not site.endswith(" - TSU"):
            continue

        location_name = site.replace(" - TSU", "").strip()

        # Check in the preloaded set instead of hitting DB
        if location_name in location_names:
            frappe.db.set_value("Collection Entry", entry.name, "site", location_name, update_modified=False)
            updated_count += 1

            # Commit in batches for performance and safety
            if updated_count % 1000 == 0:
                frappe.db.commit()

    # Final commit
    frappe.db.commit()
    frappe.logger().info(f"[PATCH] Updated {updated_count} Collection Entry records with Location references.")
