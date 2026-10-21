my_dict = {"Cringe": "Algo extraño o embarazoso.", "Funar": "Cancelar públicamente a algo o alguien", "NTP": "Abreviación de 'no te preocupes'", "LOL": "Expresión para algo gracioso.", "XD": "Representación de una carita riéndose."}

word = input("Escribe una palabra que no entiendas:")

if word in my_dict.keys():
   print(my_dict[word])
else:
   print("Esa palabra no se encuentra en el diccionario.")
