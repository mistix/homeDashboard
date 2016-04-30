# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462018652.043065
_enable_loop = True
_template_filename = '/mnt/external/weatherStation/weatherStationApp/template/electricity.mako'
_template_uri = 'electricity.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml">\n  <head>\n    <title>Home Temperature</title>\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n    <link rel="stylesheet" type="text/css" href="/static/css/electricity.css">\n  </head>\n  <body>\n      <ul>\n\t  <li><a class=\'active\' href=\'#lastMonth\'>Ostatni miesiac</a></li>\n\t  <li><a href=\'#twoMonths\'>Ostatnie 2 miesiace</a></li>\n\t  <li><a href=\'#addNewValue\'>Dodaj odczyt</a></li>\n\t  <li class=\'floatRight\'><a href=\'/index\'>Dashboard</a></li>\n      </ul>\n      <div class=\'insertBody hidden\'>\n\t  <span class=\'boldText\'>Licznik</span>\n\t  <select id=\'meterPicker\'></select>\n\t  <input id=\'meterValue\' type=\'text\' />\n\t  <button id=\'addNewReading\' type=\'button\'>Dodaj</button>\n      </div>\n      <div id="content-container">\n\t<div id="curve_chart"></div>\n\t  <div id=\'loading\' class=\'modal\'></div>\n      </div>\n  </body>\n  <script data-main="/static/scripts/common" src="/static/scripts/require.js"></script>\n  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>\n  <script>\n    require([\'common\'], function() {\n\trequire([\'pages/electricity\']);\n    });\n  </script>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "electricity.mako", "filename": "/mnt/external/weatherStation/weatherStationApp/template/electricity.mako"}
__M_END_METADATA
"""
