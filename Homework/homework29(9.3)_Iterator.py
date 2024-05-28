class EvenNumbers:
    def __init__(self, start=0, end=1):
        if start % 2 == 0:
            self.start = start - 2
        else:
            self.start = start - 1
        self.i = self.start
        self.end = end


    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        self.i += 2
        if self.i < self.end:
            return self.i
        else:
            raise StopIteration()


en = EvenNumbers(10, 25)
for i in en:
    print(i)
