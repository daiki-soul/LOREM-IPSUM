#ALL SCRIPT GO HERE

#declare all characters here
#can change color of character names, declare here

#MAIN CAST
define mc = Character("old world mc")
define mc2 = Character("new world mc")
define mom = Character("Mom")
define sis = Character("Monika")
define f1 = Character("Kel")
define td = Character("Truck Driver")


#NPCs
define s = Character("Convenience store staff")

#declare image bg resolutions here
image bg MC_room = im.Scale("bg MC_room.png", 1920, 1080)
image bg kitchen = im.Scale("bg kitchen.png", 1920, 1080)
image bg street = im.Scale("bg street.png", 1920, 1080)
image bg convenience store = im.Scale("bg convenience store.jpg", 1920, 1080)

#GAME START
label start:

    "(MC)... (MC)..? We miss you.."
    "Please.. just.. r-"

    "" "..."

    mc "Ugh.."

    scene bg MC_room
    with fade

    play music "DDLC bgm.mp3" volume 0.7
#ACT 1
    "" "I check the clock"

    "" "Holy shit how is it already 2PM?"

    "" "I got up my bed and cleaned up a little bit before promptly stretching"

    show mc happy at left

    mc "Man, I really have to fix my sleep schedule."

    "I fix up my bed before heading downstairs."

    scene bg kitchen
    with dissolve


    stop music fadeout 1.0

    mc "Oh, I gotta get moving.. maybe I should start with some breakfast."

    play music "Family bonds.mp3" volume 0.7

#put mom art here
    show mom happy at right
    with moveinright

    mom "Oh, you're up early, sweetie."
 
    "" "I give her a dead eyed look"

    mc "Yeah, very funny, Mom. I overslept again, I know that my sleep schedule's a mess."

    mom "I was just kidding. Come eat, I got you your favorite!"

    mc "Mac and cheese again? Seriously?"

    mom "..."
    hide mom

    mom "What's up with you? Aren't they your favorite?"

    mc "Sorry, it's just that I'm not feeling great right now."

    mc "Forget about it."
    show sis happy at left
    with moveinright

    sis "Aww, c'mon! You can't skip mac and cheese. That’s, like, your ultimate comfort food"


    "" "My sister, Monika, she the type of person that would mess with you for no reason at all."
    show sis happy at center
    with move

    "" "She has that energy where she effortlessly releases good vibes around her, even if I find her a bit annoying."

    "" "(mc describing sis apperacnce here)"

    "" "If my mom is the warmth of my life, then that rascal sister is the glaring sunlight in my eyes while I'm sleeping."

    "" "Yeah, she drives me crazy but I don't know what I'll do without her."

    mc "I said forget about it."

    sis "Fine, if you don't want it then don't mind if I do."

    "" "She takes a bite out of my food using her spoon and runs away giggling"

    mc "..."

    mc "..Seriously?"

    sis "Do you still want it or not? I don't want you to waste that food."

    "" "Sigh"

    mc "Fine, I'll eat it."

    mc "You're unbelievable."

    sis "That's why you love me, right?"

    "" "She elbows me while grabbing her own breakfast and walking away."


    show mom at right
    with moveinright
    mom "Aww, look at you two getting along, it's like how you both used to."

    mc "..."

    sis "You better eat that now before I take a bite of your food again."

    mc "Heh.. Yeah yeah.."

    "" "After chowing down my food, I decide to go out for a walk."

    stop music fadeout 1.0
    #bright white light transition
    scene bg street
    with fade

    play music "Skips.mp3" volume 0.7

    mc "Maybe this will properly wake me up."

    "" "I start walking down a familiar street, the sound of birds and distant traffic filling the air."

    "" "Come to think of it, I haven't been outside in a while.."

    mc "Hmm.. where should I go?"

    menu:
        "The Park":
            jump choice_1
        "A Convenience Store":
            jump choice_2



    label choice_1:
        mc "The Park it is."


        return

    label choice_2:
        mc "Guess I should get something to drink first."

        "" "I hastily walked to the nearest convenience store."
        scene bg convenience store
        with dissolve

        "" "As I enter the store, I was instantly met with the sound of panel lights and the smell of cheap coffee."

        mc "Lets see.. An energy drink sounds good right now"

        s "Thanks, come again!"

        "" "As I grab the energy drink at the top shelf of the glass fridge, I heard a familiar voice call out to me."

        s "(MC)? Is that you?"

        "" "No way.."

        f1 "Hey it's actually you!"
        show boy happy at right
        with moveinright

        "" "The person standing in front of me is an old friend, Kel, we both used to hangout alot in high school."

        "" "After graduation, we kinda drifted apart."

        mc "Oh, hey, long time no see."

        f1 "Nonchalant as always, huh?"

        mc "..."

        f1 "Yeah, I figured."




        #DIALOGUES FOR STORE END HERE

        #MC DEATH SCENE STARTS HERE




        return









    #NOTES FOR JOSH!!! if transitions to you aren't working, toggle the transition option
    # at the "preferences" bar on the main menu.
    #We should find a way to remove that toggle there so that transitions are on by default.








#audio, bg images, sprites used here are temporary for now until arlo releases official art
#may use the temporary stuff as official part of game, but try not to


#GAME END
return
