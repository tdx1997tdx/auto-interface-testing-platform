# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class Case(db.Model):
    __tablename__ = 'case'
    id = db.Column(db.INTEGER, primary_key=True,autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    url = db.Column(db.String(80), nullable=True)
    is_exe = db.Column(db.Enum('yes', 'no'))
    method = db.Column(db.Enum('get', 'post'))
    headers = db.Column(db.String(200))
    data = db.Column(db.String(500))
    expect_code = db.Column(db.Integer)
    expect_return = db.Column(db.String(500))
    level = db.Column(db.INTEGER)


class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    content = db.Column(db.TEXT(300000))
    create_time = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Setting(db.Model):
    __tablename__ = 'setting'
    id = db.Column(db.INTEGER, primary_key=True)
    based_url = db.Column(db.String(80))
    based_headers = db.Column(db.String(500))
    cookie = db.Column(db.String(80))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.INTEGER)
