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
        file.AppendSeparator()

        # make a quit item and add to file menu
        quit = wx.MenuItem(file, 105, 'Quit', 'Quit the Application')
        quit.SetBitmap(wx.Image('stock_exit_24.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        file.AppendItem(quit)

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
        frame.Center()
        frame.Show(True)
        return True

app = MyApp(False)
app.MainLoop()
