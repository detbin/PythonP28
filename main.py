def main():
    pais=''
    pais=input('Introduzca una lista de paises separados por comas')
    lista=pais.split(',')
    listaLimpia=set(lista)
    sorted(listaLimpia)
    print(listaLimpia)
if __name__ == '__main__':
    main()