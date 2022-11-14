class Card:
    def __init__(self, hash:str,id:int,icon:str,cost:int, name:str, type:str, arena:int, rarity:str):
        self.id = id
        self.hash = hash
        self.icon = icon
        self.cost = cost
        self.name = name
        self.type = type
        self.arena = arena
        self.rarity = rarity


