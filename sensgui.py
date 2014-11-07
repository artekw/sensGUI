__author__ = 'artek'
__appname__ = 'sensGUI'
__version__ = 'v0.1'

import wx

app = wx.App()

frame = wx.Frame(None, -1, "%s %s" % (__appname__, __version__))
frame.Show()

app.MainLoop()