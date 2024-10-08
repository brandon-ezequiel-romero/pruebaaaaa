inventario = []


def mostrar_menu():

    print(
        """
    1-• Cargar producto/s.
    2-• Buscar producto.
    3-• Ordenar inventario.
    4-• Mostrar producto más caro y más barato.
    5-• Mostrar productos con precio mayor a 15000.
    6-• Salir
    """
    )

    opcion = int(input("eliga una opcion: "))

    return opcion


def verificar_opcion(opcion):

    while opcion > 6 or opcion <= 0:

        opcion = int(input("ERROR | eliga una opcion: "))

    return opcion


def cargar_producto():

    num_productos = int(input("¿Cuántos productos deseas agregar? "))

    for _ in range(num_productos):

        nombre = input("Nombre del producto: ")

        precio = float(input("Precio del producto: "))

        cantidad = int(input("Cantidad del producto: "))

        inventario.append([nombre, precio, cantidad])


def buscar_producto():

    if inventario == []:

        print("No hay producto en el inventario")
        return

    nombre_buscar = input("Introduce el nombre del producto a buscar: ")

    for i in inventario:
        if i[0].lower() == nombre_buscar.lower():

            print(f"Nombre: {i[0]}, Precio: {i[1]}, Cantidad: {i[2]}")

            break


def ordenar_inventario():

    if inventario == []:

        print("No hay producto en el inventario")

        return

    for i in range(len(inventario)):

        for j in range(0, len(inventario) - i - 1):

            if inventario[j][1] > inventario[j + 1][1]:

                inventario[j], inventario[j + 1] = inventario[j + 1], inventario[j]

    for i in inventario:

        print(f"Nombre: {i[0]}, Precio: {i[1]}, Cantidad: {i[2]}")


def mostrar_mas_caro_y_mas_barato():

    if inventario == []:

        print("No hay producto en el inventario")

        return

    producto_mas_caro = inventario[0]

    producto_mas_barato = inventario[0]

    for i in inventario:

        if i[1] > producto_mas_caro[1]:

            producto_mas_caro = i

        if i[1] < producto_mas_barato[1]:

            producto_mas_barato = i

    print(
        f"Producto más caro: Nombre: {producto_mas_caro[0]}, Precio: {producto_mas_caro[1]}, Cantidad: {producto_mas_caro[2]}"
    )

    print(
        f"Producto más barato: Nombre: {producto_mas_barato[0]}, Precio: {producto_mas_barato[1]}, Cantidad: {producto_mas_barato[2]}"
    )


def producto_15000():

    if inventario == []:

        print("No hay producto en el inventario")

        return

    print("Productos con precio mayor a 15000:")

    for i in inventario:

        if i[1] > 15000:

            print(
                f"Nombre: {i[0]}, Precio: {i[1]}, Cantidad: {i[2]}"
            )


def menu():

    opcion = 0

    while opcion != 6:

        opcion = mostrar_menu()

        opcion = verificar_opcion(opcion)

        if opcion == 1:

            cargar_producto()

        elif opcion == 2:

            buscar_producto()

        elif opcion == 3:

            ordenar_inventario()

        elif opcion == 4:

            mostrar_mas_caro_y_mas_barato()

        elif opcion == 5:

            producto_15000()

        else:

            print("Saliendo del sistema")


menu()