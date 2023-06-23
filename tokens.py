tokens = [
    "ADD",
    "SUBTRACT",
    "MULTIPLY",
    "DIVIDE",
    "IF",
    "ELSE",
    "WHILE",
    "PRINT",
    "OPEN",
    "CALC",
    "INPUT",
    "LOOP"
]

r_vars = {}

def INPUT(r):
    line = input()
    r_vars[r] = line
    
def PRINT(line):
    complete_line = ""
    for l in line:
        if l[0] == "$":
            #print(r_vars[l[1:]])
            complete_line += str(r_vars[l[1:]])
        else:
            complete_line += str(l)
    print(complete_line)
        
def ADD(numbers):
    num = list()
    for n in numbers:
        if type(n) is not int:
            if n[0] == "$":
                num.append(r_vars[n[1:]])
        else:
            num.append(n)
    #print(numbers)
    return sum(num)

def SUBTRACT(numbers):
    #print(numbers)
    total = numbers[0]
    for n in numbers[1:]:
        total -= n
    return total

def CALC(string):
    return eval(string)

def OPEN(file,r_vars):
    #print(r_vars[file["RETURN"]])
    r_vars[file[-1]] = open(file[1],"r").readlines()

#Loops here will always have the 'line' iterator that they can reference for now. I'm too lazy to make custom iterators atm.    
def LOOP(token, item):
    #print("item is: " + str(item))
    for l in item:
        x = list()
        for t in token:
            #print(t)
            if t[1][0] != "line":
                x.append(t)
                #process_tokens(t)
            else:
                #print([t[0], l])
                x.append([t[0], [l]])
        #print(x)
        process_tokens(x)
                    
def GET_VAR(item):
    if item[0] == "$":
        i = r_vars[item[1:]]
        if i is not None:
            return i
        else:
            return False
                
#This is really fucking ugly, but it gets the job done for now with integer/float comparisons and true/false statements.
def IF(s):
    t = ["LT","GT","EQ","TRUE","FALSE"]
    if s[2] in t:
        if s[2] == "LT":
            if s[1][0] == "$":
                if int(r_vars[s[1][1:]]) < int(s[3]):
                    if s[4] in tokens:
                        eval(s[4]+'(s[5])')
            try:        
                if s[3][0] != int():
                    if s[3][0] == "$": 
                        if int(s[1]) < int(r_vars[s[3][1:]]):
                            if s[4] in tokens:
                                eval(s[4]+'(s[5])')
            except:
                pass
                    
            try:
                if s[1][0] and s[3][0] == "$": 
                    if int(r_vars[s[1][1:]]) < int(r_vars[s[3][1:]]):
                        if s[4] in tokens.tokens:
                            eval(s[4]+'(s[5])')
            except:
                pass
            
        if s[2] == "GT":
            if s[1][0] == "$": 
                if int(r_vars[s[1][1:]]) > int(s[3]):
                    if s[4] in tokens:
                        eval(s[4]+'(s[5])')
            try:        
                if s[3][0] != int():
                    if s[3][0] == "$": 
                        if int(s[1]) > int(r_vars[s[3][1:]]):
                            if s[4] in tokens:
                                eval(s[4]+'(s[5])')
            except:
                pass
                    
            try:
                if s[1][0] and s[3][0] == "$": 
                    if int(r_vars[s[1][1:]]) > int(r_vars[s[3][1:]]):
                        if s[4] in tokens.tokens:
                            eval(s[4]+'(s[5])')
            except:
                pass         
            
        if s[2] == "EQ" or s[[2] == "TRUE"]:
            if s[1][0] == "$": 
                if int(r_vars[s[1][1:]]) == int(s[3]):
                    if s[4] in tokens:
                        eval(s[4]+'(s[5])')
            try:        
                if s[3][0] != int():
                    if s[3][0] == "$": 
                        if int(s[1]) == int(r_vars[s[3][1:]]):
                            if s[4] in tokens:
                                eval(s[4]+'(s[5])')
            except:
                pass
                    
            try:
                if s[1][0] and s[3][0] == "$": 
                    if int(r_vars[s[1][1:]]) == int(r_vars[s[3][1:]]):
                        if s[4] in tokens.tokens:
                            eval(s[4]+'(s[5])')
            except:
                pass     
                        

def process_tokens(token):
    #print(token)
    for s in token:
        f = s[0]
        #print(s)
        if f in tokens:
            if str(f) == "ADD":
                total = ADD(s[1])
                #print(total)
                #print(s[-1])
                r_vars[s[-1]]= total
                
            if f == "SUBTRACT":
                total = SUBTRACT(s[1])
                r_vars[s[-1]]= total
                
            if str(f) == "PRINT":
                #print(s[1])
                PRINT(s[1])
            
            if f == "CALC":
                total = CALC(s[1])
                r_vars[s[-1]]= total
                
            if f == "OPEN":
                OPEN(s, r_vars)
            
            if f == "IF":
                IF(s)
                
            if f == "INPUT":
                INPUT(s[1])
                
            if f == "LOOP":
                var = GET_VAR(s[1])
                if var:
                    LOOP(s[2],var)