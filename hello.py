#!/usr/bin/env python
import wx

app = wx.App(False)
father = wx.Frame(None, wx.ID_ANY, "father_frame")
child = wx.Frame(father, wx.ID_ANY, "child_frame")
child.Show(True)
father.Show(True)
app.MainLoop()
