from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@mysql:3306/admin'
db = SQLAlchemy(app)

## Create Route
@app.route('/')
def hello_world():
    return 'Hello, From Flask!'

if __name__== '__main__':
      app.run(host='0.0.0.0',debug=True)