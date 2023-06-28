from Listas import Metodos
Listas=[]
_tam=int(input("Ingrese el tamano de la Lista: "))
c=Metodos()
c.ingreso(Listas,_tam)
c.impresion(Listas,_tam)
ultimo_elemento = Listas.pop()
print("Último número eliminado:", ultimo_elemento)
print("Después de eliminar el último elemento:", Listas)
Listas.insert(2, 7)
print("Después de insertar un elemento:", Listas)
Listas.sort()
print("Después de ordenar la lista:", Listas)
Listas.reverse()

print("esto es una prueba de funcionamiento!!!!!!")