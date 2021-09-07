# Users - RBAC - Testing
The Staffer API grants uses RBAC to delegate the following roles and their permissions:

## Roles

----
&nbsp;

#### HR Manager
This role allows read, create, edit, and delete employee and project records.
### Permissions
* delete:employee	
* delete:project 
* get:employee 
* get:project 
* patch:employee
* patch:project
* post:employee
* post:project

##### User: email1@email.com
&nbsp;

#### Project Manager
This role allows read, create and edit project records (no delete permission).
No access to employee record
### Permissions
* get:project
* patch:project
* post:project

##### User: email2@email.com
&nbsp;

----

# Testing
Because some of the test depend on specific employee and project ids, make sure you have a new new data set before running the test file.  
Create the test tables and add the test data. 

```bash
psql postgres < starting_psql_tester.psql
```
Once the database is running, run the test file

```
python test_staffer.py
```

Ensure all tests run successfully.