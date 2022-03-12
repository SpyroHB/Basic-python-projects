class Robot:
    def __init__(self,name=str,id=int,type=str) -> None:
        self.id = id
        self.name = name
        self.type = type
    
    def get_id(self):
        return self.id
    
    
    def get_type(self):
        return self.type
        


class BotProgram:
    def __init__(self,name=str,max_bots=int) -> None:
        self.name = name
        self.max_bots = max_bots
        self.bots = []

    
    def introduceSelf(self):
        return self.name,self.max_bots
    
    
    
    def add_bot(self,bot):
        if len(self.bots) < self.max_bots:
            self.bots.append(bot)
            return True
        return False
        





p1 = BotProgram('Dsicord bots',3)
r1 = Robot('SpyroBot','34568745645490','Admin')


print(p1.add_bot(r1))