"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Developer, Company, Candidate, Project, Offer
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required
from flask_bcrypt import generate_password_hash, check_password_hash  
import stripe


api = Blueprint('api', __name__)
stripe.api_key = 'sk_test_51PsqIxG3cEcyZuNprPRA1UTti31vG7fgiVVBfefTiZ61KUnQpESthKWS5oV9QFWCQoVsWzLbAJLmGP7npT9Wejth00qZpNlIhY'


# Allow CORS requests to this API
CORS(api)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200


@api.route('/signup', methods=['POST'])
def signup_user():
    # Campos del body
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    name = request.json.get('name', None)
    last_name = request.json.get('last_name', None)
    telephone = request.json.get('telephone', None)
    country = request.json.get('country', None)

    # Validar que todos los campos requeridos no estén vacíos
    if not email or not password or not name or not last_name:
        return jsonify({'success': False, 'msg': 'Todos los campos son obligatorios'}), 400
    
    #Verificar que si el email existe
    email_exist = User.query.filter_by(email=email).first()
    if email_exist:
        return jsonify({'success': False, 'msg':'Ya existe una cuenta registrada con el email '+ email}),400

    # Verificar si el usuario ya existe
    user_exist = User.query.filter_by(email=email).first()
    if user_exist:
        return jsonify({'success': False, 'msg': 'Este usuario ya está registrado'}), 400

    # Encriptar la contraseña antes de guardarla
    hashed_password = generate_password_hash(password).decode('utf-8')
    
    # Crear un nuevo usuario con todos los campos
    new_user = User(
        email=email,
        password=hashed_password,
        name=name,
        last_name=last_name,
        telephone=telephone,
        country=country,
        is_active=True
    )

    # Agregar a la base de datos
    db.session.add(new_user)
    db.session.commit()

    # Crear un token de acceso
    access_token = create_access_token(identity=new_user.id)

    return jsonify({
        'success': True,
        'msg': 'Ha sido registrado correctamente',
        'token': access_token,
        'user': new_user.serialize()  
    }), 200



@api.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify({'success': False, 'msg': 'Por favor, proporciona correo y contraseña.'}), 400

        user = User.query.filter_by(email=email).first()

        # Verificar la contraseña encriptada
        if not user or not check_password_hash(user.password, password):
            return jsonify({'success': False, 'msg': 'Usuario o contraseña incorrectos.'}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify({
            'success': True,
            'msg': 'Inicio de sesión exitoso.',
            'token': access_token,
            'user': user.serialize()
        }), 200
    
    except Exception as e:
        print(f"Error en login: {str(e)}")  
        return jsonify({'success': False, 'msg': 'Ocurrió un error interno, por favor intenta de nuevo.'}), 500

# @api.route('/private', methods=['GET'])
# @jwt_required()
# def page_private():
#     user_id = get_jwt_identity()
#     user = User.query.get(user_id)

#     if user:
#         return jsonify({'success': True, 'msg': 'Has logrado entrar a una página privada'}), 200
#     return jsonify({'success': False, 'msg': 'No estás logeado'}), 400

@api.route('/token', methods=['GET'])
@jwt_required()
def token():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user:
        return jsonify({
            "id": user.id,
            "email": user.email,
            "is_active": user.is_active
        }), 200
    else:
        return jsonify({"msg": "Usuario no encontrado"}), 404
