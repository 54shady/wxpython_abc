#!/usr/bin/env python
import wx

# MyFrame derive from wx.Frame and overwrite its __init__ method
class MyFrame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(200,100))
        wx.TextCtrl(self, style=wx.TE_MULTILINE)

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

        # show myself
        self.Show(True)
    
    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "this is all about:)")
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        dlg = wx.MessageDialog(self, "Exiiiiiiiiiiiiit")
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpen(self,e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MyFrame("text editor")
app.MainLoop()
