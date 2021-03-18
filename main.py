import tkinter as tk

X_1 = 0

class Application( tk.Frame ):
    def __init__(self, master=None):
        super().__init__( master )
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button( self )
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack( side="top" )

        self.do_something = tk.Button( self, text="Something else\nyeeeee", fg="green" , command=self.do_something)
        self.do_something.pack(side="left")

        self.quit = tk.Button( self, text="QUIT", fg="red",
                               command=self.master.destroy )
        self.quit.pack( side="bottom" )

    def say_hi(self):
        print( "hi there, everyone!" )

    def do_something(self):
        global X_1
        X_1 += 1

        print(X_1)


root = tk.Tk()
app = Application( master=root )
app.mainloop()
