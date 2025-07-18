import frappe

@frappe.whitelist()
def get_employees():
    return frappe.get_all(
        "Employee",
        filters={"status": "Active"},
        fields=["name", "employee_name", "department", "designation", "gender"]
    )