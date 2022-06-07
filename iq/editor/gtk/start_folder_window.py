#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module <start_folder_window.py>. 
Generated by the iqFramework module the Glade prototype.
"""

import os
import os.path
import signal
import gi

gi.require_version('Gtk', '3.0')
import gi.repository.Gtk

from iq.util import log_func
from ...util import lang_func
from ...util import global_func
from ...util import res_func
from ...util import id_func

from ...dialog import dlg_func

from iq.engine.gtk import gtk_handler
# from iq.engine.gtk import gtktreeview_manager
# from iq.engine.gtk import gtkwindow_manager

from ...project import prj

from ...engine.gtk import stored_gtk_form_manager

from ..wx import wxfb_manager
from ..jasper_report import jasperreport_manager
from ..lime_report import limereport_manager
from . import glade_manager

__version__ = (0, 0, 0, 1)

_ = lang_func.getTranslation().gettext


class iqStartFolderWindow(gtk_handler.iqGtkHandler,
                          stored_gtk_form_manager.iqStoredGtkFormsManager):
    """
    Start project folder window class.
    """
    def __init__(self, *args, **kwargs):
        self.glade_filename = os.path.join(os.path.dirname(__file__), 'start_folder_win.glade')
        gtk_handler.iqGtkHandler.__init__(self, glade_filename=self.glade_filename,
                                          top_object_name='start_folder_window',  
                                          *args, **kwargs)
        self.folder_path = None

        self.loadCustomProperties()

    def init(self):
        """
        Init form.
        """
        self.initImages()
        self.initControls()

    def initImages(self):
        """
        Init images of controls on form.
        """
        pass

    def initControls(self):
        """
        Init controls method.
        """
        pass

    def onDestroy(self, widget):
        """
        Destroy window handler.
        """
        self.saveCustomProperties()
        gi.repository.Gtk.main_quit()

    def onRunProjectButtonClicked(self, widget):
        """
        Run project button click handler.
        """
        project_manager = prj.iqProjectManager()
        selected_prj_name = os.path.basename(self.folder_path) if self.folder_path else None
        project_manager.run(selected_prj_name)

        gi.repository.Gtk.main_quit()

    def onNewButtonClicked(self, widget):
        """
        New button click handler.
        """
        try:
            menu = self.createNewMenu()
            menu.popup()
            menu.destroy()
        except:
            log_func.fatal(u'Error New menu popup')

        gi.repository.Gtk.main_quit()

    def createNewMenu(self):
        """
        Create New menu.

        :return: Menu object.
        """
        new_menu = gi.repository.Gtk.Menu()

        menuitem_label = _(u'New resource')
        menuitem = gi.repository.Gtk.MenuItem(label=menuitem_label)
        new_menu.append(menuitem)
        menuitem.connect('select', self.onNewResMenuItem)
        new_menu.append(gi.repository.Gtk.SeparatorMenuItem())

        menuitem_label = _(u'New wxFormBuilder project')
        menuitem = gi.repository.Gtk.MenuItem(label=menuitem_label)
        new_menu.append(menuitem)
        menuitem.connect('select', self.onNewWXFBMenuItem)

        menuitem_label = _(u'New Glade project')
        menuitem = gi.repository.Gtk.MenuItem(label=menuitem_label)
        new_menu.append(menuitem)
        menuitem.connect('select', self.onNewGladeMenuItem)

        menuitem_label = _(u'New JasperReport report')
        menuitem = gi.repository.Gtk.MenuItem(label=menuitem_label)
        new_menu.append(menuitem)
        menuitem.connect('select', self.onNewJasperReportMenuItem)

        menuitem_label = _(u'New LimeReport report')
        menuitem = gi.repository.Gtk.MenuItem(label=menuitem_label)
        new_menu.append(menuitem)
        menuitem.connect('select', self.onNewLimeReportMenuItem)

        return new_menu

    def onNewResMenuItem(self, widget):
        """
        Menu item handler <New resource>.
        """
        new_res_filename = os.path.join(self.folder_path,
                                        'default%d%s' % (id_func.genNewId(),
                                                         res_func.RESOURCE_FILE_EXT)) if self.folder_path else None
        res_filename = new_resource_dialog.createNewResource(parent=self, res_filename=new_res_filename)

        self.getGtkTopObject().close()

        if res_filename is not None:
            resource_editor.openResourceEditor(res_filename=res_filename)

    def onNewWXFBMenuItem(self, widget):
        """
        Menu item handler <New wxFormBuilder project>.
        """
        wxfb_manager.runWXFormBuilder()
        self.getGtkTopObject().close()

    def onNewGladeMenuItem(self, widget):
        """
        Menu item handler <New Glade project>.
        """
        glade_manager.runGlade()
        self.getGtkTopObject().close()

    def onNewJasperReportMenuItem(self, widget):
        """
        Menu item handler <New JasperReport project>.
        """
        new_basename = dlg_func.getTextEntryDlg(parent=self, title=_(u'NEW'),
                                                prompt_text=_(u'New JasperReport filename'))
        if new_basename:
            new_prj_filename = os.path.join(self.folder_path,
                                            new_basename + jasperreport_manager.JASPER_REPORT_PROJECT_FILE_EXT)
            if jasperreport_manager.createJasperReportProjectFile(new_prj_filename):
                dlg_func.openMsgBox(title=_(u'CREATE'),
                                    prompt_text=_(u'Create JasperReport file') + ' <%s>' % new_prj_filename)
                self.getGtkTopObject().close()
                jasperreport_manager.runJasperReportEditor(filename=new_prj_filename)
            else:
                dlg_func.openWarningBox(title=_(u'ERROR'),
                                        prompt_text=_(u'Error create JasperReport file') + ' <%s>' % new_prj_filename)
                self.getGtkTopObject().close()

    def onNewLimeReportMenuItem(self, widget):
        """
        Menu item handler <New LimeReport project>.
        """
        new_basename = dlg_func.getTextEntryDlg(parent=self, title=_(u'NEW'),
                                                prompt_text=_(u'New LimeReport filename'))
        if new_basename:
            new_prj_filename = os.path.join(self.folder_path,
                                            new_basename + limereport_manager.LIME_REPORT_PROJECT_FILE_EXT)
            if limereport_manager.createLimeReportProjectFile(new_prj_filename):
                dlg_func.openMsgBox(title=_(u'CREATE'),
                                    prompt_text=_(u'Create LimeReport file') + ' <%s>' % new_prj_filename)
                self.getGtkTopObject().close()
                limereport_manager.runLimeReportEditor(filename=new_prj_filename)
            else:
                dlg_func.openWarningBox(title=_(u'ERROR'),
                                        prompt_text=_(u'Error create LimeReport file') + ' <%s>' % new_prj_filename)
                self.getGtkTopObject().close()

    def onHelpButtonClicked(self, widget):
        """
        Help button click handler.
        """
        self.getGtkTopObject().close()

    def onExitButtonClicked(self, widget):
        """
        Exit button handler.
        """
        self.getGtkTopObject().close()


def openStartFolderWindow():
    """
    Open start_folder_window.

    :return: True/False.
    """
    result = False
    obj = None
    try:
        obj = iqStartFolderWindow()
        obj.init()
        obj.getGtkTopObject().run()
        result = True
    except:
        log_func.fatal(u'Error open window <start_folder_window>')

    if obj and obj.getGtkTopObject() is not None:
        obj.getGtkTopObject().destroy()
    return result                    


def startFolderEditor(folder_path=None):
    """
    Open start folder editor window.

    :param folder_path: Folder path.
    :return: True/False.
    """
    log_func.info(u'GTK library version: %s' % gi.__version__)

    result = False
    win = None
    try:
        win = iqStartFolderWindow()
        win.folder_path = folder_path
        win.init()
        win.getGtkTopObject().show_all()
        result = True
    except:
        log_func.fatal(u'Error open window <start_editor_window>')

    gi.repository.Gtk.main()

    if win and win.getGtkTopObject() is not None:
        win.getGtkTopObject().destroy()
    return result
