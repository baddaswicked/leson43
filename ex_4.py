class Test:
    def double(self,x):
        print("mul on 2")
        return x*2

    @classmethod
    def triple(cls,x):
        print("mul on 3")
        return x*3

    @staticmethod
    def quad(x):
        print("mul on 4")
        return x*4

test_object=Test()
print("--Виклик через екземляр класу--")
print(test_object.double(4))
print(test_object.triple(4))
print(test_object.quad(4))

print("--Виклик через клас--")
# print(Test.double(10))
print(Test.triple(10))
print(Test.quad(10))

