# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define mc = Character("old world mc")
define mc2 = Character("new world mc")
define mom = Character("Mom")

# The game starts here.

label start: 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.
    "I miss you.. I miss you so much.."
    ""
    ""

#put music here
    play music "DDLC bgm.mp3" volume 1.0

    mc "I keep thinking that maybe this is the parts of intros that no one actually watches"

    "" "I got up my bed and cleaned up a little bit before heading to the living room"

    "" "I check the clock"

    "" "Holy shit how is it already 2PM?"

    show mc happy at left

    mc "Man, I really have to fix my sleep schedule"

    mc "I wonder.."

    stop music

    menu:
        "yes?":
            jump choice_1
        "no?":
            jump choice_2

    label choice_1:
        mc "Oh, gotta get moving.. maybe I should start with some breakfast. "
    #show mom here
        play music "sayonara.mp3" volume 1.0
        scene bg sayonara

        mom "Oh you're up early, sweetie.'"

        "I give her a dead eyed look"

        mc "Yeah, I overslept again. My sleep schedule's a mess."

        mom "I was just kidding. Come eat, I got you your favorite!"

        mc "Mac and cheese again? Seriously?"

        mom "..."

        mom "What's up with you? Aren't they your favorite?"

        mc "Forget it."

        "I leave the house to get some fresh air"

        

        #bright white light transition







        return

    label choice_2:
        mc "WORK IN PROGRESS"
        return



    mc2 "adsasdasdasdsasdasd"

    mc2 "test2"

    mc2 "hey whats up?dasdasdasdddaddsadsd"

    ""

    mc "monologue here"

    # This ends the game.
    

    return
