#!/usr/bin/python

import wx

class MyMenu(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(200, 100))

        # menubar
        menubar = wx.MenuBar()

        # menus
        file = wx.Menu()
        edit = wx.Menu()
        help = wx.Menu()

        # add some item to the menu
        file.Append(101, 'Open', 'Open a new document')
        file.Append(102, 'Save', 'Save the document')

        # add menus to the menubar
        menubar.Append(file, 'File')
        menubar.Append(edit, 'Edit')
        menubar.Append(help, 'Help')

        # set the menubar to the frame
        self.SetMenuBar(menubar)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyMenu(None, wx.ID_ANY, "menu1.py")
        frame.SetIcon(wx.Icon('icon.ico', wx.BITMAP_TYPE_ICON))
        frame.Show(True)
        return True

app = MyApp(False)
app.MainLoop()
