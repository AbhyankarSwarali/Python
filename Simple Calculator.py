class InvalidFormulaError(Exception):
    pass 

print('Valid formula format: a (operand) b')

def evaluate(formula):    
    f=formula.split()

    if len(f) < 3:
        raise InvalidFormulaError ('Formula should have SPACES')

    if f[1]=='+' or f[1]=='-' or f[1]=='*' or f[1]=='/':
        op1= int(f[0])
        op2=int(f[2])

        if f[1]=='+':
            res = op1 + op2
        elif f[1]=='-':
            res = op1 - op2
        elif f[1]=='*':
            res = op1 * op2
        else:
            res = op1 / op2

        return res
    
    else: 
        raise InvalidFormulaError ('Invalid formula format')
    
try:
    formula = input('Enter formula: ')
    print(evaluate(formula))
except InvalidFormulaError as i:
    print(i)