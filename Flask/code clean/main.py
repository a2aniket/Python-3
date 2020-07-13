from flask import Flask,render_template,request
from flask_sqlalchemy import  SQLAlchemy
from flask_mail import Mail
import json

with open('config.json' , 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
local_server = True
app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_username'],
    MAIL_PASSWORD=  params['gmail_password']
)

mail = Mail(app)

local_server=True
if local_server :
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Conatct(db.Model):
    SrNo = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=False, nullable=False)
    Email = db.Column(db.String(120), unique=False, nullable=False)
    Phone = db.Column(db.Integer, unique=False, nullable=False)
    Message = db.Column(db.String(120), unique=False, nullable=False)


class Block(db.Model):
    SrNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    date = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(12), nullable=True)
    ##img_file = db.Column(db.String(12), nullable=True)


print(params)
@app.route("/")
def index():
    return  render_template("index.html",params=params)
@app.route("/contact",methods=["GET","POST"])
def contact():
    if(request.method=="POST"):
        name = request.form.get("Name")
        email = request.form.get("Email")
        phone = request.form.get("Phone")
        message = request.form.get("Message")

        mail.send_message('New message bloger ' + name,
                          sender=email,
                          recipients=[params['gmail_username']],
                          body=message + "\n" + phone
                          )

        entry = Conatct(Name=name, Email=email, Phone=phone,Message=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html",params=params)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post =Block.query.filter_by(slug=post_slug).first()
    return render_template("post.html", params=params,post=post)

app.run(debug=True)