dic={"lol":"una respuesta a algo gracioso","cringe":"algo raro o embarazoso","rofl":"una respuesta a una broma","sheesh":"ligera desaprobación","creepy":"aterrador,siniestro","agroo":"ponerse agresivo/enojado"}
while True:
    pal=input("pon aquí la palabra que quieras buscar.")
    if pal in dic.keys():
        print(dic[pal])
    else:
        print("esta palabra no se encuentra en el diccionario")
