# Halo API/Flask App Project 

Halo code test

# Getting Started

The following instructions will cover useful information to start the Halo Flask Application

# Creating Virtual Environment
create a virtual envirionment using virtualenv

* To install virtualenv use:
```shell
pip install virtualenv venv
```

* To start virtualenv:
- (Windows)
```shell
foo\bar\venv\Scripts\activate
```
-(Mac)
```shell
source venv/bin/activate
```

### Next steps:
- Navigate to working directory
- run ```pip install -r requirements.txt```
* To run the project
- run ```python app.py```

# Testing
In terms of testing the API:
* I have written tests to cover most of the applications login/logout functions. Because of time, I was unable to create full tests for checking if a user has permission to view specific data (This functionality is however working in app).

## To run the testing file:
---
- Run ```shell
python test.py -v```
### Further Documentation regarding endpoints

| EndPoint        | Description | 
| ------------- |:-------------:| 
| /login      | Sign in as a signed up user |
| /logout       | Logout User  |
| /signup       | Sign up as new user  |
| /dashboard| Add a new post as a logged in user     |
| /posts        | Display your posts   | 
| /index        | Landing Page - Login Default     |
