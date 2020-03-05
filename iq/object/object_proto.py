#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Base object class module.
"""

from . import object_context
from ..util import global_func
from ..util import spc_func
from ..util import log_func

__version__ = (0, 0, 0, 1)


class iqObject(object):
    """
    Base object class.
    """
    def __init__(self, parent=None, resource=None, spc=None, context=None, *args, **kwargs):
        """
        Constructor.

        :param parent: Parent object.
        :param resource: Object resource dictionary.
        :param spc: Component specification.
        :param context: Context dictionary.
        :param args:
        :param kwargs:
        """
        self._parent = parent
        self._resource = spc_func.fillResourceBySpc(resource=resource, spc=spc)
        self._context = self.createContext(context)

        self._children = None

    def getName(self):
        """
        Object name.
        """
        res = self.getResource()
        if isinstance(res, dict):
            return res.get('name', u'Unknown')
        return u'Unknown'

    def getType(self):
        """
        Object type.
        """
        res = self.getResource()
        if isinstance(res, dict):
            return res.get('type', u'Unknown')
        return u'Unknown'

    def getParent(self):
        """
        Get parent object.
        """
        return self._parent

    def getResource(self):
        """
        Get object resource dictionary.
        """
        return self._resource

    def getContext(self):
        """
        Get context object.
        """
        return self._context

    def createContext(self, context=None):
        """
        Create object context.

        :param context: Context dictionary.
        :return: Context.
        """
        self._context = None
        if context is None:
            self._context = object_context.iqContext(runtime_object=self)
        elif isinstance(context, dict):
            self._context = object_context.iqContext(runtime_object=self)
            self._context.update(context)
        elif isinstance(context, object_context.iqContext):
            self._context = context
        return self._context

    def getKernel(self):
        """
        Get kernel object.
        """
        return self._context.getKernel() if self._context else global_func.getKernel()

    def getAttribute(self, attribute_name):
        """
        Get attribute from resource.

        :param attribute_name: Attribute name.
        :return: Attribute value.
        """
        value = self._resource.get(attribute_name, None) if self._resource else None
        return value

    def getChildren(self):
        """
        Get children objects.
        """
        if self._children is None:
            self._children = self.createChildren()
        return self._children

    def createChildren(self):
        """
        Create children objects.

        :return: Children list or None if error.
        """
        try:
            res_children = self._resource.get(spc_func.CHILDREN_ATTR_NAME, list())
            kernel = self.getKernel()
            context = self.getContext()

            self._children = [kernel.createByResource(parent=self,
                                                      resource=res_child,
                                                      context=context) for res_child in res_children]
            return self._children
        except:
            log_func.fatal(u'Error create children obj object <%s : %s>' % (self.getName(), self.getType()))
        return list()

    def hasChild(self, name):
        """
        Is there a child with that name?

        :param name: Child object name.
        :return: True/False.
        """
        res_children = self._resource.get(spc_func.CHILDREN_ATTR_NAME, list())
        return name in [res_child.get('name', None) for res_child in res_children]

    def getChild(self, name):
        """
        Get child object by name.

        :param name: Child object name.
        :return: Child object or None if not found.
        """
        children = self.getChildren()

        for child in children:
            if name == child.getName():
                return child

        log_func.warning(u'Child <%s> not found in <%s : %s>' % (name, self.getName(), self.getType()))
        return None
