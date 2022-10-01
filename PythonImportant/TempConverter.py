import tkinter
import tkinter.messagebox as box 

class FahrenConverterGUI:
    def __init__(self):
      
        self.main_window = tkinter.Tk()

        
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create widgets for the top frame
        
        #Pack the top frame's widgets
        
        #Create widgets for the bottom frame
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        
        #Pack the bottom frame's widgets
        self.quit_button.pack(side='left')
      
        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        
temp_converter = FahrenConverterGUI()
