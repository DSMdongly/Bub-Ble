from test.factory.user import UserFactory
from app import db
from app.model import User
from config import TestConfig
import jwt


class TestAuthAPI:
    @classmethod
    def _call_auth_api(self, client, id, password):
        return client.post('/auth', json={
            'id': id,
            'password': password,
        })

    def test_normal(self, test_client):
        user = UserFactory.create()
        db.session.commit()

        resp = self._call_auth_api(
            test_client,
            user.id,
            user.password
        )

        assert resp.status_code == 200

        resp = resp.json

        access_token = resp.get('access_token')
        refresh_token = resp.get('refresh_token')

        assert access_token and refresh_token

        access_token_data = jwt.decode(
            refresh_token,
            TestConfig.SECRET_KEY,
            algorithms=['HS256']
        )

        refresh_token_data = jwt.decode(
            access_token,
            TestConfig.SECRET_KEY,
            algorithms=['HS256']
        )

        assert access_token_data['identity'] == user.id
        assert refresh_token_data['identity'] == user.id

    def test_invalid_account(self, test_client):
        resp = self._call_auth_api(
            test_client,
            'invalid',
            'invalid',
        )

        assert resp.status_code == 401


class TestRegisterAPI:
    @classmethod
    def _call_register_api(self, client, id, password, name):
        return client.post('/register', json={
            'id': id,
            'password': password,
            'name': name,
        })

    def test_normal(self, test_client):
        resp = self._call_register_api(
            test_client,
            'testid',
            'testpass',
            'testname',
        )

        assert resp.status_code == 201

        user = User.find_by_id('testid')

        assert user.password == 'testpass'
        assert user.name == 'testname'

    def test_duplicate_account(self, test_client):
        user = UserFactory.create()
        db.session.commit()

        resp = self._call_register_api(
            test_client,
            user.id,
            user.password,
            user.name,
        )

        assert resp.status_code == 409
