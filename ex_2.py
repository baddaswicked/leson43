from random import randint

class Rand_iterator:
    def __init__(self,start,end,quantity):
        self.start = start
        self.end = end
        self.quantity = quantity

        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count+=1

        if self.count>self.quantity:
            raise StopIteration
        else:
            return randint(self.start,self.end)

my_iter=Rand_iterator(1,20,10)


for item in set(my_iter):
    print(item, end= " ")

