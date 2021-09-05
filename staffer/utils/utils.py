

# takes a sqlalchemy query results and jsonifies it
def process_employee_results(sql_employees):
    employees =[]
    for emp in sql_employees:
        emp_dict = {}
        emp_dict['id'] = emp.id
        emp_dict['username'] = emp.username
        emp_dict['department'] = emp.department

        employees.append(emp_dict)

    return employees

# takes a sqlalchemy query results and jsonifies it
def process_project_results(sql_projects):
    projects =[]
    for proj in sql_projects:
        proj_dict = {}
        proj_dict['id'] = proj.id
        proj_dict['name'] = proj.name
        proj_dict['tag'] = proj.tag
        proj_dict['advisor_id'] = proj.advisor_id
        proj_dict['manager_id'] = proj.manager_id
        projects.append(proj_dict)

    return projects

