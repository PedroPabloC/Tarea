#Determinar la matriz de relaciones para un subesbacio ⟨v1,v2,…,vn⟩.

def matrizDeRelaciones(*elementos):
    '''
    DESCRIPCION DE LA FUNCION:
        La funcion obtiene una lista de elementos de un espacio vectorial V. 
        Calcula la matriz y la lleva a su forma escalonada reducida. Retorna
        la matriz de relaciones.
    
    ENTRADA (INPUT):
        *Una lista v1, ... , vn de elementos en el mismo espacio V
        
    SALIDA (OUTPUT):
        *Una matriz de relaciones 
    '''
    
    #comprobacion 
    m=elementos[0].nrows()
    n=elementos[0].ncols()
    bandera=False
    for elemento in elementos:
        if(m == elemento.nrows() and n == elemento.cols()):
            bandera=True
        else:
            bandera=False
            break
        
    if(bandera):
        
        MR=[]    
        #formar matriz
        for x in range(n):                     
            for y in range(m):   
                row=[]          
                for elemento in elementos:
                    dato = elemento[x][y]
                    row.append(dato)      
                MR.append(row)

        #escalonada reducida 
        MR=MR.rref()

        #imprimir matriz           
        for i in range(len(MR)):
            print ('[', end=" ")
            for j in range(len(MR[i])):
                print ('{:>3s}'.format(str(MR[i][j])), end=" ")
            print (']')

    else:
        
        print("Los elementos deben pertenecer al mismo espacio V")
    



matrizDeRelaciones([[1,0],[1,1]],[[0,1],[1,0]],[[2,3],[5,2]],[[1,1],[2,1]])

        
        
        