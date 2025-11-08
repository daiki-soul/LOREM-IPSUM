# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Original World MC")
define mc2 = Character("New World MC")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    mc "Fuck, can't wait to get home."
       "I am feeling a bit hungry though"

    mc "I should probably grab some mcdonald's real quick"

    mc "I was heree"

    mc "i was here again"

    mc "law was here once again"
    
    mc "everyday i imagine the future where i.."


    # This ends the game.

    return
