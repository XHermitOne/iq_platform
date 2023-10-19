#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Accumulate registry component.
"""

from ... import object

from . import spc
from . import acc_registry

from ...util import log_func

from .. import data_column

__version__ = (0, 0, 1, 2)


REQUISITE_VAL_TYPE_TRANSLATE = dict(Text='text',
                                    Integer='int',
                                    Float='float',
                                    DateTime='datetime')


class iqDataAccumulateRegistry(acc_registry.iqAccRegistry, object.iqObject):
    """
    Accumulate registry component.
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
            log_func.warning(u'DB URL not defined for accumulate registry <%s>' % self.getName())
        acc_registry.iqAccRegistry.__init__(self, db_url=db_url,
                                            operation_table_name=self.getOperationTabName(),
                                            result_table_name=self.getResultTabName())

        self.createChildren()

        dimension_requisite_names = self.getAttribute('dimension_requisites')
        dimension_requisites = [requisite for requisite in self.getChildrenRequisites() if
                                requisite.getName() in dimension_requisite_names]
        for requisite in dimension_requisites:
            requisite_name = requisite.getName()
            requisite_type = REQUISITE_VAL_TYPE_TRANSLATE.get(requisite.getFieldType(), 'text')
            self.addDimensionRequisite(requisite_name, requisite_type)

        resource_requisite_names = self.getAttribute('resource_requisites')
        resource_requisites = [requisite for requisite in self.getChildrenRequisites() if
                               requisite.getName() in resource_requisite_names]
        for requisite in resource_requisites:
            requisite_name = requisite.getName()
            requisite_type = REQUISITE_VAL_TYPE_TRANSLATE.get(requisite.getFieldType(), 'text')
            self.addResourceRequisite(requisite_name, requisite_type)

        used_requisite_names = self.getDimensionRequisiteNames() + self.getResourceRequisiteNames()
        extended_requisite_names = [requisite.getName() for requisite in self.getChildrenRequisites() if requisite.getName() not in used_requisite_names]
        extended_requisites = [requisite for requisite in self.getChildrenRequisites() if
                               requisite.getName() in extended_requisite_names]
        for requisite in extended_requisites:
            requisite_name = requisite.getName()
            requisite_type = REQUISITE_VAL_TYPE_TRANSLATE.get(requisite.getFieldType(), 'text')
            self.addExtendedRequisite(requisite_name, requisite_type)

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

    def getResultTabName(self):
        """
        Get result table name.
        """
        return self.getAttribute('result_table')

    def updateLinkDataDataset(self, dataset, columns=None):
        """
        Update dataset by link object data

        :param dataset: Dataset list.
        :param columns: Column object list.
        :return: Updated dataset.
        """
        if columns is None:
            columns = self.getChildren()
        return acc_registry.iqAccRegistry.updateLinkDataDataset(self, dataset=dataset, columns=columns)

    def updateLinkDataRecord(self, record, columns=None):
        """
        Update record by link object data

        :param record: Record dictionary.
        :param columns: Column object list.
        :return: Updated record dictionary.
        """
        if columns is None:
            columns = self.getChildren()
        return acc_registry.iqAccRegistry.updateLinkDataRecord(self, record=record, columns=columns)


COMPONENT = iqDataAccumulateRegistry
