from flask import abort, Blueprint, request
from flask_restful import Api
from flask_jwt_extended import *
from sqlalchemy.exc import IntegrityError
from ..model import User
from ..view import BaseResource, json_required

api = Api(Blueprint(__name__, 'account_api'))


@api.resource('/auth')
class AuthService(BaseResource):
    @json_required({'id': str, 'password': str})
    def post(self):
        payload = request.json
        user = User.find_by_id(payload['id'])

        if not (user and payload['password'] == user.password):
            return abort(401)

        return self.unicode_json_response({
            'access_token': create_access_token(identity=user.id),
            'refresh_token': create_refresh_token(identity=user.id),
        })


@api.resource('/register')
class RegisterService(BaseResource):
    @json_required({'id': str, 'password': str, 'name': str})
    def post(self):
        payload = request.json

        user = User(id=payload['id'],
                    name=payload['name'],
                    password=payload['password'])

        try:
            user.save()

        except IntegrityError:
            return abort(409)

        return self.unicode_json_response({
            'access_token': create_access_token(identity=user.id),
            'refresh_token': create_refresh_token(identity=user.id)
        }, 201)


@api.resource('/refresh')
class RefreshService(BaseResource):
    @jwt_refresh_token_required
    def post(self):
        return {
            'access_token': create_access_token(identity=get_jwt_identity()),
        }
