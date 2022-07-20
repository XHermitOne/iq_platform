#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module <single_choice_dialog.py>. 
Generated by the iqFramework module the Glade prototype.
"""

import os
import os.path
import signal
import gi

gi.require_version('Gtk', '3.0')
import gi.repository.Gtk

from iq.util import log_func

from iq.engine.gtk import gtk_handler
from iq.engine.gtk import gtktreeview_manager
# from iq.engine.gtk import gtkwindow_manager

__version__ = (0, 0, 1, 2)


class iqSingleChoiceDialog(gtk_handler.iqGtkHandler,
                           gtktreeview_manager.iqGtkTreeViewManager):
    """
    Single choice dialog class.
    """
    def __init__(self, *args, **kwargs):
        self.glade_filename = os.path.join(os.path.dirname(__file__), 'single_choice_dialog.glade')
        gtk_handler.iqGtkHandler.__init__(self, glade_filename=self.glade_filename,
                                          top_object_name='single_choice_dialog',  
                                          *args, **kwargs)
                                          
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

    def setChoices(self, choices):
        """
        Set choices.
        """
        assert isinstance(choices, (list, tuple)), u'Choices must be list or tuple'

        choice_liststore = self.getGtkObject('choice_liststore')
        choice_liststore.clear()
        for choice in choices:
            choice_liststore.append([str(choice)])

    def onCancelButtonClicked(self, widget):
        """
        Cancel button click handler.
        """
        self.getGtkTopObject().close()

    def onOkButtonClicked(self, widget):
        """
        OK button click handler.
        """
        self.getGtkTopObject().close()


def openSingleChoiceDialog(parent=None, title='', prompt_text='', choices=(),
                           default_idx=-1):
    """
    List selection dialog.

    :param parent: Parent form.
    :param title: Dialog form title.
    :param prompt_text: Dialog form prompt text.
    :param choices: List of selection lines.
    :param default_idx: Default selected line index.
    :return: Selected idx or None if pressed cancel.
    """
    result = -1
    dlg = None
    try:
        dlg = iqSingleChoiceDialog()
        dlg.init()
        if title:
            dlg.getGtkTopObject().set_title(title)
        if prompt_text:
            dlg.getGtkObject('prompt_label').set_label(prompt_text)
        dlg.setChoices(choices)
        if default_idx >= 0:
            dlg.getGtkObject('choice_treeview').set_selection(default_idx)
        response = dlg.getGtkTopObject().run()
        if response == gi.repository.Gtk.ResponseType.OK:
            result = dlg.getGtkTreeViewSelectedRow(treeview=dlg.getGtkObject('choice_treeview'))
    except:
        log_func.fatal(u'Error open window <single_choice_dialog>')

    if dlg and dlg.getGtkTopObject() is not None:
        dlg.getGtkTopObject().destroy()
    return result                    
