class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old")

    def sound(self):
        print("meow")


class dog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def info(self):
        print (f"I am a dog. My name is {self.name}. I am {self.age} years old")

    def sound(self):
        print("bark")
    

obj1 = cat("luna",2)
obj2 = dog("sam",3)

for i in [obj1,obj2]:
    i.info()
    i.sound()