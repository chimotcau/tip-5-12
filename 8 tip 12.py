a = 1000*'9'
while('999'in a)or ('888' in a):
    if '888' in a:
        a =a.replace('888','9',1)
    else:
        a = a.replace('999','8',1)
print(a) 
#answer:8899           