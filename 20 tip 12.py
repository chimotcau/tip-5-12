a = 8*'1'+8*'2'
while('111' in a) or('222' in a):
    if '111' in a:
        a = a.replace('111','2',1)
    if '222' in a:
        a =a.replace('222','1',1)
print(a) 
#answer:1122       
