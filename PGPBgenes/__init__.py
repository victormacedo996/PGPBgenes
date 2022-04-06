from flask import Flask
from PGPBgenes.config import Config
from PGPBgenes.blast import filters

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from PGPBgenes.main.routes import main
    from PGPBgenes.blast.routes import blast
    app.register_blueprint(main)
    app.register_blueprint(blast)

    return app
