# Django-rail-api
This is an api which can answer train related queries of a user.

API Link
========
```
http://ec2-54-68-158-128.us-west-2.compute.amazonaws.com:8081/api/chat/
http://ec2-54-68-158-128.us-west-2.compute.amazonaws.com:8081/api/user/
 ```
Installation
============
```
To run this project follow:

  *Open Git bash and run following command:*

$ git clone https://github.com/sidhant47/Django-rail-api
  ```

Setup Environment Variables
============
```
$ export GOOGLE_APPLICATION_CREDENTIALS="<path of dialog flow cred>"
$ export RAIL_API_KEY="<rail api>"
$ export PROJECT_ID="<dialog-flow-project-id>"
  ```
```  
$ python3 manage.py makemigrations
$ python3 manage.py runserver 127.0.0.1:8080  
```
Project Requirements
==============
```
*Python (3.6)
*Django
```
Contact
=======
* sidhant47@gmail.com


