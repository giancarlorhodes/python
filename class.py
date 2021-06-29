
class myFirstClass():
    var1 = 0

    def method1(self):
        print("myFirstClass method1")

    def method2(self, x):
        print("myFirstClass method2", x)

    def method3(self):
        print(self.var1)



def main():
    c = myFirstClass()
    c.method1()
    c.method2(10000)
    c.var1 = 100
    c.method3()


if __name__ == "__main__":
   main()