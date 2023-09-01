class MinStack:

    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
    

def use_min_stack(instructions: list, input: list):
    output = []
    for i in range(len(instructions)):
        if instructions[i] == 'MinStack':
            obj = MinStack()
            output.append(None)
        elif instructions[i] == 'push':
            obj.push(input[i])
            output.append(None)
        elif instructions[i] == 'pop':
            obj.pop()
            output.append(None)
        elif instructions[i] == 'top':
            output.append(obj.top()[0])
        elif instructions[i] == 'getMin':
            output.append(obj.getMin()[0])
    
    return output


# input1 = ["MinStack","push","push","push","getMin","pop","top","getMin"]
# input2 = [[],[-2],[0],[-3],[],[],[],[]]
# excepted = [None,None,None,None,-3,None,0,-2]

# print(use_min_stack(input1, input2) == excepted)
# print(use_min_stack(input1, input2))
# print(excepted)