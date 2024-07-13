from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Crear una aplicación Flask
app = Flask(__name__)

# Configurar la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

# Crear la base de datos
with app.app_context():
    db.create_all()

# Ruta para agregar usuarios
@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    data = request.get_json()
    nombre = data['nombre']
    password = data['password']
    password_hash = generate_password_hash(password)

    nuevo_usuario = Usuario(nombre=nombre, password_hash=password_hash)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario agregado exitosamente"})

# Ruta para validar usuarios
@app.route('/validar_usuario', methods=['POST'])
def validar_usuario():
    data = request.get_json()
    nombre = data['nombre']
    password = data['password']

    usuario = Usuario.query.filter_by(nombre=nombre).first()

    if usuario and check_password_hash(usuario.password_hash, password):
        return jsonify({"mensaje": "Validación exitosa"})
    else:
        return jsonify({"mensaje": "Nombre o contraseña incorrecta"}), 401

if __name__ == '__main__':
    app.run(port=7500)
