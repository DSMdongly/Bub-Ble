import factory
from factory.alchemy import SQLAlchemyModelFactory
from app.model.user import User
from app import db


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    id = factory.sequence(lambda n: 'user{0}'.format(n + 1))
    name = factory.sequence(lambda n: 'user {0}'.format(n + 1))
    password = 'test1234'

