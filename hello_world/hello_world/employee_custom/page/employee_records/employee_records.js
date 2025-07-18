frappe.pages['employee-records'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Employee Records',
        single_column: true
    });

    frappe.call({
        method: 'hello_world.employee_custom.employee_custom.page.employee_records.employee_records.get_employees',
        callback: function(r) {
            const data = r.message;
            let html = `
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Department</th>
                            <th>Designation</th>
                            <th>Gender</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${data.map(emp => `
                            <tr>
                                <td>${emp.name}</td>
                                <td>${emp.employee_name}</td>
                                <td>${emp.department}</td>
                                <td>${emp.designation}</td>
                                <td>${emp.gender}</td>
                            </tr>`).join('')}
                    </tbody>
                </table>
            `;
            $(page.body).html(html);
        }
    });
};
