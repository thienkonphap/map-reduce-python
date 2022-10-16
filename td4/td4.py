from abc import ABC, abstractmethod
import sys
print(sys.argv)

class Rope(ABC):
    def __init__(self,d):
        self.length = 0
    @abstractmethod
    def __getitem__(self,i):
        pass
    @abstractmethod
    def __add__(self,r):
        pass
    @abstractmethod
    def __str__(self):
        pass

class App(Rope): #Node with left and Right
    def __init__(self,left,right):
        self.left = left
        self.right = right
    def  __getitem__(self,i):
        if isinstance(i,int):
            if i <= self.left.size():
                return self.left.__getitem__(i)
            else:
                return self.right.__getitem__(i - self.left.size())
        elif isinstance(i, slice):
            if i.step is None:
                step = 1
            else:
                step = i.step
            if i.start is None:
                start = 0
            else:
                start = i.start
            if i.stop is None:
                stop = self.size()
            else:
                stop = i.stop
            if start < 0:
                start = self.size() + start
            if stop < 0:
                stop = self.size() + stop
            if start > stop:
                return ""
            if step > 0:
                if start >= self.left.size():
                    return self.right.__getitem__(
                        slice(start - self.left.size(), stop - self.left.size(), step)
                    )
                elif stop <= self.left.size():
                    return self.left.__getitem__(slice(start, stop, step))
                else:
                    return self.left.__getitem__(
                        slice(start, self.left.size(), step)
                    ) + self.right.__getitem__(slice(0, stop - self.left.size(), step))
            else:
                if start >= self.left.size():
                    return self.right.__getitem__(
                        slice(start - self.left.size(), stop - self.left.size(), step)
                    )
                elif stop <= self.left.size():
                    return self.left.__getitem__(slice(start, stop, step))
                else:
                    return self.right.__getitem__(
                        slice(self.right.size() - 1, self.right.size() - stop - 1, step)
                    ) + self.left.__getitem__(
                        slice(self.left.size() - 1, self.left.size() - start - 1, step)
                    )
           
    def __add__(self,r):
        res = self.get_last_right()
        if res.size() + r.size() <10:
            res+=r
            return self
        else:
            return App(self,r)

    def __str__(self):
        return self.left.__str__() + self.right.__str__()
    def size(self):
        return self.left.size()+self.right.size()
    def get_last_right(self):
        if isinstance(self.right,App):
            return self.get_last_right(self.right)
        else:
            return self
# OK
class Str(Rope): #Node with a string
    def __init__(self,s):
        self.s = s
    def __getitem__(self,i):
        return self.s[i]
    def __add__(self,r):
        if self.size() + r.size() <10:
            return Str(self.s+r.s)
        else:
            return App(self,r)
    def __str__(self):
        return self.s
    def size(self):
        return len(self.s)

r = App(Str('La structure de'), App(App(Str('corde per'),Str('met de manipuler')), App(Str(' de grandes '),Str('chaînes'))))
print(r)
print(r[6])
print( r[16])
print((r[21:54]))
assert(str(r) == "La structure decorde permet de manipuler de grandes chaînes")

assert(str(Str("chai") + Str("ne")) == "chaine")
assert(str((Str("debut de la ") + Str("chai") + Str("ne"))) == "debut de la chaine")