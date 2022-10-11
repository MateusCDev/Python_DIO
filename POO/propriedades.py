class Foo:
    def __init__(self, x= None) -> None:
        self._x = x
    
    @property # para retornar valor 
    def x(self):
        return self._x or 0

    @x.setter # metodo vira propriedade no setter posso atribuir um valor
    def x(self, value):
         self._x += value

    @x.deleter  # para deletar e não tirar ele da memoria e passa 0 na variavel   
    def x(self):
        self._x = 0

foo = Foo(10)
print(foo.x)  
foo.x = 10
print(foo.x)    
del foo.x  
print(foo.x)