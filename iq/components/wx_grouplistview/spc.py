#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Wx GroupListView specification module.
"""

import wx

from iq.object import object_spc
from ...editor import property_editor_id

__version__ = (0, 0, 0, 1)

COMPONENT_TYPE = 'iqWxGroupListView'

WXGROUPLISTVIEW_STYLE = {
    'LC_LIST': wx.LC_LIST,
    'LC_REPORT': wx.LC_REPORT,
    'LC_VIRTUAL': wx.LC_VIRTUAL,
    'LC_ICON': wx.LC_ICON,
    'LC_SMALL_ICON': wx.LC_SMALL_ICON,
    'LC_ALIGN_TOP': wx.LC_ALIGN_TOP,
    'LC_ALIGN_LEFT': wx.LC_ALIGN_LEFT,
    'LC_AUTOARRANGE': wx.LC_AUTOARRANGE,
    'LC_EDIT_LABELS': wx.LC_EDIT_LABELS,
    'LC_NO_HEADER': wx.LC_NO_HEADER,
    'LC_SINGLE_SEL': wx.LC_SINGLE_SEL,
    'LC_SORT_ASCENDING': wx.LC_SORT_ASCENDING,
    'LC_SORT_DESCENDING': wx.LC_SORT_DESCENDING,
    'LC_HRULES': wx.LC_HRULES,
    'LC_VRULES': wx.LC_VRULES,
    #
    'SUNKEN_BORDER': wx.SUNKEN_BORDER,
}

WXGROUPLISTVIEW_SPC = {
    'name': 'default',
    'type': COMPONENT_TYPE,
    'description': '',
    'activate': True,
    'uuid': None,

    '_children_': [],

    'position': (-1, -1),
    'size': (100, 100),
    'foreground_colour': None,
    'background_colour': None,
    'style': wx.TAB_TRAVERSAL,

    'even_rows_background_colour': None,
    'odd_rows_background_colour': None,

    'data_src': None,
    'get_dataset': None,

    'sortable': True,

    'selected': None,
    'activated': None,
    'conv_record': None,
    'conv_dataset': None,

    'get_row_text_colour': None,
    'get_row_background_colour': None,

    'show_items_count': False,

    '__package__': u'wxPython',
    '__icon__': 'fatcow/table_heatmap',
    '__parent__': object_spc.OBJECT_SPC,
    '__doc__': None,
    '__content__': ('iqWxColumn', ),
    '__edit__': {
        'position': property_editor_id.POINT_EDITOR,
        'size': property_editor_id.SIZE_EDITOR,
        'foreground_colour': property_editor_id.COLOUR_EDITOR,
        'background_colour': property_editor_id.COLOUR_EDITOR,
        'style': {
            'editor': property_editor_id.FLAG_EDITOR,
            'choices': WXGROUPLISTVIEW_STYLE,
        },

        'even_rows_background_colour': property_editor_id.COLOUR_EDITOR,
        'odd_rows_background_colour': property_editor_id.COLOUR_EDITOR,

        'data_src': {
            'editor': property_editor_id.PASSPORT_EDITOR,
        },
        'get_dataset': property_editor_id.METHOD_EDITOR,

        'sortable': property_editor_id.CHECKBOX_EDITOR,

        'on_selected': property_editor_id.EVENT_EDITOR,
        'on_activated': property_editor_id.EVENT_EDITOR,

        'conv_record': property_editor_id.METHOD_EDITOR,
        'conv_dataset': property_editor_id.METHOD_EDITOR,

        'get_row_foreground_colour': property_editor_id.METHOD_EDITOR,
        'get_row_background_colour': property_editor_id.METHOD_EDITOR,

        'show_items_count': property_editor_id.CHECKBOX_EDITOR,

    },
    '__help__': {
        'position': u'Panel position',
        'size': u'Panel size',
        'foreground_colour': u'Foreground colour',
        'background_colour': u'Background colour',
        'style': u'Control style',

        'even_rows_background_colour': u'Even rows background colour',
        'odd_rows_background_colour': u'Odd rows background colour',

        'data_src': u'Data source object passport',
        'get_dataset': u'Get dataset as list of record dictionary',

        'sortable': u'Can sort?',

        'on_selected': u'Select item event',
        'on_activated': u'Activate item event',

        'conv_record': u'Convert record method',
        'conv_dataset': u'Convert dataset method',

        'get_row_foreground_colour': u'Get text colour row method',
        'get_row_background_colour': u'Get background colour row method',

        'show_items_count': u'Show group items count?',
    },
}

SPC = WXGROUPLISTVIEW_SPC
