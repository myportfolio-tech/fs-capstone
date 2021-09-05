from flask import jsonify

# takes a sqlalchemy query results and jsonifies it
def json_employees_results(sql_employees):
    employees =[]
    for emp in sql_employees:
        emp_dict = {}
        emp_dict['id'] = emp.id
        emp_dict['username'] = emp.username
        emp_dict['department'] = emp.department
        emp_dict['email'] = emp.email

        employees.append(emp_dict)

    return jsonify({
        'success': True,
        'employees': employees,
        'total': len(employees)
    })


def json_employee(sql_employee):
        
        return jsonify({
        'success': True,
        'id': sql_employee.id,
        'username': sql_employee.username,
        'email': sql_employee.email,
        'department': sql_employee.department
    })


# takes a sqlalchemy query results and jsonifies it
def json_projects_results(sql_projects):
    projects =[]
    for proj in sql_projects:
        proj_dict = {}
        proj_dict['id'] = proj.id
        proj_dict['name'] = proj.name
        proj_dict['tag'] = proj.tag
        proj_dict['advisor_id'] = proj.advisor_id
        proj_dict['manager_id'] = proj.manager_id
        projects.append(proj_dict)

    return jsonify({
        'success': True,
        'projects': projects,
        'total': len(projects)
    })


def json_project(sql_project):
        
        return jsonify({
        'success': True,
        'id': sql_project.id,
        'name': sql_project.name,
        'tag': sql_project.tag,
        'advisor_id': sql_project.advisor_id,
        'manager_id': sql_project.manager_id,
        'director_id': sql_project.director_id
    })