from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from flask import Flask, request, jsonify, make_response


app = Flask(__name__)
# Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@mysql:3306/admin'
db = SQLAlchemy(app)

## Create Route
@app.route('/')
def hello_world():
    return 'Hello, From Flask!'

class Authors (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))
    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
    def __repr__(self):
      return '<Product %d>' % self.id

db.create_all()

class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Authors
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialisation = fields.String(required=True)

@app.route('/authors', methods = ['GET'])
def index():
    get_authors = Authors.query.all()
    author_schema = AuthorSchema(many=True)
    authors = author_schema.dump(get_authors)
    return make_response(jsonify({"authors": authors}))

if __name__== '__main__':
      app.run(host='0.0.0.0')