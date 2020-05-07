# 自动化接口测试平台

## 安装依赖

```sh
pip install flask Flask-SQLAlchemy Flask-Migrate Flask-Script mysql-connector-python Flask-Socketio
```

## 使用方法

1. 安装mysql数据库
2. setting.py设置连接mysql数据库的参数
3. 输入以下命令迁移更新数据库

```sh
python manager.py db migrate
python manager.py db upgrade
python manager.py dbinit
```

4. 打开应用

```sh
nohup python manager.py runserver &
```

5. 访问 http://ip:5000就可以用了