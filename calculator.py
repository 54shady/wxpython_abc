#!/usr/bin/python
# https://wiki.wxpython.org/AnotherTutorial

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(300, 240))

        # add a textctrl
        self.myTextCtrl = wx.TextCtrl(self, -1, '', style = wx.TE_RIGHT)

        # add a sizer
        mySizer = wx.BoxSizer(wx.VERTICAL)
        mySizer.Add(self.myTextCtrl, 0, wx.EXPAND | wx.TOP | wx.BOTTOM)
        self.SetSizer(mySizer)


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'my frame skeleton')
        frame.Show(True)
        return True

app = MyApp(False)
app.MainLoop()
