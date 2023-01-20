from flask import Flask, render_template
from database import db
from flask_migrate import Migrate
from usuarios import bp_usuarios

app = Flask(__name__)

conexao = 'sqlite:///meubanco.sqlite'

app.config['SECRET_KEY'] = 'chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')

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
    app.run(host='0.0.0.0', port=81)
