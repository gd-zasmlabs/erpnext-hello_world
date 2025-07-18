import frappe
from frappe import _

def get_context(context):
    # Fetch all enabled employees with relevant fields
    employees = frappe.get_all(
        "Employee",
        filters={"status": "Active"},
        fields=["name", "employee_name", "gender"]
    )

    context.title = _("Employee Directory")
    context.employees = employees
    return context
