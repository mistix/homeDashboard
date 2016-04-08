# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1459669122.488982
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
        __M_writer(u'<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml">\n  <head>\n    <title>.:. Twiseless .:.</title>\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n    <link href="http://fonts.googleapis.com/css?family=Nunito" rel="stylesheet" type="text/css">\n    <link rel="stylesheet" type="text/css" href="/static/css/twiseless.css" /> \n    <!--[if IE]>\n    <script type="text/javascript" src="/static/js/Jit/Extras/excanvas.js"></script>\n    <![endif]-->\n    <script type="text/javascript" src="/static/js/jquery-1.7.2.min.js"></script> \n    <script type="text/javascript" src="/static/js/Jit/jit-yc.js"></script> \n    <script type="text/javascript" src="/static/js/twiseless.js"></script> \n    <script type="text/javascript">\n      $(document).ready(function() {\n        $("#viz").twiseless("render");\n      });\n    </script>\n  </head>\n  <body>\n    <div id="container">\n      <div id="header">\n\t<h1>:: Twiseless</h1>\n      </div>\n      <div id="content-container">\n\t<div id="content">\n\t  <div id="tweets"></div>\n\t</div>\n\t<div id="aside">\n\t  <div id="viz"></div>\n\t</div>\n\t<div id="footer">\n\t  <div id="footer-info">\n\t    &copy; Sylvain Hellegouarch, licensed under a <a href="https://github.com/Lawouach/Twiseless/blob/master/LICENSE">BSD license</a>.\n\t    Layout mostly taken from <a href="http://www.maxdesign.com.au/articles/css-layouts/two-fixed/">maxdesign</a>.\n\t  </div>\n\t</div>\n      </div>\n    </div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "index.mako", "filename": "/mnt/external/weatherStation/weatherStationApp/template/index.mako"}
__M_END_METADATA
"""
