# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "collections_management"
app_title = "Collections Management"
app_publisher = "Element Labs"
app_description = "This App Helps you track down your Collections"
app_icon = "fa fa-money"
app_color = "grey"
app_email = "saeed@elementlabs.xyz"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/collections_management/css/collections_management.css"
# app_include_js = "/assets/collections_management/js/collections_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/collections_management/css/collections_management.css"
# web_include_js = "/assets/collections_management/js/collections_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "collections_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "collections_management.install.before_install"
# after_install = "collections_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "collections_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"collections_management.tasks.all"
# 	],
# 	"daily": [
# 		"collections_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"collections_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"collections_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"collections_management.tasks.monthly"
# 	]
# }
scheduler_events = {
	"cron":{
		"0 9 * * *":[
			"collections_management.events.send_mail"
		]
	}
}

# Testing
# -------

# before_tests = "collections_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "collections_management.event.get_events"
# }

fixtures = [
    {"dt": "Custom Field", "filters": [["module", "=", "Collections Management"]]},
    {"dt": "Property Setter", "filters": [["module", "=", "Collections Management"]]},
]

doctype_js = {
    "Asset Movement": "public/js/asset_movement.js"
}



