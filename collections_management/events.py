from __future__ import unicode_literals
import frappe
from frappe.utils import flt, add_days, nowdate
import datetime

def send_mail():

	settings = frappe.get_single("Collections Settings")
	if settings.notification_users and settings.uncoll_num_days:
		recipients = []
		for user in settings.notification_users:
			recipients.append(str(user.user))
		num_days = settings.uncoll_num_days
		subject = "{} Days Uncollected Summary".format(num_days)
		summary = get_location_wise_uncollected_since(num_days,"dict")
		if summary:

			options = {
			"summary" : summary,
			"num_days": num_days
			}

			message = frappe.render_template('templates/pages/notification_email_template.html',options)
			frappe.sendmail(recipients=recipients, subject=subject, message=message,now=True)
		else:
			print("None")



def get_uncollected_machines_since(no_of_days=15,response_format="list",site_filter=None):
	excluded_locations = []
	settings = frappe.get_single("Collections Settings")
	for location in settings.excluded_locations:
		excluded_locations.append(location.location)
	excluded_locations = "'{}'".format("','".join(excluded_locations))
	sqlq = """select name, location, LastCollected, datediff(curdate(), LastCollected) numDays from `tabAsset`
			left join (
				select machine_number, max(creation) LastCollected from `tabCollection Entry`
				group by machine_number) La
			on La.machine_number = `tabAsset`.name
			where location not in ({excluded_locations})""".format(excluded_locations=excluded_locations)
	if site_filter:
		sqlq = sqlq + """ and location='{}'""".format(site_filter,excluded_locations=excluded_locations)

	sqlq = sqlq + """ 
			and  `tabAsset`.creation not between DATE_SUB(NOW(), INTERVAL {no_days} DAY) and now()
			and name not in (
				select distinct machine_number from `tabCollection Entry` where creation between DATE_SUB(NOW(), INTERVAL {no_days} DAY) and now()
			    )
			order by LastCollected ASC""".format(no_days=no_of_days)
	if response_format=="list":
		response = frappe.db.sql(sqlq,as_list=1)
	elif response_format == "dict":
		response = frappe.db.sql(sqlq,as_dict=1)

	return response

def get_location_wise_uncollected_since(no_of_days=15, response_format="list"):
	excluded_locations = []
	settings = frappe.get_single("Collections Settings")
	for location in settings.excluded_locations:
		excluded_locations.append(location.location)
	
	excluded_locations = "'{}'".format("','".join(excluded_locations))
	sqlq = """select t1.location site,(site_machines-count(t1.location)) collected, count(t1.location) uncollected_machines, t2.site_machines machines_on_site from `tabAsset` t1
				left join 
					(
						select location, count(location) site_machines from tabAsset
						group by location
					) t2
				on t1.location = t2.location
				where t1.location not in ({excluded_locations}) 
				and  t1.creation not between DATE_SUB(NOW(), INTERVAL {no_days} DAY) and now()
				and name not in 
					(
						select distinct machine_number from `tabCollection Entry` where creation between DATE_SUB(NOW(), INTERVAL {no_days} DAY) and now()
				    )
				group by t1.location
				order by collected DESC, uncollected_machines desc;""".format(no_days=no_of_days,excluded_locations=excluded_locations)
	print(sqlq)
	if response_format=="list":
		response = frappe.db.sql(sqlq,as_list=1)
	elif response_format == "dict":
		response = frappe.db.sql(sqlq,as_dict=1)

	return response