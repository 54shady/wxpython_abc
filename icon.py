#!/usr/bin/python

import wx

def main():
    app = wx.App()

    frame = wx.Frame(None, title = 'MyIconApp', pos = (350, 300))
    # icon.ico is located in current directory
    frame.SetIcon(wx.Icon('icon.ico', wx.BITMAP_TYPE_ICON))
    # frame.Center()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
