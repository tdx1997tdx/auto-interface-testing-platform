# -*- coding: utf-8 -*-
from init_db_and_models import *
from flask import Flask
from flask_socketio import SocketIO
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import json

from src.view import v
from src.controller import c


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v)
    app.register_blueprint(c)
    app.config.from_object('settings')
    db.init_app(app)
    # 必须绑定app和db
    Migrate(app, db)
    return app


def create_manager(app):
    manager = Manager(app)
    # 把MigrateCommand命令添加到manager中
    manager.add_command('db', MigrateCommand)
    return manager


app = create_app()
socketio = SocketIO(app, async_mode=None)
manager = create_manager(app)


@manager.command
def dbinit():
    db.drop_all()
    db.create_all()
    based_headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36",
        "Authorization": "user_id=11;token=dbe5c4ec-ae0a-4a38-85fe-59b91be45bd5",
        "Content-Type": "application/json"
    }
    s = Setting(id=1, based_url='http://39.99.172.71:8080', based_headers=json.dumps(based_headers),
                cookie='user_id=11;token=dbe5c4ec-ae0a-4a38-85fe-59b91be45bd5', username='tom2',
                password='123', role=1)
    data = {
        "username": "tom",
        "password": "123",
        "role": "1"
    }
    expect_return = {
        "state": "1",
        "message": "登陆成功"
    }
    c = Case(id=1, name='登陆测试', url='http://39.99.172.71:8080/user/login', is_exe='yes', method='post',
             headers='{}',
             data=json.dumps(data), expect_code=200, expect_return=json.dumps(expect_return), level=1)
    db.session.add(s)
    db.session.add(c)
    db.session.commit()


# @manager.command
# def run():
#     socketio.run(app, host='127.0.0.1', port=5000, use_reloader=False)
#
#
# @socketio.on('message', namespace="/test")
# def handle_message(message):
#     print('received message: ' + message['data'])
#     socketio.emit("response", {'age': 18}, namespace="/test")
#
#
# @socketio.on('connect', namespace="/test")
# def connect():
#     print("connect..")
#
#
# @socketio.on('disconnect', namespace="/test")
# def connect():
#     print("disconnect...")
