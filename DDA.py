X1 = int(input("insira o valor de X1: "))
Y1 = int(input("insira o valor de Y1: "))
X2 = int(input("insira o valor de X2: "))
Y2 = int(input("insira o valor de Y2: "))

Dx = X2 - X1
Dy = Y2 - Y1
M = Dy / Dx
cont = X1
cont2 = Y1

X = X1
Y = Y1
if(0 <= M and M<=1):
    while cont < X2 +1:
        print(str(cont) + ", " + str(round (Y, 2)))

        Y = Y + M
        cont += 1
elif (M > 1):
    while cont2 < Y2:
        #faça dy = 1
        Dx = X2-X1
        Dy = 1 
        M = Dy / Dx 
        print(  str(round (X, 2))+ ", " +str(cont2))

        X = X + 1/M
        cont2+=1
else:
    print("M esta fora da area de cobertura")