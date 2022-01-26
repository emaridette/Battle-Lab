import tkinter as tk

class Screen_PrepareToBattle (tk.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)
        
        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        tk.Label(self, text = "You").grid(row = 0, column = 0)
        tk.Label(self, text = "Computer").grid(row = 0, column = 1)
        imageSmall = tk.PhotoImage(file="images/" + self.player1.large_image)
        w= tk.Label (self,
                    image = imageSmall, 
                        )
        w.photo = imageSmall # It's odd.
        w.grid(row = 1, column = 0)
        imageSmall = tk.PhotoImage(file="images/" + self.player2.large_image)
        w= tk.Label (self,
                    image = imageSmall, 
                        )
        w.photo = imageSmall # It's odd.
        w.grid(row = 1, column = 1)

        tk.Label(self, text = f"{self.player1.hit_points} HP").grid(row = 2, column = 0)
        tk.Label(self, text = f"{self.player1.dexterity} Dexterity").grid(row = 3, column = 0)
        tk.Label(self, text = f"{self.player1.strength} Strength").grid(row = 4, column = 0)
        tk.Label(self, text = f"{self.player2.hit_points} HP").grid(row = 2, column = 1)
        tk.Label(self, text = f"{self.player2.dexterity} Dexterity").grid(row = 3, column =1)
        tk.Label(self, text = f"{self.player2.strength} Strength").grid(row = 4, column =1)

        tk.Button(self, text = "Commence Battle!", command = self.commence_battle_clicked, bg = "magenta", fg = "white").grid(row = 5, column = 1, sticky = tk.E)

 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        