
def BFintperpret(code, input_data=""):
    #initialisations
    tape = [0] * 30000  
    pointer = 0 
    code_pointer = 0 
    input_pointer = 0  
    output = ""  
    loop_stack = []  
    
    #instuction interpreter for +,><[]-
    while code_pointer < len(code):
        command = code[code_pointer]
        
        if command == '>':
            pointer += 1 
        elif command == '<':
            pointer -= 1  
        elif command == '+':
            tape[pointer] = (tape[pointer] + 1) % 256  
        elif command == '-':
            tape[pointer] = (tape[pointer] - 1) % 256  
        elif command == '.':
            output += chr(tape[pointer])  
        elif command == ',':
            if input_pointer < len(input_data):
                tape[pointer] = ord(input_data[input_pointer])  
                input_pointer += 1
        elif command == '[':
            if tape[pointer] == 0:
                open_loops = 1
                while open_loops > 0:
                    code_pointer += 1
                    if code[code_pointer] == '[':
                        open_loops += 1
                    elif code[code_pointer] == ']':
                        open_loops -= 1
            else:
                loop_stack.append(code_pointer)  
        elif command == ']':
            if tape[pointer] != 0:
                code_pointer = loop_stack[-1]  
            else:
                loop_stack.pop()  

        code_pointer += 1  

    return output



bf_code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++." #edit here
decoded = BFintperpret(bf_code)
print(decoded)
    