# Django-rail-api
This is an api which can answer train related queries of a user.

API Enpoints
========

## User
http://ec2-54-68-158-128.us-west-2.compute.amazonaws.com:8081/api/user/

Method: *POST*

```
{
	"first_name": "hello",
	"last_name": "world",
	"email": "hello@hello.com"
}
```
---

## Chat

http://ec2-54-68-158-128.us-west-2.compute.amazonaws.com:8081/api/chat/

Method: *POST*

```
{
	"message": "find trains",
	"user": "/api/user/fcaf31d6-937f-42fc-b562-83b5fe6ab21b/"
}
```

Installation
============

To run this project follow:

```
$ git clone https://github.com/sidhant47/Django-rail-api

$ cd Django-rail-api

```

Setup Environment Variables
============
```
$ export GOOGLE_APPLICATION_CREDENTIALS="<path of dialog flow creds json>"
$ export RAIL_API_KEY="<rail api>"
$ export PROJECT_ID="<dialog flow project_id>"
```

```  
$ python3 manage.py makemigrations
$ python3 manage.pt migrate
$ python3 manage.py runserver  
```
Project Requirements
==============

* Python (3.6)

* Django

Contact
=======
* sidhant47@gmail.com

