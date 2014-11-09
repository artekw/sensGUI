#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'artek'
__appname__ = 'sensGUI'
__version__ = 'v0.1'

import wx

class sensorTabPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        '''
        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)

        self.SetSizer(sizer)
        '''

class controlTabPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        '''
        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)

        self.SetSizer(sizer)
        '''

class infoTabPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        '''
        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)

        self.SetSizer(sizer)
        '''

class Tabs(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=
                             wx.BK_DEFAULT
                             #wx.BK_TOP
                             #wx.BK_BOTTOM
                             #wx.BK_LEFT
                             #wx.BK_RIGHT
                             )
        sensTab = sensorTabPanel(self)
        self.AddPage(sensTab, "Czujniki")

        controlTab = controlTabPanel(self)
        self.AddPage(controlTab, "Sterowanie")

        controlTab = infoTabPanel(self)
        self.AddPage(controlTab, "Informacje")

class Start(wx.Frame):

    def __init__(self, parent, title):
        super(Start, self).__init__(parent, title=title, size=(500, 400))

        self.InitUI()
        self.Centre()
        self.Show()


    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Wyjście', 'Zamknij aplikację')
        menubar.Append(fileMenu, '&Plik')
        menubar.Append(fileMenu, '&Pomoc')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        panel = wx.Panel(self)
        tabs = Tabs(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(tabs, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        # self.Layout()

    def OnQuit(self, e):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    title = "%s %s" % (__appname__, __version__)
    Start(None, title=title)
    app.MainLoop()