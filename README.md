# 28-days-of-flask

Chapter 1: Beginning with Flask

Chapter 2: Database Modeling in Flask

Chapter 3: CRUD Application with Flask (Part 1)

Chapter 4: CRUD Application with Flask (Part 2)

Chapter 5: Testing in Flask

Chapter 6: Deploying Flask Applications

Chapter 7: Monitoring Flask 

# Flask Setup

```
python3 -m venv env
source env/bin/activate
pip3 install flask
pip3 freeze > requirements.txt 
```

## Docker 

docker-compose up -d --build


## Rest API

| Verb        |  CRUD       |   Operation     |   Safe   |   Idempotent   |
| :---        |    :----:   |          ---:   |  :----:  |      :----:    |   
| GET         | -           | -               |    YES   |                |
| POST        | -           | -               |    NO    |                |
| PUT         | -           | -               |    NO    |                |
| DELETE      | -           | -               |          |                |
| OPTIONS     | -           | -               |          |                |


## MYSQL SETUP

pip install flask-sqlalchemy pymysql


### 2.1 Mysql : Creating an Author Database

We’ll now create an author database application which will provide RESTfulCRUDAPIs.Alltheauthorswillbestoredinatabletitled“authors”.
After the declared db object, add the following lines of code to declare a class as Authors which will hold the schema for the author table:

```
class Author (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))
    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
    def __repr__(self):
      return '<Product %d>' % self.id
db.create_all()
```
# Issues 
1. mysql wait is not added