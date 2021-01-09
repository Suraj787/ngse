# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "ngse"
app_title = "NGSE"
app_publisher = "Sambhaji Kolate"
app_description = "App for NGSE ERP"
app_icon = "icon-th-list"
app_color = "#2E70D2"
app_email = "kolate.sambhaji@gmail.com"
app_version = "0.0.1"
# fixtures = ["Custom Field",
# "Property Setter",
# "Custom Script",
# "Print Format"]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ngse.install.before_install"
# after_install = "ngse.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ngse.notifications.get_notification_config"

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

doc_events = {
	"Quotation": {
		"after_insert": "ngse.ngse.comments.comments_and_emails",
		# "on_cancel": "method",
		# "on_trash": "method"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ngse.tasks.all"
# 	],
# 	"daily": [
# 		"ngse.tasks.daily"
# 	],
# 	"hourly": [
# 		"ngse.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ngse.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ngse.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ngse.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ngse.event.get_events"
# }

