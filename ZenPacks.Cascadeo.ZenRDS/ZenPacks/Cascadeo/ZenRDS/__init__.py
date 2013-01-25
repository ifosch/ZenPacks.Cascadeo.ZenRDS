#### Copyright (C) 2012-2013 Cascadeo Corporation
####
#### THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS 
#### CREATIVE COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS 
#### PROTECTED BY COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF 
#### THE WORK OTHER THAN AS AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT 
#### LAW IS PROHIBITED.
####
#### BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT 
#### AND AGREE TO BE BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT 
#### THIS LICENSE MAY BE CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS 
#### YOU THE RIGHTS CONTAINED HERE IN CONSIDERATION OF YOUR ACCEPTANCE 
#### OF SUCH TERMS AND CONDITIONS.
####
#### Please see LICENSE for full legal details and the following URL
#### for a human-readable explanation:
####
#### http://creativecommons.org/licenses/by-nc-sa/3.0/us/
####

import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

from Products.ZenModel.ZenPack import ZenPackBase

class ZenPack(ZenPackBase):
    """
    ZenPacks.Cascadeo.ZenRDS ZenPack loader.
    """

    packZProperties = [
            ('zRDSIdentity', '', 'password'),
            ('zRDSKey', '', 'password'),
            ('zRDSInstance', '', 'string'),
	    ('zRDSRegion', 'us-east-1', 'string'),
            ]

