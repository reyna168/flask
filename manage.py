# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:49:06 2020

@author: reyna
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)

# 初始化 migrate
# 两个参数一个是 Flask 的 app，一个是数据库 db
migrate = Migrate(app, db)

# 初始化管理器
manager = Manager(app)
# 添加 db 命令，并与 MigrateCommand 绑定
manager.add_command('db', MigrateCommand)

# 构建我们的数据模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()