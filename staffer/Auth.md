# Users - RBAC - Testing
The Staffer API grants uses RBAC to delegate the following roles and their permissions:

## Roles

----

#### &nbsp;&nbsp;  **HR Manager**
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

#### &nbsp;&nbsp;  **Project Manager**
This role allows read, create and edit project records (no delete permission).
No access to employee record
### Permissions
* get:project
* patch:project
* post:project

##### User: email2@email.com
&nbsp;


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

&nbsp;

## Heroku - Testing Deployed API

The [`Postman Collection`](../Staffer.postman_collection.json) contains all the tests against the [`deployed APi`](https://staffer-udacity.herokuapp.com/)

&nbsp;

### API Calls with the HR Manager Token
----
&nbsp;
#### &nbsp;&nbsp;  **GET Tests**

1. home - no authentication needed
2. all projects - no authentication needed
3. all employees - no authentication needed
4. Employee Details - __get:employee__ permission needed
5. Poroject Details - __get:project__ permission needed

&nbsp;
#### &nbsp;&nbsp;  **POST Tests**

1. Create Employee - __post:employee__ permission needed
5. Create Project - __post:project__ permission needed

&nbsp;

#### &nbsp;&nbsp;  **DELETE  Tests**

1. Delete Employee - __delete:employee__ permission needed
5. Delete Project - __delete:project__ permission needed

&nbsp;

#### &nbsp;&nbsp;  **PATCH Tests**

1. Edit Employee - __delete:employee__ permission needed
5. Edit Project - __delete:project__ permission needed

&nbsp;

The HR Manager role has access to all resources.

All calls include a test of response code.

```js script
pm.test("Status & Success", function () {
    const responseJson = pm.response.json(); 
    pm.response.to.have.status(200);
    pm.expect(responseJson.success).to.eql(true);
});
```
And tests for response values and dictionary keys similar to:
```js script
pm.test("Employee Dictionary", () => {
  const project = pm.response.json(); 
  pm.expect(project).to.have.all.keys('advisor_id', 'director_id' , 'id', 'success', 'name', 'manager_id', 'tag');
  pm.expect(project['id']).to.be.a("number");
  pm.expect(project['name']).to.be.equal('test 011');
  pm.expect(project['tag']).to.be.equal(1001);
});
```

&nbsp;
### API Calls with the Project Manager Token
---

#### &nbsp;&nbsp;  **GET Tests**

1. Employee Details - __get:employee__ permission needed - not present
2. Poroject Details - __get:project__ permission needed - not present

&nbsp;
#### &nbsp;&nbsp;  **POST Tests**

1. Create Employee - __post:employee__ permission needed - not present
5. Create Project - __post:project__ permission needed

&nbsp;

#### &nbsp;&nbsp;  **DELETE  Tests**

1. Delete Employee - __delete:employee__ permission needed - not present


&nbsp;

#### &nbsp;&nbsp;  **PATCH Tests**

1. Edit Employee - __delete:employee__ permission needed  - not present
5. Edit Project - __delete:project__ permission needed

&nbsp;

For tests without the propper permission, we test for a 403 reponse code.

```js script
pm.test("Status & Success", function () {
    const responseJson = pm.response.json(); 
    pm.response.to.have.status(403);
    pm.expect(responseJson.success).to.eql(false);
});
```