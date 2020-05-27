#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data object history component.
"""

from ... import object

from . import spc
from . import obj_registry

from ...util import log_func

from .. import data_column

__version__ = (0, 0, 0, 1)


REQUISITE_VAL_TYPE_TRANSLATE = dict(Text='text',
                                    Integer='int',
                                    Float='float',
                                    DateTime='datetime')


class iqDataObjectHistory(obj_registry.iqObjRegistry, object.iqObject):
    """
    Data object history component.
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

        db = self.getDB()
        db_url = db.getDBUrl() if db else None
        if not db_url:
            log_func.error(u'DB URL not defined for data object history <%s>' % self.getName())
        obj_registry.iqObjRegistry.__init__(self, db_url=db_url,
                                            operation_table_name=self.getOperationTabName(),
                                            obj_table_name=self.getObjectTabName())

        self.createChildren()

        obj_requisites = self.getChildrenRequisites()
        for requisite in obj_requisites:
            requisite_name = requisite.name
            requisite_type = REQUISITE_VAL_TYPE_TRANSLATE.get(requisite.getTypeValue(), 'text')
            self.addObjRequisite(requisite_name, requisite_type)

    def getDBPsp(self):
        """
        Get database.
        """
        return self.getAttribute('db_engine')

    def getDB(self):
        """
        Get database object.
        """
        db_psp = self.getDBPsp()
        db = None
        if db_psp:
            db = self.getKernel().createByPsp(psp=db_psp)
        return db

    def getChildrenRequisites(self):
        """
        Get children requisites.
        """
        return [child for child in self.getChildren() if issubclass(child.__class__, data_column.COMPONENT)]

    def getOperationTabName(self):
        """
        Get operation table name.
        """
        return self.getAttribute('operation_table')

    def getObjectTabName(self):
        """
        Get object table name.
        """
        return self.getAttribute('obj_table')


COMPONENT = iqDataObjectHistory
