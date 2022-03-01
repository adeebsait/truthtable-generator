import re
  
def main():
    print("Welcome to Adeeb's Truth Table Generator")
    print("Please use the symbols '+ for OR' '. for AND' '! for NOT'")
    inputcount = int(input("How many inputs?(2 or 3) "))#A,B OR A,B,C
    expnum = int(input("How many expressions? "))
    i = 1
    j = 1
    exps = []
    funcs = []
    while (i<=expnum):#take expression from user
        print("Enter Propositional Logic",i,": ")       
        line = input()
        exps.append(line)#storing the expressions in a list
        i+=1
        if j<expnum:
            print("Enter the operator for the expression",j,"and",j+1,": ")
            op = input()
            funcs.append(op)#storing the operators in separate list
            j+=1
    funcs.append("")
    print("Your Expression is D = ",end='')#print the total expression
    for (x,y) in zip(exps, funcs):
        print("(",x,")",y,"",end="")
    results = []
    cresults = []
    for p in range(expnum):#intialise nested list for storing results
        cresults.append([])
    fresults = []
    h = 0
    n = 0
    print()
    if inputcount==2:#if only A and B
        m=0
        while(m<expnum):
            for a in [ 0, 1 ]:
                for b in [ 0, 1 ]:#passing values of A,B and expressions
                    cur = compute2(exps[m],a,b)#returns result of the expression
                    cresults[m].append(cur)#storing value in nested list
            m+=1
    elif inputcount==3:#if A, B and C
        m=0
        while(m<expnum):
            for a in [ 0, 1 ]:
                for b in [ 0, 1 ]:
                    for c in [ 0, 1 ]:#passing values of A,B,C and expressions
                        cur = compute3(exps[m],a,b,c)#returns the result of the expression
                        cresults[m].append(cur)#storing value in nested list
            m+=1
    apcount = 0#append counter
    c = 0
    e = 1
    for d in funcs:#applying the logical operators to the results of the expression
        if d=="+":#for OR operation
            if apcount==0:#writing final results for first time
                l=0
                while(l<len(cresults[c])):
                    vals = cresults[c][l] or cresults[e][l]
                    fresults.append(vals)
                    l+=1
                e+=1
                c+=2
                apcount+=1#write counter       
                    
            elif apcount>0:#if values are already present
                l=0
                f=0
                while(l<len(cresults[e])):
                    vals = fresults[l] or cresults[e][l]#compare present value with next expression
                    fresults[l] = vals#replace the value
                    l+=1
                e+=1
                c+=1
                apcount+=1#write counter
                          
        elif d==".":#same for AND operation
            if apcount==0:
                l=0
                while(l<len(cresults[c])):
                    vals = cresults[c][l] and cresults[e][l]
                    fresults.append(vals)
                    l+=1
                e+=1
                c+=2
                apcount+=1#write counter
            elif apcount>0:
                l=0
                while(l<len(cresults[e])):
                    vals = fresults[l] and cresults[e][l]
                    fresults[l] = vals
                    l+=1
                e+=2
                c+=2
                apcount+=1
                
    if inputcount==2:#for 2 input Truth Table
        z=0
        print("Your truth table is: ")
        print( "  A  B  |  D  " )
        print( "--------+-----" )
        while(z<len(fresults)):    
            for a in [ 0, 1 ]:
                for b in [ 0, 1 ]:
                    print( "%3d%3d  |%3d" % 
                          ( a, b,
                            fresults[z] ) )
                    z+=1

                
               
    elif inputcount==3:#for 3 input Truth Table
        z=0
        print("Your truth table is: ")
        print( "  A  B  C  |  D  " )
        print( "-----------+-----" )
        while(z<len(fresults)):
            for a in [ 0, 1 ]:
                for b in [ 0, 1 ]:
                    for c in [ 0, 1 ]:
                        print( "%3d%3d%3d  |%3d" % 
                              ( a, b, c,
                                fresults[z]))
                        z+=1

def compute2( instr, a, b):#function to evaluate 2 input expression
    val = 0
    i = 0
    aref = a
    bref = b
    while(i<len(instr)):
        if instr[i]=="A" or instr[i]=="!":
            if instr[i]=="!":
                a = not a
                i+=1
            if instr[i+2]=="!" and instr[i+3]=="B":
                b = not b
            if instr[i+2]=="!" and instr[i+3]=="A":
                a 
            if instr[i+1]=="+":
                if instr[i+2]=="B" or instr[i+3]=="B":
                    return a or b
                elif instr[i+2]=="A" or instr[i+3]=="A":
                    if instr[i+2]=="!":
                        return a or (not aref)
                    else:
                        return a or a
            elif instr[i+1]==".":
                if instr[i+2]=="B" or instr[i+3]=="B":
                    return a and b
                elif instr[i+2]=="A" or instr[i+3]=="A":
                    if instr[i+2]=="!":
                        return a and (not aref)
                    else:
                        return a and a

        elif instr[i]=="B" or instr[i]=="!":
            if instr[i]=="!":
                bref = b
                b = not b
                i+=1
            if instr[i+2]=="!" and instr[i+3]=="A":
                a = not a
            if instr[i+1]=="+":
                if instr[i+2]=="A" or instr[i+3]=="A":
                    return b or a
                elif instr[i+2]=="B" or instr[i+3]=="B":
                    if instr[i+2]=="!":
                        return b or (not bref)
                    else:
                        return b or b
            elif instr[i+1]==".":
                if instr[i+2]=="A" or instr[i+3]=="A":
                    return a and b
                elif instr[i+2]=="B" or instr[i+3]=="B":
                    if instr[i+2]=="!":
                        return b and (not bref)
                    else:
                        return b and b
            
        
            
def compute3( instr, a, b, c):#function to evaluate 3 input expression
    val = 0
    i = 0
    aref = a
    bref = b
    cref = c                 
    while(i<len(instr)):
        if instr[i]=="!" and  instr[i+1]=="A":#if first input is !A 
            if instr[i+3]=="!" and instr[i+4]=="B":
                if instr[i+2]==".":
                    val3 = not a and not b
                    i=i+5
                elif inst[i+2]=="+":
                    val3 = not a or not b
                    i=i+5
            elif instr[i+3]=="!" and instr[i+4]=="C":
                if instr[i+2]==".":
                    val3 = not a and not c
                    i=i+5
                elif inst[i+2]=="+":
                    val3 = not a or not c
                    i=i+5
            elif instr[i+3]=="B":
                if instr[i+2]==".":
                    val3 = not a and b
                    i=i+4
                elif instr[i+2]=="+":
                    val3 = not a or b
                    i=i+4
            elif instr[i+3]=="C":
                if instr[i+2]==".":
                    val3 = not a and c
                    i=i+4
                elif instr[i+2]=="+":
                    val3 = not a or c
                    i=i+4
            
        if instr[i]=="!" and  instr[i+1]=="B":#if first input is !B  
            if instr[i+3]=="!" and instr[i+4]=="A":
                if instr[i+2]==".":
                    val3 = not b and not a
                    i=i+5
                elif inst[i+2]=="+":
                    val3 = not b or not a
                    i=i+5
            elif instr[i+3]=="!" and instr[i+4]=="C":
                if instr[i+2]==".":
                    val3 = not b and not c
                    i=i+5
                elif inst[i+2]=="+":
                    val3 = not b or not c
                    i=i+5
            elif instr[i+3]=="A":
                if instr[i+2]==".":
                    val3 = not b and a
                    i=i+4
                elif instr[i+2]=="+":
                    val3 = not b or a
                    i=i+4
            elif instr[i+3]=="C":
                if instr[i+2]==".":
                    val3 = not b and c
                    i=i+4
                elif instr[i+2]=="+":
                    val3 = not b or c
                    i=i+4
                    
        if instr[i]=="!" and  instr[i+1]=="C":#if first input is !C  
            if instr[i+3]=="!" and instr[i+4]=="B":
                if instr[i+2]==".":
                    val3 = not c and not b
                    i=i+5
                elif inst[i+2]=="+":
                    val3 = not c or not b
                    i=i+5
            elif instr[i+3]=="!" and instr[i+4]=="A":
                if instr[i+2]==".":
                    val3 = not a and not c
                    i=i+5
                elif inst[i+2]=="+":
                    val3 = not a or not c
                    i=i+5
            elif instr[i+3]=="B":
                if instr[i+2]==".":
                    val3 = not a and b
                    i=i+4
                elif instr[i+2]=="+":
                    val3 = not a or b
                    i=i+4
            elif instr[i+3]=="C":
                if instr[i+2]==".":
                    val3 = not a and c
                    i=i+4
                elif instr[i+2]=="+":
                    val3 = not a or c
                    i=i+4
        if instr[i]=="A":#if first input is A 
            if instr[i+2]=="!" and instr[i+3]=="A":
                if instr[i+1]==".":
                    val3 = a and not a
                    i=i+4
                elif instr[i+1]=="+":
                    val3 = a or not a
                    i=i+4
            if instr[i+2]=="!" and instr[i+3]=="B":
                if instr[i+1]==".":
                    val3 = a and not b
                    i=i+4
                elif instr[i+1]=="+":
                    val3 = a or not b
                    i=i+4
            elif instr[i+2]=="!" and instr[i+3]=="C":
                if instr[i+1]==".":
                    val3 = a and not c
                    i=i+4
                elif inst[i+1]=="+":
                    val3 = a or not c
                    i=i+4
            elif instr[i+2]=="A":
                if instr[i+1]==".":
                    val3 = a and a
                    i=i+3
                elif instr[i+1]=="+":
                    val3 = a or a
                    i=i+3
            elif instr[i+2]=="B":
                if instr[i+1]==".":
                    val3 = a and b
                    i=i+3
                elif instr[i+1]=="+":
                    val3 = a or b
                    i=i+3
            elif instr[i+2]=="C":
                if instr[i+1]==".":
                    val3 = a and c
                    i=i+3
                elif instr[i+1]=="+":
                    val3 = a or c
                    i=i+3
        if instr[i]=="B":#if first input is B
            if instr[i+2]=="!" and instr[i+3]=="B":
                if instr[i+1]==".":
                    val3 = b and not b
                    i=i+4
                elif instr[i+1]=="+":
                    val3 = b or not b
                    i=i+4
            if instr[i+2]=="!" and instr[i+3]=="A":
                if instr[i+1]==".":
                    val3 = not a and b
                    i=i+4
                elif inst[i+1]=="+":
                    val3 = not a or b
                    i=i+4
            elif instr[i+2]=="!" and instr[i+3]=="C":
                if instr[i+1]==".":
                    val3 = b and not c
                    i=i+4
                elif inst[i+1]=="+":
                    val3 = b or not c
                    i=i+4
            elif instr[i+2]=="B":
                if instr[i+1]==".":
                    val3 = b and b
                    i=i+3
                elif instr[i+1]=="+":
                    val3 = b or b
                    i=i+3
            elif instr[i+2]=="A":
                if instr[i+1]==".":
                    val3 = a and b
                    i=i+3
                elif instr[i+1]=="+":
                    val3 = a or b
                    i=i+3
            elif instr[i+2]=="C":
                if instr[i+1]==".":
                    val3 = b and c
                    i=i+3
                elif instr[i+1]=="+":
                    val3 = b or c
                    i=i+3
        if instr[i]=="C":#if first input is C 
            if instr[i+2]=="!" and instr[i+3]=="C":
                if instr[i+1]==".":
                    val3 = c and not c
                    i=i+4
                elif instr[i+1]=="+":
                    val3 = c or not c
                    i=i+4
            if instr[i+2]=="!" and instr[i+3]=="A":
                if instr[i+1]==".":
                    val3 = not a and c
                    i=i+4
                elif inst[i+1]=="+":
                    val3 = not a or c
                    i=i+4
            elif instr[i+2]=="!" and instr[i+3]=="B":
                if instr[i+1]==".":
                    val3 = c and not b
                    i=i+4
                elif instr[i+1]=="+":
                    val3 = c or not b
                    i=i+4
            elif instr[i+2]=="A":
                if instr[i+1]==".":
                    val3 = a and b
                    i=i+3
                elif instr[i+1]=="+":
                    val3 = a or b
                    i=i+3
            elif instr[i+2]=="B":
                if instr[i+1]==".":
                    val3 = b and c
                    i=i+3
                elif instr[i+1]=="+":
                    val3 = b or c
                    i=i+3
            elif instr[i+2]=="C":
                if instr[i+1]==".":
                    val3 = c and c
                    i=i+3
                elif instr[i+1]=="+":
                    val3 = c or c
                    i=i+3

        if instr[i]=="+":
            if instr[i+1]=="!" and instr[i+2]=="A":
                val3 = val3 or not aref
                return val3
            elif instr[i+1]=="!" and instr[i+2]=="B":
                val3 = val3 or not bref
                return val3
            elif instr[i+1]=="!" and instr[i+2]=="C":
                val3 = val3 or not cref
                return val3
            elif instr[i+1]=="A":
                val3 = val3 or aref
                return val3
            elif instr[i+1]=="B":
                val3 = val3 or bref
                return val3
            elif instr[i+1]=="C":
                val3 = val3 or cref
                return val3
        elif instr[i]==".":
            if instr[i+1]=="!" and instr[i+2]=="A":
                val3 = val3 and not aref
                return val3
            elif instr[i+1]=="!" and instr[i+2]=="B":
                val3 = val3 and not bref
                return val3
            elif instr[i+1]=="!" and instr[i+2]=="C":
                val3 = val3 and not cref
                return val3
            elif instr[i+1]=="A":
                val3 = val3 and aref
                return val3
            elif instr[i+1]=="B":
                val3 = val3 and bref
                return val3
            elif instr[i+1]=="C":
                val3 = val3 and cref
                return val3
        
            
main()  
