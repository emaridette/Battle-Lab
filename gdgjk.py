import tkinter as tk

class Screen_CharacterSelection(tk.Frame):

    def __init__ (self, master):
        super().__init__(master)
        self.cool = 10
        self.grid()
        self.hi()

    def hi(self):
    
        tk.Label(self, text = "Hit Points").grid(row = 0, column = 3)
        tk.Label(self, text = "Dexterity").grid(row = 0, column = 4)
        tk.Label(self, text = "Strength").grid(row = 0, column = 5)

root = tk.Tk()
root.title("Select your character!")
root.geometry("280x250")
app = Screen_CharacterSelection(root)
root.mainloop()
