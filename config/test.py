from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_DATABASE_URI = (
        'postgres://localhost:5432/poem_test?user=postgres&password=ehdgus0608'
    )
