import tkinter as tk
from characters import *

class Screen_Battle (tk.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        self.attack = tk.Button(self, text = "Attack", command = self.attack_clicked)
        self.attack.grid(row = 0)
        self.message = tk.Label(self)
        self.message["text"] = " "
        self.message.grid(row = 0, column = 1)

        tk.Label(self, text = "You").grid(row = 2, column = 0)
        tk.Label(self, text = "Computer").grid(row = 2, column = 1)

        imageSmall = tk.PhotoImage(file="images/" + self.player1.large_image)
        w= tk.Label (self,
                    image = imageSmall, 
                        )
        w.photo = imageSmall # It's odd.
        w.grid(row = 3, column = 0)
        imageSmall = tk.PhotoImage(file="images/" + self.player2.large_image)
        w= tk.Label (self,
                    image = imageSmall, 
                        )
        w.photo = imageSmall # It's odd.
        w.grid(row = 3, column = 1)
        
        self.hp1 = tk.Label(self, text = f"{self.player1.hit_points}/{self.player1_max_hp} HP")
        self.hp1.grid(row = 4, column = 0)
        self.hp2 = tk.Label(self, text = f"{self.player2.hit_points}/{self.player2_max_hp} HP")
        self.hp2.grid(row = 4, column = 1)
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''  
        self.result1 = self.player1.attack(self.player2)      
        if self.player2.hit_points > 0:
            self.result2 = self.player2.attack(self.player1)

        self.message["text"] = f"{self.result1}\n{self.result2}"
        self.hp1["text"] = f"{self.player1.hit_points}/{self.player1_max_hp} HP"
        self.hp2["text"] = f"{self.player2.hit_points}/{self.player2_max_hp} HP"
              
        if self.player1.hit_points <= 0 or self.player2.hit_points <= 0:
            if self.player1.hit_points > 0:
                self.message["text"] = f"{self.result1}\n{self.result2}\n{self.player1.name} is victorious!"
            else:
                self.message["text"] = f"{self.result1}\n{self.result2}\n{self.player2.name} is victorious!"
            self.attack.destroy()
            tk.Button(self, text = "Exit", command = self.exit_clicked).grid(row = 0)
        
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
            