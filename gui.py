#! /usr/bin/env python
from Tkinter import *
import tkFileDialog
import tkMessageBox

class GUIFramework(Frame):
    """This is the GUI"""
    
    def __init__(self,master=None):
        """Initialize yourself"""
        
        """Initialise the base class"""
        Frame.__init__(self,master)
        
        """Set the Window Title"""
        self.master.title("Mapa de Materias GUI")
        
        """Display the main window"
        with a little bit of padding"""
        self.grid(padx=10,pady=10)
        self.CreateWidgets()
       
    def CreateWidgets(self):
        """Create all the widgets that we need"""
                
        """Create the Text"""
        self.lbText = Label(self, text="Plan de materias:")
        self.lbText.grid(row=0, column=0)
        
        """Create the Entry, set it to be a bit wider"""
        self.enText = Entry(self)
        self.enText.grid(row=0, column=1, columnspan=3)
        
        #~ self.boton0 = Button(self, text="Abrir...", command=
        
        self.browse0 = tkFileDialog.askopenfile(parent=self,mode="r",title="Seleccionar plan de materias...")
        
        self.lbText1 = Label(self, text="Tu nombre:")
        self.lbText1.grid(row=1, column=0)
        
        self.enText1 = Entry(self)
        self.enText1.grid(row=1, column=1, columnspan=3)
        
        """Create the Button, set the text and the 
        command that will be called when the button is clicked"""
        self.btnDisplay = Button(self, text="Display!", command=self.Display)
        self.btnDisplay.grid(row=2, column=2)
        
    def Display(self):
        """Called when btnDisplay is clicked, displays the contents of self.enText"""
        tkMessageBox.showinfo("Text", "You typed: %s" % self.enText.get())    
                
if __name__ == "__main__":
    guiFrame = GUIFramework()
    guiFrame.mainloop()
