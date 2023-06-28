class Metodos():
    def ingreso(self,lis,tam):
        i=0
        while(i<tam):
            print("Ingrese el [",i,"] valor de la lista")
            num=int(input("numero "))
            lis.append(num)
            i=i+1
    def impresion(self,lis,tam):
        for i in range(tam):
            print(lis[i])