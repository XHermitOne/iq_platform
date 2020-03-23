#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data model navigator component.
"""

from ... import object

from . import spc
from . import model_navigator

from ...util import log_func

__version__ = (0, 0, 0, 1)


class iqDataNavigator(model_navigator.iqModelNavigatorManager, object.iqObject):
    """
    Data model navigator component.
    """
    def __init__(self, parent=None, resource=None, context=None, *args, **kwargs):
        """
        Standart component constructor.

        :param parent: Parent object.
        :param resource: Object resource dictionary.
        :param context: Context dictionary.
        """
        component_spc = kwargs['spc'] if 'spc' in kwargs else spc.SPC
        object.iqObject.__init__(self, parent=parent, resource=resource, spc=component_spc, context=context)
        model_navigator.iqModelNavigatorManager.__init__(self, *args, **kwargs)

    def getModelPsp(self):
        """
        Get model passport.
        """
        model_psp = self.getAttribute('model')
        return model_psp

    def getScheme(self):
        """
        Get scheme object by model.

        :return: Data scheme object or None if error.
        """
        model_psp = self.getModelPsp()

        if not model_psp:
            log_func.error(u'Not define model in <%s : %s>' % (self.getName(), self.getType()))
            return None

        psp = self.newPassport().setAsStr(model_psp)
        psp.typename = None
        psp.name = None
        scheme = self.getKernel().getObject(psp=psp, register=True)
        return scheme

    def createModel(self):
        """
        Create model object.

        :return: Model or None if error.
        """
        model_psp = self.getModelPsp()

        if not model_psp:
            log_func.error(u'Not define model in <%s : %s>' % (self.getName(), self.getType()))
            return None

        model_name = self.newPassport().setAsStr(model_psp).name

        scheme = self.getScheme()
        if scheme:
            return scheme.getModel(model_name)
        else:
            log_func.error(u'Error create data scheme object')
        return None


COMPONENT = iqDataNavigator
