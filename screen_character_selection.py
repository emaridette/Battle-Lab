import tkinter as tk

from characters import *

class Screen_CharacterSelection (tk.Frame, Character, CharacterRoster):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       # Save the CharacterRoster  
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''
        self.character_index = tk.StringVar()
        self.character_index.set(None)

        tk.Label(self, text = "Hit Points").grid(row = 0, column = 3, sticky = tk.W)
        tk.Label(self, text = "Dexterity").grid(row = 0, column = 4, sticky = tk.W)
        tk.Label(self, text = "Strength").grid(row = 0, column = 5, sticky = tk.W)

        value = 0
        i = 1
        for char in self.roster.character_list:
            tk.Radiobutton(self, text = char.name, value = value, variable = self.character_index).grid(row = i, column = 0)
            imageSmall = tk.PhotoImage(file="images/" + char.small_image)
            w= tk.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # It's odd.
            w.grid(row = i, column = 1)
            tk.Label(self, text = char.hit_points).grid(row = i, column = 3)
            tk.Label(self, text = char.dexterity).grid(row = i, column = 4)
            tk.Label(self, text = char.strength).grid(row = i, column = 5)
            i += 1
            value += 1

        tk.Button(self, text = "Character Selected!", command = self.selected_clicked, bg = "magenta", fg = "white").grid(row = 7, column = 5)
        
        
       
    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''         
        self.callback_on_selected(self.character_index.get())

# root = tk.Tk()
# root.title("Select your character!")
# root.geometry("380x450")
# app = Screen_CharacterSelection(root)
# root.mainloop()