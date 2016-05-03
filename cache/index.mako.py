# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462264493.075895
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
        __M_writer(u'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml">\n  <head>\n    <title>Home Dashboard</title>\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n    <link rel="stylesheet" type="text/css" href="/static/css/main.css">\n  </head>\n  <body>\n\t  <div class=\'dashboard\'>\n\t\t  <div class=\'row\'>\n\t\t\t  <div class=\'item temperature\'>\n\t\t\t\t  <div class=\'body\'>\n\t\t\t\t\t  <div class=\'image\'>\n\t\t\t\t\t\t  <img src=\'/static/images/tool.png\' />\n\t\t\t\t\t  </div>\n\t\t\t\t\t  <div class=\'content\'>\n\t\t\t\t\t\t  <div class=\'mesure\'>\n\t\t\t\t\t\t\t  <div class=\'mesureTitle\'>\n\t\t\t\t\t\t\t\t  Average air temperature:\n\t\t\t\t\t\t\t  </div>\n\t\t\t\t\t\t\t  <div class=\'mesureValue\'>\n\t\t\t\t\t\t\t\t  23.6 C\n\t\t\t\t\t\t\t  </div>\n\t\t\t\t\t\t  </div>\n\t\t\t\t\t  </div>\n\t\t\t\t  </div>\n\t\t\t\t  <div class=\'footer\'>\n\t\t\t\t\t  <div class=\'footerText\'>\n\t\t\t\t\t      <span>Click to more</span>\n\t\t\t\t\t  </div>\n\t\t\t\t  </div>\n\t\t\t  </div>\n\t\t\t  <div class=\'item electricity\'>\n\t\t\t\t  <div class=\'body\'>\n\t\t\t\t\t  <div class=\'image\'>\n\t\t\t\t\t\t  <img src=\'/static/images/electricity.png\' />\n\t\t\t\t\t  </div>\n\t\t\t\t\t  <div class=\'content\'>\n\t\t\t\t\t\t  <div class=\'mesure\'>\n\t\t\t\t\t\t\t  <div class=\'mesureTitle\'>\n\t\t\t\t\t\t\t\t  Average usage:\n\t\t\t\t\t\t\t  </div>\n\t\t\t\t\t\t\t  <div class=\'mesureValue\'>\n\t\t\t\t\t\t\t\t  16 kWh\n\t\t\t\t\t\t\t  </div>\n\t\t\t\t\t\t  </div>\n\t\t\t\t\t  </div>\n\t\t\t\t  </div>\n\t\t\t\t  <div class=\'footer\'>\n\t\t\t\t\t  <div class=\'footerText\'>\n\t\t\t\t\t      <span>Click to more</span>\n\t\t\t\t\t  </div>\n\t\t\t\t  </div>\n\t\t\t  </div>\n\t\t  </div>\n\t  </div>\n  </body>\n  <script data-main="/static/scripts/common" src="/static/scripts/require.js"></script>\n  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>\n  <script>\n    require([\'common\'], function() {\n\trequire([\'pages/main\']);\n    });\n  </script>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "index.mako", "filename": "/mnt/external/weatherStation/weatherStationApp/template/index.mako"}
__M_END_METADATA
"""
