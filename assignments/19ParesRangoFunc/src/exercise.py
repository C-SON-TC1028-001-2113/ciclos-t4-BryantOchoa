
def main():
    #escribe tu código abajo de esta línea
    pass
    num = int(input("Valor 1: "))
    num2 = int(input("Valor 2: "))
    for cont in range(num,num2 + 1):
        if cont % 2 == 0:
            print(cont)

if __name__=='__main__':
    main()
