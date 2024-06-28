class Count:
    def __init__(self,int_step):
        self.step = int_step

    def __call__(self, *args, **kwargs):
        inc, = args # args-> tuple (25, )
        self.step +=inc

count=Count(100)
count(25)
count(40)
print(count.step)
