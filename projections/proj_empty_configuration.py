import wx

class EmptyPanel(wx.Panel):
    
 
    def __init__(self, parent, title):
        wx.Window.__init__(self, parent)
        self.parent = parent
        wx.EVT_SIZE(self, self.OnSize)
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        lbl = wx.StaticText(self.panel, label="\n\n  " + str(title) + " has no parameters.")
        vbox.Add(lbl, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=25)

        
    def OnSize(self, event):
        self.panel.SetSize(self.GetSizeTuple())