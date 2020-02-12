#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data model component.
"""

from ... import object

from . import spc
from . import model

__version__ = (0, 0, 0, 1)


class iqDataModel(object.iqObject, model.iqModelManager):
    """
    Data model component.
    """
    def __init__(self, parent=None, resource=None, context=None, *args, **kwargs):
        """
        Standart component constructor.

        :param parent: Parent object.
        :param resource: Object resource dictionary.
        :param context: Context dictionary.
        """
        object.iqObject.__init__(parent=parent, resource=resource, spc=spc.SPC, context=context)
        model.iqModelManager.__init__(self, *args, **kwargs)


COMPONENT = iqDataModel
