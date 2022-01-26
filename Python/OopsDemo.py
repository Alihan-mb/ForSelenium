class Calculator:
    num = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as a method in class")

    def Summation(self):
        return self.a + self.b + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj.getData()
print(obj1.Summation())
