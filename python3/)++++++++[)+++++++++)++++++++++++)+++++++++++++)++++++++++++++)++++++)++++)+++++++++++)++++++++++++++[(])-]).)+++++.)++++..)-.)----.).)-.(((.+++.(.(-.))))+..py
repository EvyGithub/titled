code = __file__.split("\\")[-1][:-3]
loopStack = []
overflow = True

index = 0

memory = [0] * 30000
memoryPointer = 0

while index < len(code):
    match code[index]:
        case "(":
            memoryPointer -= 1

        case ")":
            memoryPointer += 1

        case "+":
            memory[memoryPointer] += 1
            if memory[memoryPointer] > 255 and overflow:
                memory[memoryPointer] = 0

        case "-":
            memory[memoryPointer] -= 1
            if memory[memoryPointer] < 0 and overflow:
                memory[memoryPointer] = 255

        case ",": # input as char
            temp = input("input one character:\n> ").rstrip()[0]
            memory[memoryPointer] = temp

        case ";": # input as num
            try:
                temp = int(input("input a number:\n> ").strip())
            except:
                temp = 0

            memory[memoryPointer] = temp

        case ".": # output as char
            print(chr(memory[memoryPointer]), end="")

        case "'": # output as num
            print(memory[memoryPointer], end="")

        case "[":
            if memory[memoryPointer] == 0:
                # skip loop
                loopAmount = 1
                while loopAmount > 0:
                    index += 1
                    if code[index] == '[':
                        loopAmount += 1
                    elif code[index] == ']':
                        loopAmount -= 1
            else:
                # enter loop
                loopStack.append(index)

        case "]":
            if memory[memoryPointer] != 0:
                # go back to to the '['
                index = loopStack[-1]
            else:
                # exit
                loopStack.pop()    

        case "$":
            overflow = not overflow

    index += 1