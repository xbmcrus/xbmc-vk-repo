#!/usr/bin/python
# -*- coding: utf-8 -*-
# VK-XBMC add-on
# Copyright (C) 2011 Volodymyr Shcherban
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
__author__ = 'Volodymyr Shcherban'



import sys, xbmcaddon, xbmc, xbmcgui, xbmcplugin, urllib

from vkapp import GetApi

from xbmcvkui import XBMCVkUI_Base,HOME
from xvaudio import XVKAudio
from xvimage import XVKImage
from xvvideo import XVKVideo


handle = int(sys.argv[1])

api = GetApi()

class XBMC_VK_UI_Factory:
    def GetUI(self, param):
        #bloody hacks http://wiki.xbmc.org/index.php?title=Window_IDs
        id = xbmcgui.getCurrentWindowId()
        if id in (10006,10024,10025,10028):
            return XVKVideo(param, handle, api)
        elif id in (10005,10500,10501,10502):
            return XVKAudio(param, handle, api)
        elif id in (10002,):
            return XVKImage(param, handle, api)
        else:
            print "Invalid context: " + id


if api:
    params = {"mode" : HOME}
    if sys.argv[2]:
        l = [s.split("=") for s in sys.argv[2][1:].split("&")]
        l = map(lambda e: (e[0], urllib.unquote_plus(e[1])) , l)
        params.update(dict(l))

    ui = XBMC_VK_UI_Factory().GetUI(params)
    
else:
    listitem = xbmcgui.ListItem("-- something wrong, try again --")
    xbmcplugin.addDirectoryItem(handle, sys.argv[0], listitem, True)
    xbmc.output("THIS IS THE END")
