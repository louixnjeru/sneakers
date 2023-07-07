import wx

class MainScreen(wx.Frame):
    
    def __init__(self,parent,title):
        super(MainScreen,self).__init__(parent, title=title, size=(480,800), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Centre()
        

def main():
    app = wx.App()
    frame = MainScreen(None,title='Sneaker')
    frame.Show()
    app.MainLoop()
    
if __name__ == "__main__":
    main()