stack = []

def push(stack, item):
    stack.append(item)
def pop():
    stack.pop()
for i in range(3):
    push(stack,i)
print(stack)
for i in range(2):
    pop()
print(stack)