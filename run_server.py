from app import create_app
from config import ProdConfig

if __name__ == '__main__':
    app = create_app(ProdConfig)
    app.run(port=app.config['PORT'],
            debug=app.config['DEBUG'],
            threaded=True)

