from database import db


class Usuario(db.Model):
  __tablename__='user'
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  email = db.Column(db.String(100))
  senha = db.Column(db.String(100))

  def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.senha = senha
    
    
    
class Newsletter(db.Model):
  __tablename__='newsletter'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100))

  def __init__(self, email):
    self.email = email
    
    
class Comments(db.Model):
  __tablename__='comments'
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  email = db.Column(db.String(100))
  comment = db.Column(db.String(300))

  def __init__(self, nome, email, comment):
    self.nome = nome
    self.email = email
    self.comment = comment
  
