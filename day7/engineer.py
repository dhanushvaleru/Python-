class Engineer:
    def __init__(self):
        pass
    def work(self):
        print("Engineer is working...!")
class softwareEnginner(Engineer):
    def __init__(self):
        super().__init__()
    def work(self):
        print("Software Engineer is working")
el=Engineer()
el.work()
s1=softwareEnginner()
s1.work()                    