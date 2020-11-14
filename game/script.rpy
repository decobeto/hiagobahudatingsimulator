﻿# The script of the game goes in this file.

image secretaria = "secretaria.png"
image contrato = "contrato.jpg"
image maos = "maos.jpg"

image hiago = "hiago_oculos.png"
image hiago_putasso = "hiago_oculos_putasso.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define hb = Character("Hiago Bahú", color="#d63031")
define ht = Character("Hatsune Miku", color="#0EEADF")
define pov = Character("[povname]", color="#e84393")

$ romance_points = 0

# The game starts here.

label start:

    stop music fadeout 3.0
    scene bg unoesc
    with Dissolve(6.0)

    "Hoje é o seu primeiro dia de aula na sua nova faculdade."
    "Você teve que transferir pois seus pais estavam mudando de cidade devido ao trabalho."
    "Uma emoção enorme toma conta de você ao chegar no câmpus."
    "Entretanto alguns documentos não estão certos, é necessário ir até a secretaria assinar alguns papeis."

    scene bg secretaria
    with fade

    "A sala tem um design estranho. Parece algo de um banco de imagens"   

    show secretaria
    
    "Moça da Secretaria" "Olá, você é a aluna nova certo?"

    menu: 

        "Oi, sim sou a aluna nova.":
            jump escolha_nome
    
    return

label escolha_nome:
        
    "Moça da Secretaria" "Okay, vou precisar que você assine esses papeis."
    show contrato

    python:

        povname = renpy.input("Assine os papeis com o seu nome:")
        povname = povname.strip()

    hide contrato
    pov "Tudo pronto moça."

    "Moça da Secretaria" "Obrigada e BEM VINDA A FACULDADE."
    hide secretaria

    "Você escuta algo"
    play sound "audio/siren.mp3"
    "..."
    pov "Droga, isso levou mais tempo do que eu imaginava."
    pov "Preciso correr ou vou chegar atrasada na aula."  

    scene bg black
    with fade

    "Você sai correndo através do câmpus."

    scene bg unoesc
    with fade

    "Sente sua respiração ofegante."

    scene bg black
    with fade

    "Chega dentro da faculdade"
    "Vira em um corredor e..."

    scene bg corredor
    with vpunch

    pov "Ouch..."

    show hiago:
        xalign 1.0 yalign 1.0
    hb "Me desculpe moça"

    menu: 

        "Você não olha por onde anda?":
            $ romance_points =+ 1
            jump ajuntar_caderno

        "Sai da minha frente ô, to atrasada pra aula":
            $ romance_points =- 1

        "Tudo bem, eu estava correndo sem olhar":
            $ romance_points =+ 1
    

label ajuntar_caderno:

    hb "Foi mal mesmo"
    hb "Parece que seus cadernos cairam todos no chão"
    hb "Deixe-me ajuda-lá"

    pov "Não precisa"

    hide hiago
    with fade

    "Vocês dois se abaixam para ajuntar os cadernos"
    "Ao olhar mais de perto você percebe que a pele dele é clara"
    "Clara como leite de amêndoas"
    "Você se pergunta como podem tirar leite de um animal com mamilos tão pequenos"

    show maos
    with fade

    "Ao tentar pegar os cadernos suas mãos se encontram"
    "Você sente seu rosto ficar vermelho"

    hide maos
    with fade

    menu:

        "Desculpa":
            $ romance_points =+ 0
    
    show hiago
    hb "Tudo bem"

    menu: 

        "Bem acho melhor eu ir indo, não quero chegar atrasada":
            $ romance_points =+ 0

    hb "Certo, boa aula"

    hide hiago

    hb "Ei... espero te ver por ai"

    "Você da um sorriso e sai em direção a sua sala"

    show bg black
    with fade

    


    # This ends the game.

    return
