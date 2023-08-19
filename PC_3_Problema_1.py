check = True
while check:

    try:
        fuel = input("Ingrese la cantidad de gasolina: ")

        x,y = fuel.split("/")
        x = int(x)
        y = int(y)
        n = x/y
        total = 1
        if x > y : 
            pass
        else :

            if n < (total*0.01) : 
                print("E")
            elif  n > (total*0.99 ): 
                print("F")
            
            else:
                print(f"{round(n*100)}%")

            check = False
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

