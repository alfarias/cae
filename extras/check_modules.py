# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:59:40 2018

@author: Avell
"""

import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)