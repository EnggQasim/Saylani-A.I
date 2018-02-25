from flask import Flask,\
render_template, url_for, \
redirect, request, session, redirect, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'miti'
app.config['MONGO_URI'] = 'mongodb://admin:admin@ds143030.mlab.com:43030/miti'

mongo = PyMongo(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add", methods=['GET','POST'])
def add():
    check=False
    if request.method == 'POST':
        dataInsert = mongo.db.users
        dataInsert.insert({'user': request.form['user'], 'pass': request.form['pass']})
        check=True
    return render_template("add.html", ok=check)


@app.route("/signin", methods=['GET','POST'])
def signin():
    check=False    
    if request.method=='POST':
        checkUser=mongo.db.users
        watchMan=checkUser.find({'user': request.form['user'] , 'pass': request.form['pass']})
        for i in watchMan:
            if i['user']==request.form['user'] and i['pass']==request.form['pass'] :
                check=True
                session['username']=request.form['user']
                break

    return render_template("signin.html", ok=check)

@app.route("/logout")
def logout():
    session.pop('username',None)
    session.pop('username', None)
    return redirect(url_for('index'))
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'





@app.route("/API")
def api():
    dbAllData=mongo.db.users.find()
    allUsers=[]
    for user in dbAllData:
        allUsers.append({'user': user['user']})

    return jsonify({"Users": allUsers})


if __name__=="__main__":
    app.run(debug=True)
