class Parent():
    def _init_ ( self):
        self.value = "Inside Parent"
def show( self):
        print( self.value)
class Child( Parent):
    def _init_ ( self):
        self.value = "Inside Child"
    def show( self): 
        print( self.value)
objl=Parent()
obj2=Child()
obj1.show()
obj2.show()
