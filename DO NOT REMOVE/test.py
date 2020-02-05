from tkinter import *
import time
import Database_Module

class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.statscounter = 0
        self.vUserStats = db.DbGetStats("Thomassmith")
        
    def create_widgets(self):
        self.entInput = Label(text = "Welcome to the game\n")
        self.entInput.place(x = 100, y = 10)
        self.entInput.config(font=("Courier", 20))

        self.btn1 = Button(text = "Stats", height = 2, width = 10, command = self.show_stats, relief = GROOVE,bg = "LavenderBlush2")
        self.btn1.place(x = 100, y = 400)
        self.btn1.config(font=("Courier", 12))

        self.btn2 = Button(text = "Start", height = 2, width = 10, relief = GROOVE,bg = "LavenderBlush2")
        self.btn2.place(x = 300, y = 400)
        self.btn2.config(font=("Courier", 12))

        self.StatsVar = StringVar()
        self.StatsVar.set("")

        self.lbl1 = Label(textvariable = self.StatsVar)
        self.lbl1.place(x= 20, y = 100)
        self.lbl1.config(font=("Courier", 12))

    def show_stats(self):
        if self.statscounter == 0:
            self.StatsVar.set("Health: " + self.vUserStats[0][0] + "\n\n\n\nStamina: " + self.vUserStats[0][1] + "\n\n\n\nExperience: " + self.vUserStats[0][2] + "\n\n\n\nLevel: " + self.vUserStats[0][3])
            self.statscounter = 1
        else:
            self.StatsVar.set("")
            self.statscounter = 0
            print(self.statscounter)
            
root = Tk()
root.title("Stat Test")
root.geometry("500x500")
db = Database_Module
app = Application(root)

root.mainloop()
