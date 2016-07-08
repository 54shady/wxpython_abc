#!/usr/bin/evn python

import wx

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="MyForm")

        # Add a panel so it looks correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
        titleIcon = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)
        title = wx.StaticText(self.panel, wx.ID_ANY, "My Title")

        # top sizer
        topSizer = wx.BoxSizer(wx.VERTICAL)

        # sub sizer which will be add to top sizer
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        titleSizer.Add(titleIcon, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)

        # add titleSizer to topSizer
        topSizer.Add(titleSizer, 0, wx.CENTER)

        # set topSizer
        self.panel.SetSizer(topSizer)
        #topSizer.Fit(self)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
