from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World \
    Pakistan zinda bad \
    we are pakistani \
    <h1>Saylani Students code</h1>\
    "
@app.route("/about")
def about():
    return '''
    <h1>About Page</h1>
    Hello World 
    Pakistan zinda bad 
    we are pakistani 
    <h1>Saylani Students code</h1>
    '''

app.run(debug=True)