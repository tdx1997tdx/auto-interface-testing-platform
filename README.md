# 自动化接口测试平台

## 安装依赖

```sh
pip3 install flask flask-sqlalchemy flask-migrate flask-script mysql-connector-python flask-socketio requests logbook
```

## 使用方法

1. 安装mysql数据库
2. 创建名叫testing_system的数据库
3. setting.py设置连接mysql数据库的参数
4. 输入以下命令拉下代码

```sh
git clone https://github.com/tdx1997tdx/auto-interface-testing-platform.git
```

5. 输入以下命令迁移更新数据库

```sh
python3 manage.py db migrate
python3 manage.py db upgrade
python3 manage.py dbinit
```

6. 打开应用

```sh
nohup python3 manage.py runserver 0.0.0.0:5000 &
```

7. 访问 http://ip:5000就可以用了