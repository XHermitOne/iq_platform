#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module <month_dialog.py>. 
Generated by the iqFramework module the Glade prototype.
"""

import datetime
import os
import os.path
import signal
import gi

gi.require_version('Gtk', '3.0')
import gi.repository.Gtk

from iq.util import log_func
from iq.util import dt_func

from iq.engine.gtk import gtk_handler
# from iq.engine.gtk import gtktreeview_manager
# from iq.engine.gtk import gtkwindow_manager

__version__ = (0, 0, 0, 1)


class iqMonthDialog(gtk_handler.iqGtkHandler):
    """
    Unknown class.
    """
    def __init__(self, *args, **kwargs):
        self.glade_filename = os.path.join(os.path.dirname(__file__), 'month_dialog.glade')
        gtk_handler.iqGtkHandler.__init__(self, glade_filename=self.glade_filename,
                                          top_object_name='month_dialog',  
                                          *args, **kwargs)
                                          
    def init(self, title=None, default_year=None, default_month=None):
        """
        Init form.

        :param title: Dialog title.
        :param default_year: Default year.
        :param default_month: Default month.
        """
        self.initImages()
        self.initControls()

    def initImages(self):
        """
        Init images of controls on form.
        """
        pass

    def initControls(self, title=None, default_year=None, default_month=None):
        """
        Init controls method.

        :param title: Dialog title.
        :param default_year: Default year.
        :param default_month: Default month.
        """
        if title:
            self.getGtkTopObject().set_title(title)

        self.getGtkObject('year_spinbutton').set_range(datetime.date.min.year,
                                                       datetime.date.max.year)
        if default_year:
            self.getGtkObject('year_spinbutton').set_value(default_year)
        else:
            cur_year = datetime.date.today().year
            self.getGtkObject('year_spinbutton').set_value(cur_year)

        for month_name in dt_func.RU_MONTHS:
            model = self.getGtkObject('month_combobox').get_model()
            model.append([month_name])

        if default_month:
            self.getGtkObject('month_combobox').set_active(default_month - 1)
        else:
            cur_month = datetime.date.today().month
            self.getGtkObject('month_combobox').set_active(cur_month - 1)

    def onCancelButtonClicked(self, widget):
        """
        <Cancel> button click handler.
        """
        self.getGtkTopObject().close()

    def onOkButtonClicked(self, widget):
        """
        <OK> button click handler.
        """
        self.getGtkTopObject().close()
