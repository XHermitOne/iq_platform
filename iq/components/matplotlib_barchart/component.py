#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MatPlotLib bar chart component.
"""

from ... import object

from . import spc
from . import barchart_proto

from ...util import log_func

__version__ = (0, 0, 0, 1)


class iqMatplotlibBarChart(object.iqObject, barchart_proto.iqMatplotlibBarChartProto):
    """
    MatPlotLib bar chart component class.
    """
    def __init__(self, parent=None, resource=None, context=None, *args, **kwargs):
        """
        Standard component constructor.

        :param parent: Parent object.
        :param resource: Object resource dictionary.
        :param context: Context dictionary.
        """
        component_spc = kwargs['spc'] if 'spc' in kwargs else spc.SPC
        object.iqObject.__init__(self, parent=parent, resource=resource, spc=component_spc, context=context)
        barchart_proto.iqMatplotlibBarChartProto.__init__(self, *args, **kwargs)

    def getBarCount(self):
        """
        Get bar count.
        """
        self._bar_count = self.getAttribute('bar_count')
        return self._bar_count

    def getBarWidth(self):
        """
        Get bar width.
        """
        self._bar_width = self.getAttribute('bar_width')
        return self._bar_width

    def getTitle(self):
        """
        Get title.
        """
        self._title = self.getAttribute('title')
        return self._title

    def getXLabel(self):
        """
        Get X label.
        """
        self._x_label = self.getAttribute('x_label')
        return self._x_label

    def getYLabel(self):
        """
        Get Y label.
        """
        self._y_label = self.getAttribute('y_label')
        return self._y_label

    def getLegend(self):
        """
        Get legend.
        """
        self._legend = self.getAttribute('legend')
        return self._legend

    def getOrientation(self):
        """
        Get orientation.
        """
        self._orientation = self.getAttribute('orientation')
        return self._orientation


COMPONENT = iqMatplotlibBarChart
