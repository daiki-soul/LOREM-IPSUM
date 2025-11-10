#ALL SCRIPT GO HERE

#declare all characters here
#can change color of character names, declare here

define mc = Character("old world mc")
define mc2 = Character("new world mc")
define mom = Character("Mom")

#declare image bg resolutions here
image bg MC_room = im.Scale("bg MC_room.png", 1920, 1080)
image bg kitchen = im.Scale("bg kitchen.png", 1920, 1080)
image bg street = im.Scale("bg street.png", 1920, 1080)

#GAME START
label start:

    "(MC)... (MC)..? We miss you.."
    "Please.. just.. r-"

    "" "..."

    mc "Ugh.."

    scene bg MC_room
    with fade

    play music "DDLC bgm.mp3" volume 1.0

    "" "I check the clock"

    "" "Holy shit how is it already 2PM?"

    "" "I got up my bed and cleaned up a little bit before promptly stretching"

    show mc happy at left

    mc "Man, I really have to fix my sleep schedule."

    "I fix up my bed before heading downstairs."

    scene bg kitchen
    with dissolve


    stop music

    mc "Oh, I gotta get moving.. maybe I should start with some breakfast."

    play music "Family bonds.mp3"

#put mom art here
    show mom happy at right
    with move

    mom "Oh, you're up early, sweetie."
 
    "" "I give her a dead eyed look"

    mc "Yeah, very funny, Mom. I overslept again, I know that my sleep schedule's a mess."

    mom "I was just kidding. Come eat, I got you your favorite!"

    mc "Mac and cheese again? Seriously?"

    mom "..."

    mom "What's up with you? Aren't they your favorite?"

    mc "Sorry, it's just that I'm not feeling great right now."

    mc "Forget about it."

    "" "Better get some fresh air… maybe the sun will wake me up."

    #bright white light transition test

    scene bg street
    with fade



        #bright white light transition



    


    #NOTES FOR JOSH!!! if transitions to you aren't working, toggle the transition option
    # at the "preferences" bar on the main menu.
    #We should find a way to remove that toggle there so that transitions are on by default.


    label choice_1:
        mc "WORK IN PROGRESSS"
        return

    label choice_2:
        mc "WORK IN PROGRESS"
        return





#audio, bg images, sprites used here are temporary for now until arlo releases official art
#may use the temporary stuff as official part of game, but try not to


#GAME END
return
