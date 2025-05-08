# Marina Rizk - ID#308238
# MSCS2202 - Assignment #5.2
# module5_mod.py

class ListReader:
    def __init__(self):
        self.list = []

    def ListAppend(self, addedNu):
        self.list.append(addedNu)

    def InputPos(self, Input):
        if Input in self.list:
            return(self.list.index(Input) + 1)
        else:
            return(-1)
