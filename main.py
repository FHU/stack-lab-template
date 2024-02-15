import stack

tower = stack.Stack()
tower.push("I")
tower.push("T")
tower.push("R")
tower.push("Y")

tower.pop()
print(tower.blocks)

deck = stack.Stack()


'''stack = []

def push(item):
    stack.append(item)

def pop():
    del stack[-1]

push(1)
push(2)
push(3)

pop()

print(stack)'''