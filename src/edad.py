def evaluar(dia, mes, anno):
   if dia <= 0 or mes <= 0:
       return'Ingrese datos coherentes'
   else:
        
    from time import localtime

    t = localtime()
    diat = t.tm_mday       
    mest = t.tm_mon       
    annot = t.tm_year           
    annos = annot-anno-((mest,diat)<(mes,dia))
    
    if dia <= 31 and dia >= 1 and mes <= 12 and mes >= 1 and (diat, mest)>= (dia, mes) and annos > 0:
        return "Usted tiene {} años".format(annos)         
    else:    
     return 'Ingrese datos coherentes'
    

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)

