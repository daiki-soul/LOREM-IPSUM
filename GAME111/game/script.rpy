#ALL SCRIPT GO HERE

#declare all characters here
#can change color of character names, declare here

# #MAIN CAST
# default player_name = ""

define a = Character("???") #placeholder for unknown
define mc = Character("[player_name]") #original mc
define mcln = Character("[last_half_name]") #half of player name
define mc2 = Character("Lawrence") #unofficial name, the isekai'd new body of mc
define mom = Character("Mom") #mc and mc2 mom
define dad = Character("Dad") #dead from both mc and mc2 world
define sis = Character("Mika") #amc and mc2 sister
define kel = Character("Kiel") #mc bestfriend, mc2 classmate (something went wrong)
define hari = Character("Hari") #m (basilo bestfriend)
define bas = Character("Basilo") #m (hari and basilo best friends who compete for Chika)
define omi = Character("Omi") #m but femboy
define chi = Character("Chika") #f the beautiful shy girl
define wagi = Character("Waguri") #f
define ros = Character("Rosie") #f
define yui = Character("Yui") #f (wagi, ros, yui are childhood friends)

#SIDE CHARACTERS
define ichi = Character("Ichika") #f classmate
define paul = Character("Paul") #m school delinquent
define emu = Character("Emu") #f someone who dies later on (pretends to be important character early in the story) (this ending for her depends on the story flow and route)
define ari = Character("Ari")#f emu's friend
define ku = Character("Kuro")#m the otaku




#NPCs
define s = Character("Convenience store staff")
define cm = Character("Classmate")
define npc = Character("Stranger")
define td = Character("Truck Driver")

#declare image bg resolutions here
image bg MC_room = im.Scale("bg MC_room.png", 1920, 1080)
image bg kitchen = im.Scale("bg kitchen.png", 1920, 1080)
image bg street = im.Scale("bg street.png", 1920, 1080)
image bg convenience store = im.Scale("bg convenience store.jpg", 1920, 1080)
image bg city = im.Scale("bg city.png", 1920, 1080)
image bg arcade = im.Scale("bg arcade.jpg", 1920, 1080)
image bg arcade2 = im.Scale("bg arcade2.jpg", 1920, 1080)
image jumpscare = "images/jumpscare.png"
image bg sayonara = im.Scale("bg sayonara.png", 1920, 1080)
image monika = "images/monika.png"
image truck = im.Scale("images/truck.jpg", 1920, 1080)
image crash = im.Scale("images/black.png", 1920, 1080)

#defining positions
transform mid_left:
    xalign 0.35
    yalign 1.0

transform mid_right:
    xalign 0.65
    yalign 1.0

transform close_left:
    xalign 0.20
    yalign 1.0

transform close_right:
    xalign 0.80
    yalign 1.0

transform run_left:
    linear 0.25 xalign -0.5

transform run_right:
    linear 0.25 xalign 1.5





























#others

#GAME START
label start:

    scene bg streetrain
    with fade

    $ player_name = renpy.input("A college student is passed out cramming in his room. What is his name?")
    $ player_name = player_name.strip()

# If player leaves it blank, set default
if player_name == "":
    $ player_name = "Player"

# Compute the last half of the name
$ last_half_name = player_name[len(player_name)//2:]

# If something went wrong and last_half_name is blank (very short name), default it
if last_half_name == "":
    $ last_half_name = "Player"


    "Your name is [player_name]."

    "" "Do you remember?"

    stop music fadeout 2


    "[player_name]... [player_name]..? We miss you.."

    "Please.. just.. r-"

    "" "..."

    player_name "Ugh.."

    scene bg MC_room


    with fade

    play music "DDLC bgm.mp3" volume 0.7

    #ACT 1

    "" "I check the clock"

    show screen time_2pm


    "" "Holy shit how is it already 2PM?"


    "" "I got up my bed and cleaned up a little bit before promptly stretching"

    hide screen time_2pm


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

    $ ambient.play("audio/ambient/rain.mp3")#ambient

    with moveinright

    mom "Oh, you're up early, sweetie."

    "" "I give her a dead eyed look"

    mc "Yeah, very funny, Mom. I overslept again, I know that my sleep schedule's a mess."

    mom "I was just kidding. Come eat, I got you your favorite!"

    mc "Mac and cheese again? Seriously?"

    $ ambient.stop()


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

    scene bg city
    with dissolve

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


label choice_2:
    mc "Guess I should get something to drink first."

    "" "I hastily walked to the nearest convenience store."
    scene bg convenience store
    with dissolve

    stop music
    play music "Convenience store.mp3" volume 0.7

    "" "As I enter the store, I was instantly met with the sound of panel lights and the smell of cheap coffee."

    mc "Lets see.. An energy drink sounds good right now"

    npc "Oh yeah, please put it in the bag."

    s "Thanks sir, come again!"

    "" "As I grab the energy drink at the top shelf of the glass fridge, I heard a familiar voice call out to me."

    s "(MC)? Is that you?"

    "" "No way.."

    kel "Hey it's actually you!"
    show kiel happy at right
    with moveinright

    "" "The person standing in front of me is an old friend, Kel, we both used to hangout alot in high school."

    "" "After graduation, we kinda drifted apart."

    mc "Oh, hey, long time no see."

    kel "Nonchalant as always, huh?"

    mc "..."

    kel "Yeah, I figured."

    kel "Dude, you wanna hangout after shift?"

    menu:
        "Yes":
            jump choice_1_yes
        "No":
            jump choice_2_no


label choice_1_yes:
    "Yeah sure, whatever."
    kel "Awesome, you mind waiting till 5pm?"

    mc "Yeah for sure, bro, I'll be waiting outside yeah?"

    kel "Sweet, see you later man."

    kel "Oh wait can I get your contact just incase I get off early?"

    mc "Damn, almost forgot, yeah yeah sure."

    "" "And I'm about to hand out my cheap ass android phone to an old friend of mine.. Talk about minus aura."

    jump store_end


label choice_2_no:
    mc "Sorry man, a little busy today"

    kel "Welp, see you around I suppose."

    kel "Can I at least get your contact, Dude?"

    mc "..."

    mc "Okay, here."

    "" "And I'm about to hand out my cheap ass android phone to an old friend of mine.. Talk about minus aura."

    "" "After typing my contact into his phone, I promptly grab my phone back and walked towards the glass door, with my drinks in hand."

    "" "I raise my hands up to wave, before finally getting outside. I swear I saw him smirk when he looked at my phone."

    kel "Alright, see you, man."
    stop music fadeout 1.0

    jump store_end


label store_end:
    scene bg city
    with dissolve
    play music "Simplicities.mp3" volume 0.7

    "" "Man, I can't believe he is now working at the convenience store we all used to hangout in."

    "" "I roam around to check the arcade we also used to hangout in"

    mc "Man, this brings back so many memories."

    "" "Maybe I should ask him to go here after his shift ends."

    a "Is that who I think it is??"
    show hari happy at left
    with moveinleft

    a "Yeah! That's definitely him!"
    show bas happy at right
    with moveinright

    a "..."
    show omi happy at close_right
    with moveinleft

    "" "..?"

    hari "BROOOO is that you?!"

    bas "No way.. I thought you moved or something.."

    omi "I.."

    bas "Dude, what the fuck? Why aren't you responding to our calls?"

    hari "Yeah I genuinely thought you fucking died."

    mc "H-Hari? Basilo?? and.. Omi.."

    mc "What are you guys doing here?"

    hari "Kel texted us that he saw you, we immediately got here as soon as possible."

    bas "Yeah, he didn't even bother showering today."

    hari "Bro, I was in my room the whole day, I'm sure I'm clean!"

    omi "Haah.. Haha.."

    bas "Yeah.. sure.."

    "" "[bas] leaned closer and whispered, he's lying"

    "" "I can see the look in [hari]'s face as he's starting to look really pissed off. I almost forgot that he has always had a short fuse."

    "" "[bas] should probably stop teasing him now or else they'd get into a fight like they always do.."

    hari "Why you little!—"

    omi "G-Guys.. cut it out.."

    omi "..[mc] is with us."

    mc "..."

    hari "Oh, right.. excuse me.."

    bas "Heh, sorry man, just wanted to tease you like old times."

    hari "..."

    hari "So, [mc] been a while, huh?"

    mc "Yeah.. it really has.."

    bas "Guys lets hangout like we used to! Since [mc] is here!"

    kel "Yo, what's going on guys."
    show kel happy at center
    with moveinleft

    hari "It's about time you showed up."

    kel "Heh.. sorry, shift was tight today."

    omi "It's okay, [kel], I understand."

    bas "So, where do you guys wanna go?"

    bas "I was thinking that we'd hangout at our good ol' arcade."

    omi "Oh yeah! [hari] used to lose all the time to [kel]! Haha!"

    omi "XD"

    hari "...are you guys kidding me? I can beat you all with one hand."

    bas "Sure you can, I'm sure you use that right hand to jack off all the time, I wouldn't be surprised!"

    hari "Oh this time you're gonna get it.."

    "" "[bas] runs away and enters the arcade with [hari] chasing him with a completely red face. He sure is one heck of a fuse."
    show hari at run_right



    omi "[bas]! That's rude!"
    show bas at run_right
    "" "[omi] follows them both into the arcade, leaving just me and [kel] behind."
    show omi at run_right

    "" "[kel] smiles at me"

    kel "It's just like old times, huh?"

    mc "Heh.. real.."

    mc "And they went inside our favorite arcade. I hope they won't cause too much trouble."

    kel "We should probably follow them. Come on."

    #insert arcade bg
    scene bg arcade
    with fade
    stop music fadeout 1.0

    "We ended up drifting into the old arcade like nothing had changed."

    play music "Happenings.mp3"

    "I spot [hari] and [bas] already playing a game called Tokken 6. With Omi watching with starry eyes as the two fight it out in the game."

    hari "LOSER BUYS DRINKS!"

    bas "You’re on."

    mc "I already regret coming here."

    kel "Come on, [mc], you promised you'd hangout with me like old times sake"

    mc "But I do have to admit, I miss this place.."

    mc "I also miss you al—{nw}"


    a "Ha! Fuck you, [bas]!"

    hari "I told you I can easily beat you."

    omi "YAAAYYY!"

    bas "Damn it.. He's gotten stronger.."

    omi "Guys, our [bas]'s paying for our drinks!!"

    hari "A bet is a bet."

    bas "Yeah.. a bet is a bet.."

    bas "Atleast he already forgot about being angry.."

    omi "I want to fight [kel]!"

    kel "Mm, sure{nw}"

    "" "*put phone ringing sfx here"

    kel "Ah, I gotta take this."

    kel "You can play with [mc] instead."

    omi "[mc]..?"

    "" "[kel] walks out the arcade to take that seemingly important phone call..."

    "" "..."

    mc "What do you wanna play Omi?{nw}"
    stop music

    "" "[omi] went off really fast to the back corner of the arcade, where her favorite game is located."

    mc "What's her deal?"

    "I immediately followed"
    scene bg arcade2
    with fade

    omi "No! Leave me alone!"

    omi "I already accepted the fact that you're gone.."

    omi "Why did you.."

    play music "My Feelings.mp3"
    omi "Why did you have to show yourself back again?"

    mc "Oms..?"

    omi "NO! Don't you dare call me that again!"

    omi "You were.. you were my bestfriend.. and you.. you left me, you left us."

    omi "So suddenly.."
    stop music




    "" "SCENE IN PROGRESS. PROGRESSING TO DEATH SCENE..."









label crash:
    scene truck

    $ renpy.sound.play("audio/ambient/truckhorn.mp3", channel="sound", loop=False)
    $ renpy.sound.set_volume(1, delay=0, channel="sound")
    "" "w-what?"
    "" "Huh?"
    "" "…What’s that sound?"
    "" "Why are those headlights so close?"
    "" "Wait."
    "" "Is that truck… coming this way?"
    play music "sayonara.mp3" volume 1.0
    show screen film_grain_effect
    "" "No—"
    "" "Move."
    "" "Move!"
    "" "Why can’t I move?!"
    "" "Ah…"
    "" "So this is it."
    "" "I really thought I had more time."
    "" "I was going to fix everything tomorrow…"
    "" "Heh…"
    "" "Guess tomorrow’s not coming."
    "" "So much for finally deciding to fix everything."
    "" "This is how I die, huh?"
    "" "My life flashes before my eyes."
    "" "All I see are my regrets."
    "" "The Truck finally hits my body.."
    "" "Augh!{nw}"
    with vpunch
    $ renpy.sound.play("carsqueel.mp3",loop=False)
    $ renpy.sound.set_volume(3, delay=0, channel="sound")
    stop music

    $ renpy.pause(2, hard=True)
    "{nw}"

    scene crash
    window hide
    $ renpy.pause(2, hard=True)
    $ renpy.sound.play("audio/ambient/heart.wav", channel="sound", loop=True) #convert .wav into mp3 or OGG (better) because it is more compatible this way
    $ renpy.sound.set_volume(1, delay=0, channel="sound") #try find way to increase volume of heart sfx
    show screen incoming_call_mom1
    "" "mom?"
    show screen incoming_call_mom1
    #ring sfx here
    pause 3
    show screen incoming_call_mom1
    "" "..."
    show screen incoming_call_mom1
    "" "mom..."
    show screen incoming_call_mom1
    "" "..."
    show screen incoming_call_mom1
    "" "..."
    show screen incoming_call_mom1
    "" "Aughh.. fuck.."
    show screen incoming_call_mom1
    "" "It hurts.."
    show screen incoming_call_mom1
    "" ".."
    show screen incoming_call_mom1
    "" "I.. I can barely open my eyes.."
    show screen incoming_call_mom1
    "" ".."
    show screen incoming_call_mom1
    "" "Someone.."
    show screen incoming_call_mom1
    "" ".."
    show screen incoming_call_mom1
    "" "mom is calling.."
    show screen incoming_call_mom1
    "" "I.. {w=1.0} I need to answer."
    # Call incoming call screen
    $ result = renpy.call_screen("incoming_call_mom")

    label mom_accept:
        if result == "accept":
            jump isekai_scene

        else:
            jump isekai_scene

label isekai_scene:
    hide screen incoming_call_mom1
    stop sound
    "..."
    "I guess I'm dead."
    "[mom].. [sis].. My friends.."
    "and.."
    "[omi].. I'm sorry I let you down.."
    "I truly am the worst person ever."
    mc "Ugh.. Fuck.."
    mc "..."
    "My body feels light."
    "Like I've been somewhere inbetween sleeping and falling"
    "...[mcln]."
    ".."











#error here instead of returning to main menu properly
    return
        
        



# label monika_call:
#     hide screen creepy_blue_screen
#     "" "I received a call from my phone."
#     "" "It's Monika."
#     $ result = renpy.call_screen("incoming_call")
#     if result == "accept":
#         jump monika_accept
#     else:
#         jump monika_decline

    #DIALOGUES FOR STORE END HERE

    #MC DEATH SCENE STARTS HERE

