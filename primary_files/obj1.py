class Student():
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def changeID(self, id):
        self.id = id

    def print(self):
        print("Your name is {} and your ID is {}".format(self.name, self.id))

krish = Student("Krish", 927)

krish.print()

krish.changeID(933)

krish.print()


