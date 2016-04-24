# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1461345738.704052
_enable_loop = True
_template_filename = '/mnt/external/weatherStation/weatherStationApp/template/temperature.mako'
_template_uri = 'temperature.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml">\n  <head>\n    <title>Home Temperature</title>\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n    <script type="text/javascript" src="/static/js/jquery-1.12.0.min.js"></script>\n    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>\n    <script type="text/javascript" src="/static/js/temperature.js"></script>\n    <link rel="stylesheet" type="text/css" href="/static/css/temperature.css">\n  </head>\n  <body>\n      <ul>\n\t\t  <li><a class=\'active\' href=\'#last24h\'>Ostatnie 24h</a></li>\n\t\t  <li><a href=\'#last48h\'>Ostatnie 48h</a></li>\n\t\t  <li class=\'floatRight\'><a href=\'/index\'>Dashboard</a></li>\n      </ul>\n      <div id=\'chartTitle\'></div>\n      <div id="content-container">\n\t<div id="curve_chart"></div>\n\t  <div id=\'loading\' class=\'modal\'></div>\n      </div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "temperature.mako", "filename": "/mnt/external/weatherStation/weatherStationApp/template/temperature.mako"}
__M_END_METADATA
"""
