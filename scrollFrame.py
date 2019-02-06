import sys
if sys.version[0] == '2':
    import Tkinter as tk
else:
    import tkinter as tk

# ************************
# Scrollable Frame Class
# ************************
class ScrollFrame(tk.Frame):
    '''
    
    '''
    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

        self.canvas = tk.Canvas(self, height = 720, borderwidth=0)          #place canvas on self
        self.viewPort = tk.Frame(self.canvas)                    #place a frame on the canvas, this frame will hold the child widgets 
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.

    def onFrameConfigure(self, event):                                              
        '''
        Reset the scroll region to encompass the inner frame
        '''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                #whenever the size of the frame changes, alter the scroll region respectively.
