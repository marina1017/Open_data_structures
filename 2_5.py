
class Bag(set):
    #ハッシュテーブルにものの名前を入れると、個数が帰ってくるようにする
    dic = {}


    def __init__(self, iterable=[]):
        self.add_all(iterable)


    def add_all(self, a):
        for x in a:
            self.add(x)
            self.dic[x] = 1

    def bag_add(self, x):
        #セットにあどする
        self.add(x)
        #すでに存在するのであれば、１追加する
        if x in self.dic:
            self.dic[x] = self.dic[x] + 1
        #ハッシュテーブルに存在してなければ、新しく辞書の要素をつくって１をいれる
        else:
            self.dic[x] = 1
        print(self.dic)


    def bag_remove(self,x):
        #セットからリムーブする
        self.remove(x)
        #ハッシュテーブルから消す
        del self.dic[x]
        print(self.dic)
        print(self)


    def bag_find(self,x):
        if x in self.dic:
            return x
        else:
            return None

    def bag_findAll(self,x):
        #存在確認をする
        if x in self.dic:
            return [x for i in range(self.dic[x])]
        else:
            return None


bag = Bag([1, 2, 3, 4, 5])
print(bag)
bag.bag_add(6)
bag.bag_add(6)
bag.bag_remove(1)
print("bag.bag_find(3)",bag.bag_find(10))
print("bag.bag_findAll(6)",bag.bag_findAll(6))


