from frappe import _

def get_data():
    return [
        {
            "module_name": "Employee Custom",
            "label": _("Employee Custom"),
            "color": "#2980b9",
            "icon": "octicon octicon-person",
            "type": "module",
            "description": "Custom Employee Utilities",
            "items": [
                {
                    "type": "page",
                    "name": "employee_records",
                    "label": _("Employee Records")
                }
            ]
        }
    ]
