from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from flask import Flask, request, jsonify, make_response


app = Flask(__name__)
# Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@mysql:3306/admin'
db = SQLAlchemy(app)

###  Database Model  ###
class Team (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    role = db.Column(db.String(50))
    experience = db.Column(db.Integer)
    
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    
    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience

    def __repr__(self):
      return '<Product %d>' % self.id

db.create_all()

###  Database Schema  ###
class TeamSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Team
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    role = fields.String(required=True)
    experience = fields.Number(required=True)

###  POST - Create Team  ###
@app.route('/team', methods = ['POST'])
def add_team_members():
    data = request.get_json()
    team_schema = TeamSchema()
    team = team_schema.load(data)
    result = team_schema.dump(team.create()).data
    return make_response(jsonify({"members": team}),201)

###  GET Team Members  ###
@app.route('/team', methods = ['GET'])
def index():
    get_members = Team.query.all()
    team_schema = TeamSchema(many=True)
    team_members = team_schema.dump(get_members)
    return make_response(jsonify({"Members": team_members}))


###  GET Team Members  ###
#@app.route('/', methods = ['GET'])
#    return "hello Flask!!!"

if __name__== '__main__':
      app.run(host='0.0.0.0')