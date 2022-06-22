#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module <property_box.py>. 
Generated by the iqFramework module the Glade prototype.
"""

import datetime
import os
import os.path
import signal
import gi

gi.require_version('Gtk', '3.0')
import gi.repository.Gtk

from ....util import log_func
from ....util import global_func

from ....engine.gtk.dlg import calendar_dialog

from iq.engine.gtk import gtk_handler
# from iq.engine.gtk import gtktreeview_manager
# from iq.engine.gtk import gtkwindow_manager

from . import property_editor_proto

__version__ = (0, 0, 0, 1)

DATE_FMT = global_func.getDefaultStrDateFmt()


class iqDatePropertyEditor(gtk_handler.iqGtkHandler,
                           property_editor_proto.iqPropertyEditorProto):
    """
    Date property editor class.
    """
    def __init__(self, label='', value=None, choices=None, default=None, *args, **kwargs):
        self.glade_filename = os.path.join(os.path.dirname(__file__), 'date_property_editor.glade')
        gtk_handler.iqGtkHandler.__init__(self, glade_filename=self.glade_filename,
                                          top_object_name='property_box',  
                                          *args, **kwargs)

        property_editor_proto.iqPropertyEditorProto.__init__(self, label=label, value=value,
                                                             choices=choices, default=default)

        if label:
            self.getGtkObject('property_label').set_text(label)
        if value:
            self.setValue(value)

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

    def setValue(self, value):
        """
        Set value.
        """
        if value and isinstance(value, (datetime.date, datetime.datetime)):
            date_str = value.strftime(DATE_FMT)
            self.getGtkObject('property_entry').set_text(date_str)
        self.value = value

    def getValue(self):
        """
        Get value.
        """
        return self.value

    def onPropertyIconPress(self, widget):
        """
        Property icon mouse click handler.
        """
        selected_date = calendar_dialog.openCalendarDialog(title=u'Calendar', prompt_text=u'Select date',
                                                           default_date=self.value)
        if selected_date is not None:
            self.setValue(selected_date)

    def setHelpString(self, help_string):
        """
        Set help string.

        :param help_string: Help string.
        """
        label = self.getGtkObject('property_label')
        label.set_property('tooltip-text', help_string)
