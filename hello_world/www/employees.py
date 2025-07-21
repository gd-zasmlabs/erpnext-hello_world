import frappe
from frappe import _
import requests

def get_context(context):
    # Fetch all enabled employees with relevant fields

    response = requests.post("https://randomuser.me/api/")
    request.body = {
        "workorder" : "12345",
    }
    if response.status_code == 200:
        context.random_user = response.json().get("results", [])[0]
    else:
        context.random_user = None

    employees = frappe.get_all(
        "Employee",
        filters={"status": "Active"},
        fields=["name", "employee_name", "gender"]
    )

    context.title = _("Employee Directory")
    context.employees = response
    return context
