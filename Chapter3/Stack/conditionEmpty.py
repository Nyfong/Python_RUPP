stack = []

def push(stack, item):
    stack.append(item)
def pop():
    stack.pop()
    
def is_Empty(stack):
   return True if len(stack) == 0 else False
    
for i in range(3):
    push(stack,i)
print(stack)
for i in range(2):
    pop()
print(stack)

print(is_Empty(stack))
