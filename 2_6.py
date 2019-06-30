class SSet(set):

    def sset_find(self,x):
        for number in self:
            if x <= number:
                print(number)
                break
            else:
                return None

#setの中身をfor文で回して

sset = SSet([3,4,6,6,2,1])
print(sset.sset_find(10))