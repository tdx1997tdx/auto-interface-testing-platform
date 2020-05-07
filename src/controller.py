# -*- coding: utf-8 -*-
from flask import Blueprint, json, request, jsonify
from init_db_and_models import Setting
from src.service import *
from src.util import *

c = Blueprint("c", __name__)


@c.route("/case/get_setting", methods=['GET'])
def get_setting():
    ret = get_setting_servcie()
    return jsonify(ret)


@c.route("/case/set_setting", methods=['POST'])
def set_setting():
    data = json.loads(request.get_data(as_text=True))
    ret = set_setting_servcie(data)
    return jsonify(ret)


@c.route("/case/get_case", methods=['GET'])
def get_case():
    ret = get_case_servcie()
    return jsonify(ret)


@c.route("/case/add_case", methods=['POST'])
def add_case():
    data = json.loads(request.get_data(as_text=True))
    ret = add_case_servcie(data)
    return jsonify(ret)


@c.route("/case/update_case", methods=['POST'])
def update_case():
    data = json.loads(request.get_data(as_text=True))
    ret = update_case_servcie(data)
    return jsonify(ret)


@c.route("/case/del_case", methods=['POST'])
def del_case():
    data = json.loads(request.get_data(as_text=True))
    ret = del_case_servcie(data)
    return jsonify(ret)


@c.route("/case/execute_case", methods=['GET'])
def execute_case():
    ret = execute_case_servcie()
    return jsonify(ret)


@c.route("/report/get_report", methods=['GET'])
def get_report():
    ret = get_report_servcie()
    return jsonify(ret)


@c.route("/report/check", methods=['GET'])
def check():
    id = request.args.get("id")
    ret = check_service(id)
    return ret


@c.route("/report/del_report", methods=['POST'])
def del_report():
    data = json.loads(request.get_data(as_text=True))
    ret = del_report_servcie(data)
    return jsonify(ret)
