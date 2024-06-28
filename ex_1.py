class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index+=1
        return value

my_iterator=MyIterator([1,2,3,4,5,6])
for item in my_iterator:
    print(item)

print("="*10)

def my_gen(data):
    for item in data:
        yield item

my_generator=my_gen([1,2,3,4,5,6])
for item in my_generator:
    print(item)