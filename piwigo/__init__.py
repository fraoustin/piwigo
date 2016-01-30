#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Module piwigo
"""

from piwigo.ws import Piwigo, WsNotExistException, WsErrorException, WsPiwigoException 

__version_info__ = (1, 0, 1)
__version__ = '.'.join([str(val) for val in  __version_info__])
