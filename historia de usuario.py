#iniciamos el ciclo para preguntar el producto y en caso de ser invalido intentar nuevamente
while True:
    
        producto=str(input("que producto quiere comprar? "))
        if producto.isalpha():
         break
        else:
             print("no es valido lo ingresado intenta nuevamente")

#iniciamos el ciclo para preguntar el precio y en caso de ser invalido intentar nuevamente
    
while True:
    try:
            precio=float(input("que precio tiene el producto? "))
            break
    except ValueError: str
    print("eso no es un valor valido para el precio intenta nuevamente")
#iniciamos el ciclo para preguntar las unidades y en caso de ser invalido intentar nuevamente

while True:
     try:
          cantidad=int(input("cuantas unidades de productos mecesitas? "))
          break
     except ValueError: str
     print("eso no es un valor valido para la unidad intenta nuevamente")
#multiplicamos el precio por las unidades para tener el precio final e imprimimos el resultado
costo_total=float(precio*cantidad)

print(f"su producto {producto} tiene un valor unitario de {precio} y al solicitar {cantidad} de unidades tienen un costo de {costo_total}")

#link del diagrama
#https://drive.google.com/file/d/1WHNtxUEKgcVtGDIlfiebH2PvCsvDXhJu/view?usp=drive_link