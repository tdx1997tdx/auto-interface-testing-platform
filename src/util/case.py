# -*- coding: utf-8 -*-
# case模块，封装case的bean，以及case容器
from src.util.json_compare import *
import json


class TestCase(dict):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.ret_code = None  # 返回的状态码
        self.ret_result = None  # 返回的结果
        self.judge = None

    def set_ret(self, ret_code, ret_result):
        """设置返回状态码以及结果"""
        self.ret_code = ret_code
        self.ret_result = ret_result

    def is_case_succeed(self):
        """判断用例是否成功"""
        if self.level == 1:
            if self.expect_code != self.ret_code:
                self.judge = (0, '状态码不正确')
                return
            if not self.is_case_match():
                self.judge = (1, '返回结果不正确')
                return
            self.judge = (2, '结果正确')
        elif self.level == 0:
            if self.expect_code != self.ret_code:
                self.judge = (0, '状态码不正确')
                return
            self.judge = (2, '结果正确')

    def is_case_match(self):
        """判断用例是否与预期一致"""
        return json_contain(self.expect_result, self.ret_result, True)

    def to_json(self):
        self.headers = json.loads(self.headers)
        self.data = json.loads(self.data)
        self.expect_return = json.loads(self.expect_return)

    def __str__(self):
        return str(self.__dict__)

    def __getattr__(self, key):
        value = self[key]
        if isinstance(value, dict):
            value = TestCase(value)
        return value


class CaseContainer:
    def __init__(self):
        self.container = []
        self.success_case_num = 0
        self.fail_case_num = 0
        self.total_case_num = 0

    def add_testcase(self, testcase):
        """添加用例"""
        if testcase.is_exe.lower() == 'yes':
            self.container.append(testcase)

    def sort_container(self):
        """根据id进行排序"""
        self.container.sort(key=lambda x: x.id, reverse=False)

    def calculate(self):
        """统计个数"""
        self.success_case_num = 0
        for i in self.container:
            if i.judge[0] == 2:
                self.success_case_num += 1
        self.total_case_num = len(self.container)
        self.fail_case_num = self.total_case_num - self.success_case_num

    def __iter__(self):
        for i in self.container:
            yield i
