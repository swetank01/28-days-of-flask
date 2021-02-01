from flask import Flask
app = Flask(__name__)

## Create Route
@app.route('/')
def hello_world():
    return 'Hello, From Flask!'

if __name__== '__main__':
      app.run(host='0.0.0.0')