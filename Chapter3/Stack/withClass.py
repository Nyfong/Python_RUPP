class Stack:
    def __init__(self):
         self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
         self.stack.pop()
    
    def is_Empty(self):
          return True if len(self.stack) == 0 else False

object =  Stack()


object.push("1")
object.push( "2")
object.push("3")
print(object.stack)


object.pop()


print(object.stack)