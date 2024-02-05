def arithmetic_arranger(*problems):
    
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    
    for problem in problems[0]:
        splitp = problem.split()
        x = splitp[0]
        y = splitp[1]
        z = splitp[2]

        if len(problems[0]) <= 5:
            
            if y=="+" or y=="-":
                if x.isdigit() and z.isdigit():
                    if len(x) < 5 and len(z) < 5:
                        if y == "+":
                            result = int(x) + int(z)
                            
                        else:
                            result = int(x) - int(z)
                        len1 = len(x)
                        len2 = len(z)
                        maxlen=max(len1,len2) + 2
                        
                        line1 += x.rjust(maxlen) + "    "
                    
                        line2 += y + z.rjust(maxlen - 1)  + '    '
                        line3 += '-'*maxlen + '    '
                        line4 += str(result).rjust(maxlen)   + '    '
                        
                    else:
                        return"Error: Numbers cannot be more than four digits."
                else:
                    return"Error: Numbers must only contain digits."
            else:
                return"Error: Operator must be '+' or '-'."
        else:
            return"Error: Too many problems."
            
    text ="\n".join((line1.rstrip(),line2.rstrip(),line3.rstrip()))
    
    if len(problems) == 2 and problems[1] == True:
        text += '\n' + line4.rstrip()
    return text
            
   
            

print(arithmetic_arranger(["1 + 2", "1 - 9380"]))  
                        
                        
       
                        
                        
                        
                        
                        
                            
                       
                        
                        
                        
                        
                        
                        
            
            
                    