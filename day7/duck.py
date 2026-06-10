class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")

class horse:
    def walk(self):
        print("tabak tabak tabak tabak")

def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=horse()
myfunction(h)                   