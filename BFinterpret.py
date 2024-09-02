
def BFintperpret(code, input_data=""):
    #initialisations
    tape = [0] * 30000  
    pointer = 0 
    code_pointer = 0 
    input_pointer = 0  
    output = ""  
    loop_stack = []  
    
    #instuction interpreter



bf_code = "" #edit here
decoded = BFintperpret(bf_code)
print(decoded)
    