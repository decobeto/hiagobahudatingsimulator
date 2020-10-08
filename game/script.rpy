# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define hb = Character("Hiago Bahú", color="#d63031")
define ht = Character("Hatsune Miku", color="#0EEADF")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music fadeout 3.0
    scene bg unoesc
    with Dissolve(6.0)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "Hoje é o seu primeiro dia de aula na faculdade"


    # This ends the game.

    return
