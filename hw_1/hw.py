# 1
for i in [2,6]:
    for j in range(2,10):
        q,w,e=i+1,i+2,i+3
        print(f'{i}*{j}={i*j}\t{q}*{j}={q*j}\t{w}*{j}={w*j}\t{e}*{j}={e*j}')
        if j == 9:
            print('')