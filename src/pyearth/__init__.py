'''
Created on Dec 21, 2023

@author: chenxuhe
'''
from .earth import Earth
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
