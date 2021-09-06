# Users - RBAC - Testin
The Staffer API grants uses RBAC to deletegate the following roles and their permissions:

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
