from init_db_and_models import *
from src.util.dict_and_obj import *
from src.util.case import *
from src.util.execute_case import *
from src.util.report import GReport
import json, time


def get_setting_servcie():
    setting = Setting.query.all()[0]
    return orm_to_dict(setting)


def set_setting_servcie(data):
    data['based_headers'] = json.dumps(data['based_headers'])
    q_setting = Setting.query.filter(Setting.id == 1).update(data)
    db.session.commit()
    return {'code': q_setting}


def get_case_servcie():
    case = Case.query.all()
    ret = []
    for i in case:
        ret.append(orm_to_dict(i))
    return ret


def add_case_servcie(data):
    case = Case()
    dict_to_orm(case, data)
    case.headers = json.dumps(case.headers)
    case.data = json.dumps(case.data)
    case.expect_return = json.dumps(case.expect_return)
    db.session.add(case)
    db.session.commit()
    return {'code': 1}


def update_case_servcie(data):
    data['headers'] = json.dumps(data['headers'])
    data['data'] = json.dumps(data['data'])
    data['expect_return'] = json.dumps(data['expect_return'])
    ret = Case.query.filter(Case.id == data.get('id')).update(data)
    db.session.commit()
    return {'code': ret}


def del_case_servcie(data):
    id = data.get('id')
    result = Case.query.filter(Case.id == id).first()
    db.session.delete(result)
    db.session.commit()
    return {'code': 1}


def execute_case_servcie():
    start = time.time()
    case = Case.query.all()
    case_container = CaseContainer()
    for i in case:
        case = TestCase(orm_to_dict(i))
        case.to_json()
        case_container.add_testcase(case)
    execute(case_container)
    g_report = GReport(case_container)
    g_report.set_time(start, time.time())
    html_stearm = g_report.get_report_html()
    report = Report(name='%s-report' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))),
                    content=html_stearm)
    db.session.add(report)
    db.session.commit()
    return {'code': 1}


def get_report_servcie():
    report = Report.query.all()
    ret = []
    for i in report:
        dict_map = orm_to_dict(i)
        del dict_map['content']
        ret.append(dict_map)
    return ret


def check_service(id):
    result = Report.query.filter(Report.id == id).first()
    return result.content


def del_report_servcie(data):
    id = data.get('id')
    print(id)
    result = Report.query.filter(Report.id == id).first()
    db.session.delete(result)
    db.session.commit()
    return {'code': 1}
