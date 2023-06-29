from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'festus asiyanbi'

    from .views import views
    from .auth import auths

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auths, url_prefix="/")
    return app