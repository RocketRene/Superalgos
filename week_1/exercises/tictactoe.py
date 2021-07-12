ttt = [['X', 'O', 'X'],
       ['.', 'X', 'O'],
       ['X', 'O', 'O']]

a= ttt[0][0] 
b= ttt[0][1] 
c= ttt[0][2]

d= ttt[1][0] 
e= ttt[1][1] 
f= ttt[1][2]

g= ttt[2][0] 
h= ttt[2][1] 
i= ttt[2][2]

diagonal=[[a,e,i],[c,e,g]]
vertical= [[a,d,g],[b,e,h],[c,f,i]]
all = [ttt,diagonal,vertical]

for elem in all:
    for x in elem:
        if x == ['X', 'X', 'X'] or x ==['O', 'O', 'O'] :
            print("MATCH.",x,"wins.")