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
        # add a grid sizer
        rows = 4
        cols = 5
        gs = wx.GridSizer(rows, cols)
        gs.AddMany([
            (wx.Button(self, -1, 'A'), 0, wx.EXPAND),
            (wx.Button(self, -1, 'B'), 0, wx.EXPAND),
            (wx.Button(self, -1, 'C'), 0, wx.EXPAND),
            (wx.Button(self, -1, 'D'), 0, wx.EXPAND),
            (wx.Button(self, -1, '1'), 0, wx.EXPAND),
            (wx.Button(self, -1, '2'), 0, wx.EXPAND),
            (wx.Button(self, -1, '3'), 0, wx.EXPAND),
            (wx.Button(self, -1, '4'), 0, wx.EXPAND),
            (wx.Button(self, -1, '5'), 0, wx.EXPAND),
            (wx.Button(self, -1, '6'), 0, wx.EXPAND),
            (wx.Button(self, -1, '7'), 0, wx.EXPAND),
            (wx.Button(self, -1, '8'), 0, wx.EXPAND),
            (wx.Button(self, -1, '9'), 0, wx.EXPAND),
            (wx.Button(self, -1, '10'), 0, wx.EXPAND),
            (wx.Button(self, -1, '11'), 0, wx.EXPAND),
            (wx.Button(self, -1, '12'), 0, wx.EXPAND),
            (wx.Button(self, -1, '13'), 0, wx.EXPAND),
            (wx.Button(self, -1, '14'), 0, wx.EXPAND),
            (wx.Button(self, -1, '15'), 0, wx.EXPAND),
            (wx.Button(self, -1, '16'), 0, wx.EXPAND)
            ])

        mySizer.Add(gs, 1, wx.EXPAND)

        self.SetSizer(mySizer)


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'my frame skeleton')
        frame.Show(True)
        return True

app = MyApp(False)
app.MainLoop()
