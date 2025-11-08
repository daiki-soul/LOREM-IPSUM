# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("old world mc")
define mc2 = Character("new world mc")


# The game starts here.

label start: 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mcdo

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.


    mc "Fuck, I'm so tired, can't wait to get home."
    show mc happy at right

    "" "I am a bit hungry, though."

    mc "I ultimately decide to grab a quick takeout at Mcdonald's"
    scene bg mcdo

    mc2 "adsasdasdasdsasdasd"

    mc2 "test2"

    mc2 "hey whats up?dsd"

    # This ends the game.

    return
