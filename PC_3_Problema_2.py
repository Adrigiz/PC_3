try:
    notas = input("Ingrese las notas separadas por comas: ")

    nota_list = notas.split(",")

    nota_inte = []
    for i in range(len(nota_list)):
        nota = int(nota_list[i])
        nota_inte.append(nota)
    print(nota_inte)
except ValueError:
    print(f"Error de tipeo en la nota:{nota_list[i]}")
