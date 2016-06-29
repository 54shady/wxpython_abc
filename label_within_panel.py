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

        # edit control
        wx.StaticText(self, label="YourName :", pos=(20, 60))
        self. editname = wx.TextCtrl(self, value="Enter here your name", pos=(150, 60), size=(140, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)

        # checkbox
        self.insure = wx.CheckBox(self, label="What't your want:)", pos=(20, 180))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

    def OnClick(self, event):
        self.logger.AppendText("Click on the object with Id %d\n" % event.GetId())
    def EvtText(self, event):
        self.logger.AppendText("EvtText %s\n" % event.GetString())
    def EvtCheckBox(self, event):
        self.logger.AppendText("EvtCheckBox %s\n" % event.Checked())

app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanle(frame)
frame.Show()
app.MainLoop()
