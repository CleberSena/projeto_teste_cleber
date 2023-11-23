from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 1º Criar um API flask:
app = Flask(__name__)

# 2º Criar uma instãncia de SQLAlchemy:
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:8nb11tWgzJvoMI3q@db.zfsowaqmpndmaydisquj.supabase.co:5432/postgres'

db = SQLAlchemy(app)
db:SQLAlchemy

# 3º Definir a Estrutura da Tabela Postagem:
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# 4º Definir a Estrutura da Tabela Autor:
class Autor(db.Model) :
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

# 5º Executar o Comando para Criar o Banco de Dados:
def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()
        # Criar Administradores:
        autor = Autor(nome = 'none', email = 'none', senha = 'none', admin = True)
        db.session.add(autor)
        db.session.commit()

if __name__ == '__main__':
    inicializar_banco()