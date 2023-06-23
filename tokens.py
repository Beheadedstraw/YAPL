tokens = [
    "ADD",
    #"SUBTRACT",
    #"MULTIPLY",
    #"DIVIDE",
    "IF",
    "ELSE",
    #"WHILE",
    "PRINT",
    "OPEN_FILE",
    "CLOSE_FILE",
    "CALC",
    "INPUT",
    "LOOP",
    "WRITE_FILE",
    "READ_FILE"
]

#General variable storage. We have no concept of those fancy things like "global/private/public" variables. Pointers? Did you think this was C or something?
r_vars = {}

#storage for functions in the yaml file. Classes? The fuck are those? OOP? Sir, I'm way too innebriated for that.
r_funcs = {}


def INPUT(r):
    ''' It gets input from the user, duh. '''
    line = input()
    r_vars[r] = line
    
def PRINT(line):
    ''' It... wait for it... PRINTS stuff to the screen. '''
    complete_line = ""
    for l in line:
        if l[0] == "$":
            #print(r_vars[l[1:]])
            complete_line += str(r_vars[l[1:]])
        else:
            complete_line += str(l)
    print(complete_line)
        
def ADD(numbers):
    ''' Can you put 2 and 2 together and figure out what this does? '''
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
    ''' When opposites subtract... or is it attract... something like that '''
    #print(numbers)
    total = numbers[0]
    for n in numbers[1:]:
        total -= n
    return total

def CALC(string):
    ''' Seems like a calculating function. FYI this is just a straight eval(string) line. No really, it is. '''
    return eval(string)

#Loops here will always have the 'line' iterator that they can reference for now. I'm too lazy to make custom iterators atm.    
def LOOP(token, item):
    ''' Fruity Loops. Except without the music. For now atleast. Maybe I'll throw some magical fucking AI shit in here. '''
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
        
def OPEN_FILE(file, var):
    ''' OPEN SESAME SEEDS... or says a me, or says me... Aladdin help ya boy out. OPEN's a file and throws it into a variable, if the file doesn't exist, it makes one for you, neat huh?.'''
    r_vars[var] = open(file,"a+")        
    
def READ_FILE(file,var):
    ''' What? You think this is reading rainbow? It reads a file dumbass. Keep in mind you have to OPEN it first. '''
    f = GET_VAR(file)
    f.seek(0)
    lines = f.readlines()
    r_vars[var] = lines
    return True
            
def WRITE_FILE(file, data):
    ''' Is it WRITE or is it wrong? Write's shit to a file. Gotta have it OPEN first though. '''
    f = GET_VAR(file)
    for d in data:
        f.write(d)
    return True        

def CLOSE_FILE(file):
    ''' if I need to explain this to you we've got some problems.'''
    f = GET_VAR(file)
    f.close()
                    
def GET_VAR(item):
    ''' Gets the Vars from r_vars ya har?'''
    if item[0] == "$":
        i = r_vars[item[1:]]
        if i is not None:
            return i
        else:
            return False
        
def VAR(name, data):
    r_vars[name] = data
    return True
                
#This is really fucking ugly, but it gets the job done for now with integer/float comparisons and true/false statements.
def IF(s):
    ''' No ifs ands or buts about it '''
    t = ["LT","GT","EQ","TRUE","FALSE"]
    if s[2] in t:
        if s[2] == "LT":
            try:
                if s[1][0] == "$":
                    if type(r_vars[s[1][1:]]) == int:
                        if int(r_vars[s[1][1:]]) < int(s[3]):
                            if s[4] in tokens:
                                eval(s[4]+'(s[5])')
            except:
                pass
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
            
        if s[2] == "EQ" or s[2] == "TRUE":
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
    ''' The magic sauce. The main loop. The head of the heads. You get the idea... maybe...? '''
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
                
            if f == "OPEN_FILE":
                OPEN_FILE(s[1], s[2])
            
            if f == "IF":
                IF(s)
                
            if f == "INPUT":
                INPUT(s[1])
                
            if f == "LOOP":
                var = GET_VAR(s[1])
                if var:
                    LOOP(s[2],var)
            
            if f == "WRITE_FILE":
                WRITE_FILE(s[1],s[2])
                
            if f == "READ_FILE":
                READ_FILE(s[1],s[2])