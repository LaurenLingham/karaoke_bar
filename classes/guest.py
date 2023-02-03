class Guest:
    def __init__(self, name, age, wallet, favourite_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.tab = 0
        
    def can_afford(self, item):
        return self.wallet >= item.price
    
    def buy_drink(self, drink):
        if self.age >=18 and self.can_afford(drink):
            self.tab += drink.price
    
    def pay_tab(self):
        self.wallet -= self.tab
        self.tab = 0

    def found_fav_song(self, songs):
        if self.favourite_song in songs:
            return("Yay! This is my favourite song!")