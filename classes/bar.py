class Bar:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)
