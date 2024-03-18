from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.users import User
from data.parse_user import parser
from flask import jsonify
from werkzeug.security import check_password_hash, generate_password_hash


def set_password(password):
    return generate_password_hash(password)


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': {'id': user.id, 'surname': user.surname, 'name': user.name, 'age': user.age,
                                 'position': user.position, 'speciality': user.speciality, 'address': user.address,
                                 'email': user.email}})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        print(users)
        return jsonify({'user': [{'id': user.id, 'surname': user.surname, 'name': user.name, 'age': user.age,
                                  'position': user.position, 'speciality': user.speciality, 'address': user.address,
                                  'email': user.email} for user in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=set_password(args['hashed_password'])

        )
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
