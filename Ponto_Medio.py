X1 = int(input("insira o valor de X1: "))
Y1 = int(input("insira o valor de Y1: "))
X2 = int(input("insira o valor de X2: "))
Y2 = int(input("insira o valor de Y2: "))
Pos1 = X1
Pos2 = Y1
print(str(Pos1) + ", " + str(Pos2))
while Pos1 < X2:
    Dx = X2 - Pos1
    Dy = Y2 - Pos2 
    M = Dy / Dx 
    B = (Y2 - (M * X2)) 
    
    Condição = Dx*Pos1 + -Dy*Pos2 + Dy * B 
    
    if(Condição > 0):
        print("NE" )
        Pos1 += 1
        Pos2 +=1
    elif(Condição < 0):
        print("E")
        Pos1 += 1

    else:
        print("o proximo pixel podera ser tanto em NE quanto E.")
        Pos1 += 1
        Pos2 +=1
    
    print(str(Pos1) + ", " + str(Pos2))