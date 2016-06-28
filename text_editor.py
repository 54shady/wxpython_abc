#!/usr/bin/env python
import os
import wx

# MyFrame derive from wx.Frame and overwrite its __init__ method
class MyFrame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(200,100))
        self.myTextCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        # statusbar in the bottom of the window
        self.CreateStatusBar()

        # setting up the menu
        myMenu = wx.Menu()
        menuItemOpen = myMenu.Append(wx.ID_OPEN, "open", "open")
        myMenu.AppendSeparator()
        menuItemAbout = myMenu.Append(wx.ID_ABOUT, "about", "about Info")
        myMenu.AppendSeparator()
        menuItemExit = myMenu.Append(wx.ID_EXIT, "exit", "exit Info")
        # Set events
        self.Bind(wx.EVT_MENU, self.OnOpen, menuItemOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItemAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuItemExit)

        # menu bar
        menuBar = wx.MenuBar()
        # add menu to the menu bar
        menuBar.Append(myMenu, "File")

        self.SetMenuBar(menuBar)

        # sizer
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.myTextCtrl, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        # show myself
        self.Show(True)
    
    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "aaaa", "bbbbb", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        dlg = wx.MessageDialog(self, "Exiiiit")
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpen(self, e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.myTextCtrl.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MyFrame("text editor")
app.MainLoop()
