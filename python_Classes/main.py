import datetime as t


class Robot:
    def __init__(self,name,color,weight,createdAt,creator,mainServer,currentTime) -> None:
        self.name = name
        self.color = color
        self.weight = weight
        self.createdAt = createdAt
        self.creator = creator
        self.mainServer = mainServer
        self.currentTime = currentTime
    
    def introduceSelf(self):
        print(f'''
    Hello I'm {self.color} Robot.

    My name is {self.name}.
                    
    My virtual weight is {self.weight}.

    Created At: {self.createdAt}

    My Creator is {self.creator}

    Main Server is {self.mainServer}

    Current Time local time: {self.currentTime}.
    ''')
    





r1 = Robot('SpyroBot','Blue','43Kg','2020/03/11','SpyroDev_',None,t.datetime.now())
r1.introduceSelf()
