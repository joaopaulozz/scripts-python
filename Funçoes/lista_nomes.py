def min_list(_list_str):
    # Tamanho da lista
    len_list = len(_list_str)

    # Normalizando a lista (letra maiuscula)
    list_str =  [s.capitalize() for s in  _list_str]
      
    # Produz uma lista com os tamanhos de cada elemento
    lens = [len(s) for s in list_str]

    # Tamanho do menor (ou menores, quando empate) elemento
    min_len = min(lens)

    # Lista para guardar as strings cujos tamanhos sejam iguais ao minimo
    mins = []

    for i in range(len_list):
        # String normalizada
        s = list_str[i]
        if len(s)==min_len:
            mins.append(list_str[i].strip() )

    return mins  


list_str = ['maria', 'josé', 'PAULO', 'Catarina]', ' kate  ', 'joão', 'mara' ]


print (min_list(list_str))
