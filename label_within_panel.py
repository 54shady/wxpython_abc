#!/usr/bin/env python
import wx

# MyFrame id derive from wx Frame
class MyFrame(wx.Frame):
    def __init__(self, p):
        wx.Frame.__init__(self, p)
        panel = wx.Panel(self)
        wx.StaticText(panel, label="You quote", pos=(20, 30))
        self.Show()

app = wx.App(False)
MyFrame(None)
app.MainLoop()
