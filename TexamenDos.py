import math
x=1090
y=18593
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

for j in range(2,Zp):
    if((x3-x)==0):
        x4=-1
        y4=-1
        print("X",j+1,x4,"Y",j+1,y4)
        break
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



print("Sustituyendo los valores: y^2=x^3+x+1= (18593^2)mod(30677)=((1090^3)+1090+1)mod(30677) = ",Yc,"=",Xc)
print("El orden es:",j+1)



def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
es_primo(j+1)
n_1=j+1
print("con d=123 Q= x:6484 y: 20056")
print("con k=555 kp= x:20950 y:1060")

r=20950%n_1
print("r: ",r)
if r !=0:
    k_1=pow(k,-1,n_1)
else:
    print("Regresa al paso 1")

print("Inverso de k = 555 es k^-1=",k_1)

H_m=34653
print("El resultado de aplicar la funcion SHAfa",H_m)

s=k_1*(H_m+d*r)%n_1
print("s =",s)

sk=s*k%n_1
t=(H_m+d*r)%n_1
print("Comprobando sk mod n =h(m)+dr mod n= ",sk," = ",t)
print("La firma es: ",r,",",s)
print("r = 2431 y s = 4305 y ambos están en el intervalo [1,n-1]")
W=pow(s,-1,n_1)
print("w = ",W)

u1=(H_m*W)%n_1
u2=(r*W)%n_1
print("u1 = ",u1)
print("u2 = ",u2)

print("u1P = ",5533,17363)
print("u2Q = ",16064," , ",20932)

xu1P=5533
yu1p=17363
xu2Q=16064
yu2Q=20932

for i in range(0, Zp):
    v = ((xu1P - xu2Q) * i) % Zp
    if v == 1:
        z = i
alfa3 = ((yu1p - yu2Q) * z) % Zp
x5 = ((alfa3 ** 2) - (xu1P + xu2Q)) % Zp
y5 = (alfa3 * (xu1P - x5) - yu1p) % Zp
print("u1P + u2Q = X",x5,"Y",y5)
V=x5%n_1
print("v = ",V)

print("Entonces como r = ",r,"y v = ",V,"la firma es aceptada")

print("Q = x:6484 y: 20056")
print("r = ",r)
print("s = ",s)
print("w = ",W)
print("u1 = ",u1)
print("u2 = ",u2)
print("u1*P = x: ",xu1P," y: ",yu1p)
print("u2*Q = x: ",xu2Q," y: ",yu2Q)
print("v = ",V)




