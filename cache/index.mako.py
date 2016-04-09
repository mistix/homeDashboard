# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460140684.149965
_enable_loop = True
_template_filename = '/mnt/external/weatherStation/weatherStationApp/template/index.mako'
_template_uri = 'index.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml">\n  <head>\n    <title>Home Temperature</title>\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n    <script type="text/javascript" src="/static/js/jquery-1.7.2.min.js"></script> \n    <script type="text/javascript" src="/static/js/twiseless.js"></script> \n    <script type="text/javascript">\n      $(document).ready(function() {\n        $("#viz").twiseless("render");\n      });\n    </script>\n  </head>\n  <body>\n    <div id="container">\n      <div id="header">\n\t<h1>Home Temperature</h1>\n      </div>\n      <div id="content-container">\n\t<div id="content">\n\t</div>\n      </div>\n    </div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "index.mako", "filename": "/mnt/external/weatherStation/weatherStationApp/template/index.mako"}
__M_END_METADATA
"""
