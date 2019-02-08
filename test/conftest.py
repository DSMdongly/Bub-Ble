from app import create_app
from config import TestConfig
import pytest


@pytest.fixture(scope='session')
def test_client():
    app = create_app(TestConfig)

    with app.app_context():
        test_client = app.test_client()
        yield test_client

    with app.app_context():
        from app import db
        db.drop_all()


