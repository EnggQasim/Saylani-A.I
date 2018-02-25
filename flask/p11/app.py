from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'miti'
app.config['MONGO_URI'] = 'mongodb://qasim:qasim@ds143030.mlab.com:43030/miti'

mongo = PyMongo(app)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        usearch=request.form['user']
        students=[]
        records = mongo.db.users.find({'user': usearch})
        for user in records:
            students.append({'user': user['user'],\
            'password': user['pass']})
        return jsonify({'SearchData': students})
    else:
        return '''
        <form method="post">
        <h2>Search</h2>
        <input type="text" name="user">
        <input type="submit" value="search">
        </form>
    '''

app.run(debug=True)