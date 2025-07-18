class Producto:
    def mostrar_info(self, nombre, precio=None, stock=None):
        if precio is None and stock is None:
            print(f"Producto: {nombre}")
        elif stock is None:
            print(f"Producto: {nombre}, Precio: ${precio:.2f}")
        else:
            print(f"Producto: {nombre}, Precio: ${precio:.2f}, Stock: {stock} unidades")

# Uso con diferentes cantidades de argumentos
p = Producto()
p.mostrar_info("Laptop")
p.mostrar_info("Mouse", 25.99)
p.mostrar_info("Teclado", 45.50, 10)
