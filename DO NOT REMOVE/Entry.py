from tkinter import *
import Database_Module as Db
import game_launch as Main

class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.entInput = Label(text = "Welcome to the game\n")
        self.entInput.grid(row = 0, column = 1, sticky = E +  W)
        self.entInput.config(font=("Courier", 20))

        self.lbl1 = Label(text = "Username:\n")
        self.lbl1.grid(row = 1, column = 0, sticky = W)
        self.lbl1.config(font=("Courier", 10))

        self.lbl2 = Label(text = "Password:\n")
        self.lbl2.grid(row = 2, column = 0, sticky = W)
        self.lbl2.config(font=("Courier", 10))

        self.vUsername = StringVar()
        self.userlogin = Entry(textvariable = self.vUsername)
        self.userlogin.grid(row = 1, column = 1)

        self.vPassword = StringVar()
        self.userPass = Entry(textvariable = self.vPassword)
        self.userPass.grid(row = 2, column = 1)

        self.subbtn = Button(text = "Submit", command = self.checkpass)
        self.subbtn.grid(row = 3, column = 1, sticky = W+E)

    def checkpass(self):
        if database.PassCheck(self.userlogin.get(), self.userPass.get()):
            Main.start_game()
 
# main
root = Tk()
root.title("User Input")
root.geometry("425x170")
database = Db
app = Application(root)
root.mainloop()
