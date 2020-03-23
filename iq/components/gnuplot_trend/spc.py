#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gnuplot historical trend specification module.
"""

import os.path

from ...editor import property_editor_id
from .. import wx_panel

from . import trend_proto
from . import gnuplot_trend_proto

__version__ = (0, 0, 0, 1)

COMPONENT_TYPE = 'iqGnuplotTrend'

GNUPLOTTREND_SPC = {
    'name': 'default',
    'type': COMPONENT_TYPE,
    'description': '',
    'activate': True,
    'uuid': None,

    '_children_': [],

    'x_format': trend_proto.DEFAULT_X_FORMAT,
    'y_format': trend_proto.DEFAULT_Y_FORMAT,
    'scene_min': ('00:00:00', 0.0),
    'scene_max': ('23:59:59', 100.0),
    'adapt_scene': False,

    'x_precision': gnuplot_trend_proto.DEFAULT_X_PRECISION,
    'y_precision': gnuplot_trend_proto.DEFAULT_Y_PRECISION,

    '__package__': u'SCADA',
    '__icon__': 'fatcow%schart_line' % os.path.sep,
    '__parent__': wx_panel.SPC,
    '__doc__': None,
    '__content__': ('iqTrendPen', ),
    '__edit__': {
    },
    '__help__': {
        'x_format': u'X axis data presentation format',
        'y_format': u'Y axis data presentation format',
        'scene_min': u'The minimum value of the visible trend scene',
        'scene_max': u'The maximum value of the visible trend scene',
        'adapt_scene': u'Sign of scene adaptation according to',

        'x_precision': u'X grid trend precision',
        'y_precision': u'Y grid trend precision',
    },
}

SPC = GNUPLOTTREND_SPC
