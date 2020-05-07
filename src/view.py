# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import redirect,url_for
v = Blueprint("v", __name__, template_folder='templates', static_folder='static', static_url_path='/static')


@v.route("/case.html")
def case_view():
    return v.send_static_file('case.html')


@v.route("/report.html")
def report_view():
    return v.send_static_file('report.html')


@v.route("/")
def main_view():
    return redirect(url_for('v.case_view'),code=302)
