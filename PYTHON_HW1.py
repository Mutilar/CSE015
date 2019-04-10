#1.1
def AND(p, q):
    return p and q

#1.2
def OR(p, q):
    return p or q

#1.3
def IF(p, q):
    if p:
        return q
    return True

#1.4
def NOT(p):
    return not p

#1.5
def IFF (p,q):
    return p == q

#1.6
def evaluation(formula):
    if formula[0] == "AND":
        return AND(formula[1], formula[2])
    if formula[0] == "OR":
        return OR(formula[1], formula[2])
    if formula[0] == "IF":
        return IF(formula[1], formula[2])
    if formula[0] == "NOT":
        return NOT(formula[1])
    if formula[0] == "IFF":
        return IFF(formula[1], formula[2])

#Test Case
print ("Simple Evaluation Function Test")
print  
p = True
q = False 
print ("p =", p)
print ("q =", q) 
print
print ("(p or q):   ",evaluation (('OR', p, q)))
print ("(p and q):  ",evaluation (('AND', p, q)))
print ("(p -> q):   ",evaluation (('IF', p, q)))
print ("(p <-> q):  ",evaluation (('IFF', p, q)))
print ("-p:         ",evaluation (('NOT', p)))
input("Press Enter to continue...")