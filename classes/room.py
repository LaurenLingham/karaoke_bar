class Room:
    def __init__(self, name, price, capacity):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.head_count = 0
        self.song_list = []
        self.guests = []

    def add_song(self, song):
        self.song_list.append(song)

    def check_in_guest(self, guest):
        if self.head_count < self.capacity and guest.can_afford(self):
            self.head_count += 1
            self.guests.append(guest)
            guest.tab += self.price

    def check_out_guest(self, guest, bar):
        bar.balance += guest.tab
        guest.pay_tab()
        self.guests.remove(guest)
        self.head_count -= 1
