class MyRange:
    def __init__(self, start, stop=None, step=1):
        # range(N) 형식으로 쓰인 경우
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        self.data = []

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.start >= self.stop)\
            or (self.step < 0 and self.start <= self.stop):
            raise StopIteration
        curr = self.start
        self.data.append(curr)
        self.start += self.step
        return curr

for i in MyRange(3):
    for j in MyRange(10, 0, -3):
        print(i, j)