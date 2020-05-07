# -*- coding: utf-8 -*-
# 比较一个json是否包含另一个json

class JsonPathValue(object):
    def __init__(self, datadict):
        self.stack = []
        self.final_dict = {}
        self.do_walk(datadict)

    def get_dict(self):
        return self.final_dict

    def do_walk(self, datadict):

        if isinstance(datadict, dict):
            for key, value in datadict.items():
                self.stack.append(key)
                # print("/".join(self.stack))
                if isinstance(value, dict) and len(value.keys()) == 0:
                    self.final_dict["/".join(self.stack)] = "EMPTY_DICT"
                if isinstance(value, list) and len(value) == 0:
                    self.final_dict["/".join(self.stack)] = 'EMPTY_LIST'
                if isinstance(value, dict):
                    self.do_walk(value)
                if isinstance(value, list):
                    self.do_walk(value)
                else:
                    self.final_dict["/".join(self.stack)] = value
                self.stack.pop()

        if isinstance(datadict, list):
            n = 0
            for key in datadict:
                self.stack.append(str(n))
                n = n + 1
                if isinstance(key, dict):
                    self.do_walk(key)
                if isinstance(key, list):
                    self.do_walk(key)
                if isinstance(key, str):
                    self.final_dict["/".join(self.stack)] = key
                self.stack.pop()


def json_contain(checkpoint, actual, assert_flag):
    """
    检查实际结果(json)中是否包含检查点(json)。两个必须是同种格式，比如同时是{}或者[]
    :param checkpoint: 检查点(期望结果)
    :param actual:  实际结果
    :param assert_flag: 是否启用assert检查
    :return: 匹配成功或失败
    """
    result = False

    if isinstance(checkpoint, list):
        '''如果期望的检查点是list[]格式，使用此方法检查'''
        find_count = 0
        check_lenth = len(checkpoint)
        for item in checkpoint:
            checkpoint_dict = JsonPathValue(item).get_dict()
            if isinstance(actual, list):
                find_flag = False
                for actual_item in actual:
                    actual_dict = JsonPathValue(actual_item).get_dict()
                    find_flag = list_contain(checkpoint_dict, actual_dict, False)
                    if find_flag:
                        find_count += 1
                        break
                print(find_flag)
            else:
                assert False, "返回的实际结果格式不正确"
            if assert_flag:
                assert find_flag, "期望结果中的\n%s\n匹配失败，实际结果是:\n%s" % (item, actual)
        if find_count == check_lenth:
            result = True
    elif isinstance(checkpoint, dict):
        '''
        如果期望的检查点是dict{}格式
        '''
        checkpoint_dict = JsonPathValue(checkpoint).get_dict()
        actual_dict = JsonPathValue(actual).get_dict()
        if list_contain(checkpoint_dict, actual_dict, True):
            result = True
    return result


def list_contain(checkpoint_dict, actual_dict, assert_flag):
    """
     检查实际结果(list)中是否包含期望结果(list)
    :param checkpoint_dict: 实际结果
    :param actual_dict: 期望结果
    :param assert_flag: 是否启用assert检查
    """
    result = set(checkpoint_dict.items()).issubset(set(actual_dict.items()))
    if assert_flag is True:
        different = set(checkpoint_dict.items()) - (set(actual_dict.items()))
        assert result, \
            "期望结果中的%s匹配失败，实际结果是:\n%s" % (different, actual_dict)

    return result
