from flask import Flask, render_template
from database import db
from flask_migrate import Migrate
from usuarios import bp_usuarios
from models import Comments

app = Flask(__name__)

conexao = 'sqlite:///teste.sqlite3'

app.config['SECRET_KEY'] = 'sisahujsagbgbsabhjfhsafh'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///teste.sqlite3"
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
    comments = Comments.query.all()
    return render_template('about.html', comments=comments)

@app.route('/prevention')
def prevention():
    return render_template('prevention.html')

@app.route('/causes')
def causes():
    return render_template('causes.html')

@app.route('/types')
def types():
    return render_template('types.html')

@app.route('/treatment')
def treatment():
    return render_template('treatment.html')

if __name__ == '__main__':
    app.run(port=5151)
