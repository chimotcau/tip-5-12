a= '1'+99*'8' +'1'
while('81' in a) or ('882' in a) or('8883' in a):
    if '81' in a:
        a = a.replace('81','2',1)
    elif '882' in a:
        a = a.replace('882','3',1)
    else:
        a = a.replace('8883','1',1)
print(a)
#answer:13             