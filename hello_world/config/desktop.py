from frappe import _

def get_data():
    return [
        {
            "module_name": "hello_world",
            "label": _("Employee Custom"),
            "color": "#2980b9",
            "icon": "octicon octicon-person",
            "type": "module",
            "description": "Custom Employee Utilities",
            "items": [
                {
                    "type": "doctype",
                    "name": "Student",
                    "label": _("Student")
                }
            ]
        }
    ]