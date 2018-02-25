from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    students=[
        {'id':1, 'name':'Qasim'},
        {'id':2, 'name': 'Zeeshan hanif', 'education':'PHD'}
    ]
    return jsonify({'SaylaniStudents': students})

app.run(debug=True)