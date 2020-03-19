#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project manager module.
"""

import os
import os.path

from ..util import file_func
from ..util import log_func
from ..dialog import dlg_func
from ..util import py_func
from ..util import spc_func
from ..util import res_func
from ..util import exec_func
from ..util import global_func

from ..passport import passport
from .. import user
from .. import role
from .. import global_data

from . import spc

__version__ = (0, 0, 0, 1)


class iqProjectManager(object):
    """
    Project manager class.
    """
    def __init__(self, name=None):
        """
        Constructor.

        :param name: Project name.
        """
        self.name = name

    def setName(self, name):
        """
        Set name of actual project.

        :param name: Project name.
        :return:
        """
        self.name = name

    def create(self, name=None, parent=None):
        """
        Create new project.

        :param name: New project name.
            If None then open dialog for input.
        :param parent: Parent from.
        :return: True/False.
        """
        if name is None:
            name = dlg_func.getTextEntryDlg(parent=parent, title=u'PROJECT NAME',
                                            prompt_text=u'Enter the name of the project:', default_value='new_name')
        if name:
            prj_path = self.getPath(name)
            result = self.createPath(prj_path)
            if result:
                self.saveDefaultResource(prj_path, name)

                self.setName(name)
                return True
        return False

    def saveDefaultResource(self, prj_path=None, prj_name=None, rewrite=False):
        """
        Save default project resource.

        :param prj_path: Project path.
        :param prj_name: Project name.
        :param rewrite: Rewrite resource file if it exists?
        :return: True/False.
        """
        if not prj_path:
            log_func.warning(u'Not define project path for save default project path')
            return False

        if not os.path.exists(prj_path):
            if not self.createPath(prj_path):
                return False

        if not prj_name:
            prj_name = os.path.splitext(os.path.basename(prj_path))[0]

        try:
            prj_res_filename = os.path.join(prj_path, prj_name + res_func.RESOURCE_FILE_EXT)

            prj_resource = spc_func.clearResourceFromSpc(spc.SPC)
            prj_resource['name'] = prj_name
            prj_resource['description'] = u'Application project'

            user_resource = spc_func.clearResourceFromSpc(user.SPC)
            user_resource['name'] = 'admin'
            user_resource['description'] = u'Administrator'
            user_resource['roles'] = [role.ADMINISTRATORS_ROLE_NAME]

            role_resource = spc_func.clearResourceFromSpc(role.SPC)
            role_resource['name'] = role.ADMINISTRATORS_ROLE_NAME
            role_resource['description'] = u'Administrators'

            prj_resource[spc_func.CHILDREN_ATTR_NAME] = [user_resource, role_resource]

            return res_func.saveResourceText(prj_res_filename, prj_resource)
        except:
            log_func.fatal(u'Error save default project resource')
        return False

    def createPath(self, prj_path):
        """
        Create project directory.

        :param prj_path: Project directory path.
        :return: True/False.
        """
        if prj_path and os.path.exists(prj_path):
            log_func.warning(u'Project path <%s> exists' % prj_path)
        elif not prj_path:
            log_func.warning(u'Project path <%s> not defined' % prj_path)
        elif prj_path and not os.path.exists(prj_path):
            log_func.info(u'Create project package path <%s>' % prj_path)
            return py_func.createPackage(prj_path)
        return False

    def getPath(self, name=None):
        """
        Get project path by project name.

        :param name: Project name.
        :return: Full path to project or None if error.
        """
        if name is None:
            name = self.name

        framework_path = file_func.getFrameworkPath()
        if framework_path:
            if name:
                return os.path.join(framework_path, name)
            else:
                log_func.warning(u'Not define project name')
        return None

    def run(self, name=None):
        """
        Run project.

        :param name: Project name. If None run actual.
        :return: True/False.
        """
        if name:
            self.setName(name)

        cmd = '''#!/bin/sh

cd %s
python3 ./framework.py --debug --mode=runtime --engine=%s --prj=%s        
''' % (file_func.getFrameworkPath(), global_func.getEngineType(), name)
        return exec_func.runTask(cmd, run_filename=name)

    def debug(self, name=None):
        """
        Debug project.

        :param name: Project name. If None debug actual.
        :return: True/False.
        """
        if name:
            self.setName(name)

        pass

    def start(self, username=None, password=None):
        """
        Start project.

        :param username: User name.
        :param password: User password.
        :return: True/False.
        """
        user_psp = passport.iqPassport(prj=self.name, module=self.name,
                                       typename=user.COMPONENT_TYPE, name=username)
        log_func.debug(u'User passport <%s>' % user_psp.getAsStr())
        user_obj = self.getKernel().createObject(psp=user_psp, parent=self, register=True)

        global_data.setGlobal('USER', user_obj)

        # Login loop
        result = False
        for i in range(user.DEFAULT_LOGIN_LOOP_COUNT):
            result = user_obj.login(password)
            if result:
                break
        if not result:
            # If login failed then exit
            return result

        global_data.setGlobal('USER', user_obj if result else None)
        if result:
            user_obj.run()
        return result

    def stop(self):
        """
        Stop programm.

        :return: True/False
        """
        user_obj = global_data.getGlobal('USER')
        if user_obj:
            return user_obj.logout()
        return False
