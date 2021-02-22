

def register(name:str)->int:
    print(name)
    return 1111

class My:

    def __init__(self):
        self._dameon = False

    @property
    def dameon(self):
        return self._dameon

    @dameon.setter
    def dameon(self,value):
        self._dameon = value

a = My()
print(a.dameon)
a.dameon = True
print(a.dameon)


