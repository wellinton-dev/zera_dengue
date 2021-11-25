
conta ="x + 4 = 10"

q = conta.split(' ')

if 'x' in q[4]:
    if '-' == q[1]:
        for i in range(0,100000):
            res = int(q[0])-int(q[2])
            if res == i:
                print(res)
else:
    if 'x' in
