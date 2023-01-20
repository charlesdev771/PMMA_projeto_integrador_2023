from flask import Blueprint
from flask import render_template, request, redirect
from models import Usuario, Newsletter, Comments
from database import db

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')


@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('usuarios_create.html')

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        u = Usuario(nome, email, senha)
        db.session.add(u)
        db.session.commit()

        return 'dados :)'
    

@bp_usuarios.route('/newsletter', methods=['GET', 'POST'])
def newsletter():
    
    try:
    
        if request.method == 'POST':
            newsletter = request.form.get('newsletter')

            n = Newsletter(newsletter)
            db.session.add(n)
            db.session.commit()
            return redirect('http://127.0.0.1:5000')

    
    except Exception as error:
        
        print(error)





@bp_usuarios.route('/comments', methods=['GET', 'POST'])
def comments():
    
    try:
        
        if request.method == 'POST':
            name = request.form.get('my_name')
            email = request.form.get('email')
            comment = request.form.get('comment')
        
            c = Comments(name, email, comment)
            db.session.add(c)
            db.session.commit()

            return redirect('http://127.0.0.1:5000/about')
        
    except Exception as error:
        
        print(error)





@bp_usuarios.route('/recovery')
def recovery():
    usuarios = Usuario.query.all()
    return render_template('usuarios_recovery.html', usuarios=usuarios)


@bp_usuarios.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    u = Usuario.query.get(id)

    if request.method == 'GET':
        return render_template('usuarios_update.html', u=u)

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        u.nome = nome
        u.email = email
        db.session.add(u)
        db.session.commit()
        return redirect(
            'http://127.0.0.1:5000/usuarios/recovery')


@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    u = Usuario.query.get(id)
    if request.method == 'GET':
        return render_template('usuarios_delete.html', u=u)

    if request.method == 'POST':
        db.session.delete(u)
        db.session.commit()
        return redirect(
            'http://127.0.0.1:5000/usuarios/recovery')
