from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME']='miti'
app.config['MONGO_URI']='mongodb://qasim:qasim@ds143030.mlab.com:43030/miti'
mongo = PyMongo(app)


@app.route("/")
def index():
    students=[]
    records = mongo.db.users.find({'user':'qasim'})
    for user in records:
        students.append({'name': user['user'], \
        'password': user['pass']})

    
    return jsonify({'SaylaniStudents': students})

@app.route("/add")
def add():
    add = mongo.db.students.insert({'name':'kashan'})
    return "Successfully add"

app.run(debug=True)