class Squares:
    def __init__(self,start,stop) -> None:
        self.value=start-1
        self.stop=stop
        print(self)
    def __iter__(self):
        return self
    def __next__(self):
        if self.value==self.stop:
            rasie StopIteration
        self.value+=1
        return self.value**2

if __name__=='__main__':
    for i in Squares(1,5):
        print(i,end=' ')
