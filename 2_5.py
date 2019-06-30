
class Bag(set):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.a = set()
        #self.add_all(iterable)

    def add_all(self, a):
        for x in a:
            self.add(x)

    # def add(self, x):

    # def remove(self):

    # def find(self,x):

    # def findAll(x):



bag = Bag([1, 2, 3, 4, 5])
print(bag)
