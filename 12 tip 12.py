a = 69*'8'
while('3333' in a) or ('8888' in a):
    if '3333' in a:
        a = a.replace('3333','88',1)
    else:
        a = a.replace('8888','33')
print(a)
#answer:888            