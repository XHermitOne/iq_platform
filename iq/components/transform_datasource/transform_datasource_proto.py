#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Transformation table data component prototype class.
"""

import pandas

from ...util import log_func

__version__ = (0, 0, 0, 1)


class iqTransformDataSourceProto(object):
    """
    Transformation table data component prototype class.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        self._dataframe = None

    def getDataFrame(self):
        """
        Get DataFrame object.

        :return: Pandas DataFrame object or None if object not defined.
        """
        return self._dataframe

    def importData(self, data=None):
        """
        Import table data to DataFrame object.

        :param data: Table data as list of dictionary.
        :return: True/False.
        """
        if data is None:
            data = tuple()

        assert isinstance(data, (list, tuple)), u'Type error import data in component <%s>' % self.__class__.__name__

        try:
            self._dataframe = pandas.DataFrame(data)

            sum_by = self.getSumBy()
            if sum_by and len(sum_by) == 1:
                # Group by one column
                self._dataframe = self._dataframe.groupby(sum_by[0]).sum()
            elif sum_by:
                # Group by multiple column
                self._dataframe = self._dataframe.groupby(sum_by).sum()

            return True
        except:
            log_func.fatal(u'Error import data in <%s>' % self.getName())
            self._dataframe = None
        return False

    def exportDataToValues(self):
        """
        Export DataFrame object to table data as dict_values.

        :return: Table data as dict_values or None if error.
        """
        if isinstance(self._dataframe, pandas.DataFrame):
            try:
                return self._dataframe.T.to_dict().values()
            except:
                log_func.fatal(u'Export error DataFrame in <%s>' % self.getName())
        else:
            log_func.warning(u'Not define DataFrame object for export')
        return None

    def exportData(self):
        """
        Export DataFrame object to table data as list of dictionary.

        :return: Table data as list obj dictionary.
        """
        values = self.exportDataToValues()
        if values is not None:
            return list(values)
        return None

    def transform(self, dataframe=None):
        """
        Transform DataFrame object.

        :param dataframe: DataFrame object.
            If not defined then get current DataFrame object.
        :return: Transformed DataFrame object or None if error.
        """
        log_func.warning(u'not defined <transform> method in component <%s>' % self.__class__.__name__)
        return None

    def getSumBy(self):
        """
        Get total sum group column names.

        :return: Column names or empty list.
        """
        log_func.warning(u'Not define getSumBy in component <%s>' % self.__class__.__name__)
        return list()
