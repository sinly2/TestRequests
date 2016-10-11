from flask import *
from flask_sqlalchemy import SQLAlchemy
# from flask_apscheduler import APScheduler
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# def job1():
#     print '666666666'
#     print '333'
# class Config(object):
#     JOBS = [{'id':'job1','func':job1,'trigger':'interval','seconds':500000}]
#     SCHEDULER_EXECUTORS = {'default': {'type': 'threadpool', 'max_workers': 1}}
#     SCHEDULER_JOB_DEFAULTS = {
#         'coalesce': False,
#         'max_instances': 1
#     }

db = SQLAlchemy()
# scheduler = APScheduler()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
def create_app():
    app = Flask(__name__)

    from .main import main as main__blueprint
    from .auth import auth as auth__blueprint
    app.config['SECRET_KEY'] = 'hehe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#     app.config.from_object(Config())
    app.register_blueprint(main__blueprint)
    app.register_blueprint(auth__blueprint,url_prefix='/auth')
    db.init_app(app)
#     scheduler.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
#     scheduler.start()
    return app


