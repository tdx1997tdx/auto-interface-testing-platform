# -*- coding: utf-8 -*-
# 执行每个用例
from src.util.do_requests import send_requests
from src.util.log import LOG

def execute(container,setting):
    LOG.info("用例执行中")
    for i in container:

        ret_code, ret_result = send_requests(i.url, i.method, i.data, i.headers.update(setting['based_headers']))
        i.set_ret(ret_code, ret_result)
        i.is_case_succeed()
        LOG.info("用例%d执行完毕" % (i.id))
    container.calculate()
    LOG.info("所有用例执行完毕")
