meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "NO MANCHES": "dificil de creer"
            }

print("Bienvenido a la biblioteca")
print("...............................................................")
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print("Significa:", meme_dict[word])# ¿Qué debemos hacer si se encuentra la palabra?
        print("---------------------------------------------------------------")
    else:
        print("Lo siento! No conozco esa palabra")# ¿Qué hacer si no se encuentra la palabra?
        print("---------------------------------------------------------------")
print("Nos vemos!")
