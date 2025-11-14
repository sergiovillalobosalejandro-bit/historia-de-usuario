tienda = {
    "mojarra": 500000,
    "piña colada": 200000,
    "cerveza aguila": 50000,
    "ceviche": 150000,
    "pulpo": 700000,
    "cachama": 1000000
}

carrito = []

def agregar_producto():
    print("PRODUCTOS DISPONIBLES:")
    for producto, precio in tienda.items():
        print(f"- {producto}: ${precio}")

    producto = input("Escribe el nombre del producto que deseas agregar: ").strip().lower()

    if producto not in tienda:
        print("Producto no disponible.")
        return

    while True:
        unidades = input("¿Cuántas unidades deseas agregar?: ")
        if unidades.isdigit():
            unidades = int(unidades)
            break
        else:
            print("Ingresa solo números.")

    carrito.append({"producto": producto, "unidades": unidades, "precio": tienda[producto]})
    print(f"Se agregó al carrito: {producto} x {unidades}")


def ver_productos():
    print("LISTA DE PRODUCTOS:")
    for producto, precio in tienda.items():
        print(f"{producto}: ${precio}")


def ver_carrito():
    if not carrito:
        print("El carrito está vacío.")
        return

    print("PRODUCTOS EN EL CARRITO:")
    for item in carrito:
        total_item = item["unidades"] * item["precio"]
        print(f"{item['producto']} x {item['unidades']} - ${total_item}")


def eliminar_producto():
    if not carrito:
        print("El carrito está vacío.")
        return

    ver_carrito()

    producto = input("Escribe el nombre del producto que deseas eliminar: ").strip().lower()

    for item in carrito:
        if item["producto"] == producto:
            carrito.remove(item)
            print(f"Producto eliminado: {producto}")
            return

    print("Ese producto no está en el carrito.")


def total_pagar():
    if not carrito:
        print("El carrito está vacío.")
        return

    total = sum(item["unidades"] * item["precio"] for item in carrito)
    print(f"TOTAL A PAGAR: ${total}")


while True:
    print("""
    BIENVENIDO A CARTAGENA CACHA
    1. Agregar productos al carrito
    2. Ver productos disponibles
    3. Eliminar producto del carrito
    4. Ver carrito
    5. Total a pagar
    6. Salir
    """)

    seleccion = input("Elige una opción: ")

    match seleccion:
        case "1":
            agregar_producto()
        case "2":
            ver_productos()
        case "3":
            eliminar_producto()
        case "4":
            ver_carrito()
        case "5":
            total_pagar()
        case "6":
            print("Feliz día.")
            break
        case _:
            print("Opción inválida.")