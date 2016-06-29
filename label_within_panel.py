#!/usr/bin/env python
import wx

class ExamplePanle(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, label="You quote", pos=(20, 30))

        self.logger = wx.TextCtrl(self, pos=(300, 20), size=(200, 300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # button
        self.button = wx.Button(self, label="save", pos=(200, 325))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

    def OnClick(self, event):
        self.logger.AppendText("Click on the object with Id %d\n" % event.GetId())

app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanle(frame)
frame.Show()
app.MainLoop()
