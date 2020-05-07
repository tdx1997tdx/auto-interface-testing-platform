# -*- coding: utf-8 -*-
"""日志模块"""
import os, sys
import logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps


def get_logger(name='system', level=''):
    """ get logger Factory function """
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.StreamHandler(sys.stdout, bubble=False, encoding='utf-8', level=level).push_thread()
    return logbook.Logger(name)


LOG = get_logger(level='INFO')


def logger(param):
    """ function from logger meta """

    def wrap(function):
        """ logger wrapper """

        @wraps(function)
        def _wrap(*args, **kwargs):
            """ wrap tool """
            LOG.info("当前模块 {}".format(param))
            return function(*args, **kwargs)

        return _wrap

    return wrap
