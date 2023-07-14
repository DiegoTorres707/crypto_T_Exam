import math
x=6484
y=20056
a=1
b=0
Zp=30677
z=0
d=123
Yc=(y**2)%Zp
Xc=((x**3)+x+1)%Zp
k=555
# punto se suma sobre si mismo


w=2*y
for i in range(0,Zp):
    v=(w*i)%Zp
    if v==1:
        z=i
    alfa=((3*(x**2)+a)*z)%Zp
x3=((alfa**2)-(2*x))%Zp
y3=(alfa*(x-x3)-y)%Zp

print("X 1:",x,"y 1:",y)

print("X 2:",x3,"Y 2:",y3)

for j in range(2,4450):
    if((x3-x)==0):
        x4=-1
        y4=-1

    else:
        for i in range(0, Zp):
            v = ((x3-x) * i) % Zp
            if v == 1:
                z = i

            alfa2 = ((y3 - y) * z) % Zp
        x4 = ((alfa2 ** 2) - (x3 + x)) % Zp
        y4 = (alfa2 * (x3 - x4) - y3) % Zp
    print("X",j+1,x4,"Y",j+1,y4)
    y3=y4
    x3=x4