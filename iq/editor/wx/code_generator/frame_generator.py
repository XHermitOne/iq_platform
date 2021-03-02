#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python frame generate functions.
"""

import os
import os.path
import inspect

from ....util import log_func
from ....util import str_func
from ....util import py_func
from ....util import txtfile_func


__version__ = (0, 0, 0, 1)


SHOW_FRAME_FUNC_BODY_FMT = u'''
def show%s(parent=None):
    \"\"\"
    Open frame.
    
    :param parent: Parent window.
    :return: True/False.
    \"\"\"
    try:
        if parent is None:
            parent = global_func.getMainWin()

        frame = %s(parent)
        frame.init()
        frame.Show()
        return True
    except:
        log_func.fatal(u'Error show frame <%s>')
    return False
'''

START_FRAME_FUNC_BODY_FMT = u'''
def start%s():
    """
    Start.
    """
    app = global_func.getApplication()
    if app is None:
        log_func.info(u'Create WX application')
        app = global_func.createApplication()
    if show%s():
        app.MainLoop()


if __name__ == '__main__':
    start%s()
'''


GEN_PY_MODULE_FMT = u'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

\"\"\"
Frame module <%s>. 
Generated by the iqFramework module the wxFormBuider prototype form.
\"\"\"

import wx
from . import %s

import iq
from iq.util import log_func
from iq.util import global_func

from iq.engine.wx import form_manager

__version__ = (0, 0, 0, 1)


class %s(%s.%s, 
        form_manager.iqFormManager):
    \"\"\"
    Frame.
    \"\"\"
    def __init__(self, *args, **kwargs):
        \"\"\"
        Constructor.
        \"\"\"
        %s.%s.__init__(self, *args, **kwargs)

    def init(self):
        \"\"\"
        Init frame.
        \"\"\"
        self.initImages()
        self.initControls()

    def initImages(self):
        \"\"\"
        Init images method.
        \"\"\"
        pass

    def initControls(self):
        \"\"\"
        Init controls method.
        \"\"\"
        pass

%s
%s
%s
'''


WXFB_PRJ_MAINFORM_FMT = '''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<wxFormBuilder_Project>
    <FileVersion major="1" minor="15" />
    <object class="Project" expanded="1">
        <property name="class_decoration"></property>
        <property name="code_generation">Python</property>
        <property name="disconnect_events">1</property>
        <property name="disconnect_mode">source_name</property>
        <property name="disconnect_php_events">0</property>
        <property name="disconnect_python_events">0</property>
        <property name="embedded_files_path">res</property>
        <property name="encoding">UTF-8</property>
        <property name="event_generation">connect</property>
        <property name="file">%s</property>
        <property name="first_id">1000</property>
        <property name="help_provider">none</property>
        <property name="indent_with_spaces"></property>
        <property name="internationalize">0</property>
        <property name="name">%s</property>
        <property name="namespace"></property>
        <property name="path">.</property>
        <property name="precompiled_header"></property>
        <property name="relative_path">1</property>
        <property name="skip_lua_events">1</property>
        <property name="skip_php_events">1</property>
        <property name="skip_python_events">1</property>
        <property name="ui_table">UI</property>
        <property name="use_enum">0</property>
        <property name="use_microsoft_bom">0</property>
        <object class="Frame" expanded="1">
            <property name="aui_managed">0</property>
            <property name="aui_manager_style">wxAUI_MGR_DEFAULT</property>
            <property name="bg"></property>
            <property name="center">wxBOTH</property>
            <property name="context_help"></property>
            <property name="context_menu">1</property>
            <property name="enabled">1</property>
            <property name="event_handler">impl_virtual</property>
            <property name="extra_style"></property>
            <property name="fg"></property>
            <property name="font"></property>
            <property name="hidden">0</property>
            <property name="id">wxID_ANY</property>
            <property name="maximum_size"></property>
            <property name="minimum_size"></property>
            <property name="name">%s</property>
            <property name="pos"></property>
            <property name="size">929,574</property>
            <property name="style">wxDEFAULT_FRAME_STYLE|wxMAXIMIZE</property>
            <property name="subclass"></property>
            <property name="title"></property>
            <property name="tooltip"></property>
            <property name="window_extra_style"></property>
            <property name="window_name"></property>
            <property name="window_style">wxTAB_TRAVERSAL</property>
            <property name="xrc_skip_sizer">1</property>
            <object class="wxStatusBar" expanded="1">
                <property name="bg"></property>
                <property name="context_help"></property>
                <property name="context_menu">1</property>
                <property name="enabled">1</property>
                <property name="fg"></property>
                <property name="fields">1</property>
                <property name="font"></property>
                <property name="hidden">0</property>
                <property name="id">wxID_ANY</property>
                <property name="maximum_size"></property>
                <property name="minimum_size"></property>
                <property name="name">mainform_statusBar</property>
                <property name="permission">protected</property>
                <property name="pos"></property>
                <property name="size"></property>
                <property name="style">wxSTB_SIZEGRIP</property>
                <property name="subclass"></property>
                <property name="tooltip"></property>
                <property name="window_extra_style"></property>
                <property name="window_name"></property>
                <property name="window_style"></property>
            </object>
        </object>
    </object>
</wxFormBuilder_Project>
'''


def genFrameClassName(src_class_name):
    """
    Generate frame class name.

    :param src_class_name: Source frame prototype class name.
    :return: New frame class name.
    """
    dst_class_name = src_class_name
    dst_class_name = dst_class_name[:-9] if dst_class_name.endswith('Prototype') else dst_class_name
    dst_class_name = dst_class_name[:-5] if dst_class_name.endswith('Proto') else dst_class_name
    return dst_class_name


def genShowFunctionBody(class_name):
    """
    Generate show function text body.

    :param class_name: Frame class name.
    :return: Function text body.
    """
    function_name = class_name[2:] if class_name.startswith('iq') else class_name
    frm_body_function = SHOW_FRAME_FUNC_BODY_FMT % (function_name,
                                                    class_name,
                                                    class_name)
    return frm_body_function


def genStartFunctionBody(class_name):
    """
    Generate start function text body.

    :param class_name: Frame class name.
    :return: Function text body.
    """
    function_name = class_name[2:] if class_name.startswith('iq') else class_name
    frm_body_function = START_FRAME_FUNC_BODY_FMT % (function_name,
                                                     function_name,
                                                     function_name)
    return frm_body_function


def genPythonFrame(src_module, src_class_name):
    """
    Generation of the frame class text.

    :param src_module: Source module object.
    :param src_class_name: Source class name.
    :return: True/False.
    """
    log_func.info(u'Generate frame class ... START')

    dst_class_name = genFrameClassName(src_class_name)
    src_class = getattr(src_module, src_class_name)

    # Handlers
    src_class_methods = [getattr(src_class, var_name) for var_name in dir(src_class)]
    src_class_events = [method for method in src_class_methods if inspect.isfunction(method) and
                        method.__name__ != '__init__' and
                        'event' in method.__code__.co_varnames and
                        method.__code__.co_argcount == 2]

    # A way to get the source code from a function object+
    #                                                    v
    body_functions = u'\n'.join([u'\n'.join(inspect.getsourcelines(class_method)[0]) for class_method in src_class_events])
    body_functions = body_functions.replace(u'\t', u'    ').replace(u'( ', u'(').replace(u' )', u')')
    log_func.info(u'Append method in class <%s>:' % dst_class_name)
    log_func.debug(body_functions)

    frm_body_function = genShowFunctionBody(dst_class_name)
    start_frm_body_function = genStartFunctionBody(dst_class_name)

    py_txt = GEN_PY_MODULE_FMT % (src_class_name,
                                  src_module.__name__,
                                  dst_class_name, src_module.__name__, src_class_name,
                                  src_module.__name__, src_class_name,
                                  body_functions,
                                  frm_body_function, start_frm_body_function)
    log_func.info(u'Generate frame class ... STOP')
    return py_txt


def genDefaultMainFormFormBuilderPrj(prj_filename=None, rewrite=False):
    """
    Generate default main form wxFormBuilder project file.

    :param prj_filename: wxFormBuilder project filename.
    :param rewrite: Rewrite it if exists?
    :return: True/False.
    """
    if not prj_filename:
        log_func.warning(u'Not define wxFormBuilder project filename')
        return False

    package_dirname = os.path.dirname(prj_filename)
    py_func.createInitModule(package_path=package_dirname, rewrite=rewrite)

    mainform_name = os.path.splitext(os.path.basename(prj_filename))[0].lower()
    mainform_class_name = 'iq%s' % str_func.replaceLower2Upper(mainform_name)
    wxfb_mainform_txt = WXFB_PRJ_MAINFORM_FMT % (mainform_name,
                                                 mainform_name,
                                                 mainform_class_name)
    save_ok = txtfile_func.saveTextFile(txt_filename=prj_filename,
                                        txt=wxfb_mainform_txt,
                                        rewrite=rewrite)
    if save_ok:
        from .. import wxfb_manager
        wxformbuilder_manager = wxfb_manager.iqWXFormBuilderManager()
        return wxformbuilder_manager.generate(prj_filename=prj_filename, asynchro=False)

    return False
