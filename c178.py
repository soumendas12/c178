from tkinter import *
import random
root = Tk()
root.geometry("500x500")
root.title("Colour Game")

label = Label(root, font=("Gigi",50,"bold"))
label.place(relx=0.5,rely=0.3,anchor=CENTER)

label_s = Label(root, text="Score: 0", font=("Gigi",15), fg ="blue")
label_s.place(relx=0.1, rely=0.1, anchor=CENTER)

input_value = Entry(root)
input_value.place(relx=0.5,rely=0.5,anchor=CENTER)

class game:
    def __init__(self):
        score = 0
        self.__score = score
    def updateGame(self):
        colours=["Red","Blue","Green","Yellow","Crimson","Purple","Pink"]
        self.text = colours
        self.colour= ["red","blue","green","yellow","crimson","purple","pink"]
        self.random_number_for_text = random.randint(0, 6)
        self.random_number_for_colour = random.randint(0, 6)
        label["text"] = self.text[self.random_number_for_text]
        label["fg"] = self.colour[self.random_number_for_colour]
    def __updateScore(self, input_value):
        if(input_value == self.colour[self.random_number_for_colour]):
            self.__score = self.__score + random.randint(0,10)
            label_s["text"] = "Score : " + str(self.__score)
    def get_user_value(self, input_value):
        self.__updateScore()
        
obj = game()

def getInput():
    input_value.get()
    obj.get_user_value(value)
    input_value.delete(0, END)
    
btn = Button(root, text = "Start", command = obj.updateGame, bg = "green", fg = "yellow", relief=FLAT,font=("Gigi",20))
btn.place(relx=0.7,rely=0.7)

btn1 = Button(root, text="Check", command=getInput, bg = "green", fg = "yellow", relief=FLAT,font=("Gigi",20)) 
btn1.place(relx=0.3,rely=0.7)
root.mainloop()