#ALL SCRIPT GO HERE

#declare all characters here
#can change color of character names, declare here



#declaration for phone scene
default gallery_done = False
default contacts_done = False
default docs_done = False


# #MAIN CAST
# default player_name = ""

define a = Character("???") #placeholder for unknown
define mc = Character("[player_name]") #original mc
define mcln = Character("[last_half_name]") #half of player name
define mc2 = Character("C|�Nf") #unofficial name, the isekai'd new body of mc

    #FAMILY
define mom = Character("Mom") #mc and mc2 mom
define dad = Character("Dad") #dead from both mc and mc2 world
define sis = Character("Mika") #mc and mc2 sister

    #important to plot
define kel = Character("Kiel") #mc bestfriend, mc2 classmate (something went wrong)
define hari = Character("Hari") #m (basilo bestfriend)
define bas = Character("Basilo") #m (hari and basilo best friends who compete for Chika)

define omi = Character("Omi") #m but femboy #HEROINE

define chi = Character("Chika") #f the beautiful shy girl #HEROINE
define bg = Character("Book girl")

define wagi = Character("Waguri") #f #HEROINE

#define ros = Character("Rosie") #f no art NPC
#define yui = Character("Yui") #f (wagi, ros, yui are childhood friends) no art NPC
    #SIDE CHARACTERS USELESS FOR MOST PART
define Rei = Character("Rei") #f class president
define ich = Character("Ichika") #f classmate
define paul = Character("Paul") #m school delinquent

define chu = Character("Chuuya") #f chuunibyou a cheerful, lively, very pleasant girl, much like Sayori (no depression) someone who dies later on (pretends to be important character early in the story) (this ending for her depends on the story flow and route)
define epg = Character("Eye patch girl")
#define ari = Character("Ari")#f cHUUYA's friend NPC

define ku = Character("Kuro")#m the otaku




#NPCs
define s = Character("Convenience store staff")
define cm = Character("Classmate")
define npc = Character("Stranger")
define td = Character("Truck Driver")
define t = Character("Teacher")
define p = Character("Professor")

#declare image bg resolutions here
image bg MC_room = im.Scale("bg MC_room.png", 1920, 1080)
image bg kitchen = im.Scale("bg kitchen.png", 1920, 1080)
image door = im.Scale("bg door_day.png", 1920, 1080)
image dooraft = im.Scale("bg door_sunset.png", 1920, 1080)
image doorn = im.Scale("bg door_night.png", 1920, 1080)
image livingroom = im.Scale("livingroom.png", 1920, 1080)
image livingroomn = im.Scale("livingroomn.png", 1920, 1080)
image bg street = im.Scale("bg street.png", 1920, 1080)
image bg streetaft = im.Scale("bg streetafternoon.png", 1920, 1080)
image bg streetn = im.Scale("bg streetnight.png", 1920, 1080)
image bg convenience store = im.Scale("bg convenience store.jpg", 1920, 1080)
image bg city = im.Scale("bg city.png", 1920, 1080)
image bg cityaft = im.Scale("bg city_aft.png", 1920, 1080)
image bg cityn = im.Scale("bg city_night.png", 1920, 1080)
image bg arcade = im.Scale("bg arcade.jpg", 1920, 1080)
image bg arcade2 = im.Scale("bg arcade2.jpg", 1920, 1080)
image bg street2 = im.Scale("sidestreet.png", 1920, 1080)
image bg street2aft = im.Scale("sidestreet_afternoon.png", 1920, 1080)
image jumpscare = "images/jumpscare.png"
image bg sayonara = im.Scale("bg sayonara.png", 1920, 1080)
image monika = "images/monika.png"
image truck = im.Scale("images/truck.jpg", 1920, 1080)
image crash = im.Scale("images/black.png", 1920, 1080)
image mc2room = im.Scale("mc2room.png", 1920, 1080)
image bathroom = im.Scale("bathroom.png", 1920, 1080)
image mchallway = im.Scale("mchallway.png", 1920, 1080)
image mchallwayn = im.Scale("mchallwayn.png", 1920, 1080)
image roof = im.Scale("roof.png", 1920, 1080)
image roofaft = im.Scale("roof_aft.png", 1920, 1080)
image roofn = im.Scale("roof_night.png", 1920, 1080)
image buildingstairs = im.Scale("stairs_mid_aft.png", 1920, 1080)
image scenewithomi = im.Scale("scenewithomi.png", 1920, 1080)
image schoolhall = im.Scale("schoolhall.png", 1920, 1080)
image classmorn = im.Scale("mcclassroom.png", 1920, 1080)
image classaft = im.Scale("mcclassroom_aft.png", 1920, 1080)
image courtyard = im.Scale("courtyard.png", 1920, 1080)
image courtyardaft = im.Scale("courtyard_aft.png", 1920, 1080)
image omiscene = im.Scale("scenewithomi.png", 1920, 1080)
image sky = im.Scale("sky.png", 1920, 1080)
image skyaft = im.Scale("sky_aft.png", 1920, 1080)
image skynight = im.Scale("sky_night.png", 1920, 1080)
image sgate = im.Scale("gate.png", 1920, 1080)
image sgateaft = im.Scale("gate_aft.png", 1920, 1080)
image cafe = im.Scale("cafe.jpg", 1920, 1080)
image cafeaft = im.Scale("cafe_aft.jpg", 1920, 1080)
image cafeout = im.Scale("cafe_outside_aft.jpg", 1920, 1080)
image library = im.Scale("library.png", 1920, 1080)
image libraryaft = im.Scale("library_aft.png", 1920, 1080)

image tomorrow = Movie(play="tomorrow.mp4", size=(1920, 1080), loop=False)
image tomorrow = Movie(play="tomorrow.mp4",  size=(1280,720), loop=False, xalign=0.10, yalign=0.10)

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

#transform night effect



#MUSIC DEFINE
init python:
    renpy.music.register_channel("sound", mixer="sound", loop=True)
    renpy.music.register_channel("sfx", mixer="sfx", loop=False)
    renpy.music.register_channel("sfx1", mixer="sfx1", loop=False)
    renpy.music.register_channel("sfx2", mixer="sfx2", loop=False)
    renpy.music.register_channel("sfx3", mixer="sfx3", loop=False)
    renpy.music.register_channel("sfx_loop", mixer="sfx", loop=True)
    renpy.music.register_channel("ambient", mixer="ambient", loop=True)
    renpy.music.register_channel("sfx4", mixer="sfx4", loop=True)






#others
screen dark_overlay():
    add Solid("#00000099")

#GAME START
label start:

    scene bg streetrain
    with fade

    $ player_name = renpy.input("A college student is passed out cramming in his room. What is his name?")
    $ player_name = player_name.strip()
    $ player_name = player_name.title()

# If player leaves it blank, set default
    if player_name == "":
        $ player_name = "Player"


    $ last_half_name = player_name[len(player_name)//2:]


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

    "" "She elbows you while grabbing her own breakfast and walking away."

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

    "" "The person standing in front of you is an old friend, Kel, we both used to hangout alot in high school."

    "" "After graduation, we kinda drifted apart."

    mc "Oh, hey, long time no see."

    kel "Nonchalant as always, huh?"

    mc "..."

    kel "Yeah, I figured."

    kel "Man, you wanna hangout after shift?"

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

    kel "Can I at least get your contact, man?"

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

    kel "Hey, what's going on guys."
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
    "" "[omi] follows them both into the arcade, leaving just you and [kel] behind."
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

    kel "Mm, sure.{nw}"
    $ renpy.sound.play("audio/ambient/phonering.mp3", channel="sound", loop=False)
    $ renpy.sound.set_volume(1, delay=0, channel="sound")

    kel "..."

    kel "Ah, I gotta take this."

    kel "You can play with [mc] instead."

    $ renpy.sound.stop(channel="sound", fadeout=3.0)

    omi "[mc]..?"

    "" "[kel] walks out the arcade to take that seemingly important phone call..."

    "" "..."

    mc "What do you wanna play Omi?{nw}"
    stop music

    "" "[omi] went off real fast by herself to the back corner of the arcade, where her favorite game is seemingly located."
    "" "She didn't even look back or tell you to come with her."

    mc "What's her deal?"

    "I immediately followed"
    scene bg arcade2
    with fade

    omi "No! Leave me alone!"

    omi "I already accepted the fact that you're gone.."

    omi "Why did you.."

    play music "my confession new.ogg" volume 0.8
    omi "Why did you have to show yourself back again?"

    mc "Oms..?"

    omi "NO! Don't you dare call me that again!"

    omi "You were.. you were my bestfriend.. you.. you left us{w=1}, and..{w=1} you left me!"

    omi "So suddenly.."

    omi "Tell me, [mc], why?{w=1} How could you do this?"

    "She starts sobbing really bad.{w=1} Good thing we're at the back of the arcade, or else the others will hear her."

    mc "[omi].."

    omi "I can't even look at you anymore. You look and act so much different now."

    mc "Omi… I… I never meant to hurt you."

    omi "Never meant to hurt me? Do you even hear yourself? You disappeared without a word! Just… gone!"

    "Her hands tremble as she clutches the edge of the arcade machine, eyes glossy with tears."

    mc "I had… reasons. Things I couldn’t control… but I always thought—{nw}"

    omi "Thought what? That everything would be okay if you just left? That I wouldn’t notice?"

    "Her voice cracks, and she wipes at her face, trying to regain some composure, but failing."

    omi "You left me behind, [mc]. Everyone else… they moved on, but I stayed, waiting… hoping… for you to come back."

    mc "Omi… I never stopped caring. I just… I didn’t know how to come back to you, to us."

    omi "Us? There’s no ‘us’ anymore. You broke it. You broke everything!"

    "She turns away, shoulders shaking. The arcade noises fade into a muffled background as her sobs echo in your chest more than your ears."

    "You really done it now this time, [mc].{w=1} You've made the most caring, affectionate—warmhearted girl cry."

    "What the fuck is wrong with you."

    "Now I feel guilty."

    "I think the others might have heard us by now."

    mc "Please… just… let me explain. I’m not the same person I was… but I’m here now."

    omi "…You’re here now? And that’s supposed to fix years of silence, of… loneliness?"

    mc "No… it doesn’t fix anything. I know that. But I want to try, if you’ll let me."

    "For a long moment, she doesn’t respond. The only sound is her shaky breathing and the faint beep of the arcade machine."

    omi "…You think it’s that easy?"

    mc "No… I know it’s not. But I’ll do whatever it takes to make things right… even if it takes forever."

    "She finally turns to you, her eyes red and raw, searching yours for any hint of the friend she once knew."

    omi "…Forever, huh? That’s a long time, [mc]. Are you even sure you can handle that?"

    "She chuckles while still being teary."

    mc "You know what?{w=1} Since everyone's doing their own thing, you wanna go outside somewhere?{w=1} You know, just to talk?"

    mc "That's if you want to or not"

    "Sigh"

    "Whatever cheers her up, guess I'll have to do this."

    "She seems hesitant as first but she eventually wipes her tears then nodded her head."

    omi "..Fine."

    "Thus, you've made your first step to earning her forgiveness."

    "You both quietly leave the arcade."

    stop music fadeout 1.0

    scene bg cityaft
    with dissolve
    #$ renpy.sound.play("audio/ambient/outdoors.mp3", channel="sfx_loop", loop=True)
    #$ renpy.sound.set_volume(1.0, channel="sfx_loop") #JOSH edit the mp3 file and make it loop friendly in audacity or something

    play music "rain.mp3" fadein 1.5

    "The noise of the arcade dies the moment the door shuts behind you."

    "Outside, the air feels cooler. Lighter. Like the world isn’t pressing down as hard."

    omi "…It’s weird."

    play music "Piece By Piece.mp3" fadein 1

    #play ambient bg noise here instead

    mc "What is?"

    omi "Walking next to you like this again."

    "She stuffs her hands into her jacket pockets, staring straight ahead."

    omi "Part of me wants to pretend nothing happened."

    omi "And another part of me wants to yell at you all over again."

    mc "Yeah… that sounds about right."

    "She lets out a small breath that almost sounds like a laugh."

    omi "You always were bad at comforting people."

    mc "Hey, I’m improving. Slightly."

    omi "Mmm. Debatable."

    "A brief silence settles between you—not awkward, but heavy."

    omi "You know… when you disappeared…"

    omi "I kept replaying our last conversation in my head."

    omi "Trying to figure out what I did wrong."

    mc "…You didn’t do anything wrong."

    "She slows her steps."

    omi "Then why did it feel like I was the one left behind?"

    mc "Because I was a coward."

    "She looks at you, surprised by how fast you said it."

    mc "I didn’t know how to face everyone. Especially you."

    mc "So I ran."

    omi "…Figures."

    "She exhales, long and shaky."

    omi "I don’t hate you, you know."

    omi "I just don’t know where to put you anymore."

    mc "Then… let me earn a place."

    "She stops walking completely."

    omi "This doesn’t mean I forgive you."

    mc "I know."

    omi "And I’m not promising anything."

    mc "I’m not asking for promises."

    "She looks at your face for a moment, then nods."

    omi "…Okay."

    "It’s small. Fragile."

    "But it’s real."

    "And for the first time since you returned"

    "You’re not walking alone anymore."

    "You both stop near a quiet convenience store [kel] works in,{w=1} its lights buzzing softly."

    omi "…Hey."

    mc "Yeah?"

    omi "I’m kinda hungry."

    "She says it so suddenly, like she just remembered hunger exists."

    mc "That’s what you took from that whole emotional scene earlier in the arcade?"

    omi "Hey! Crying burns calories!"

    "She smiles small, wobbly, careless, but real."

    "That smile hits harder than her yelling did."

    "That's weird, we only just hungout today and I'm already starting to notice details about her.."

    mc "You’re… doing okay?"

    omi "Mhm."

    "She pauses."

    omi "…Well, I mean, I’m functioning."

    "She laughs, a little too quick."

    omi "Which is basically the same thing, right?"

    mc "Not really."

    omi "Wow, okay. Straight for the throat."

    "She nudges you lightly with her shoulder."

    omi "But yeah… I’m okay."

    omi "I always am."

    "She says it casually."

    "Too casually."

    mc "You don’t always have to be."

    "She looks away, pretending to read a poster on the window."

    omi "Someone has to keep things light."

    omi "If I don’t, things get… heavy."

    mc "You’re allowed to be heavy sometimes."

    omi "Heh…"

    omi "You really did change."

    mc "Is that bad?"

    omi "…No."

    "She smiles again. Brighter this time."

    omi "It’s just… different."

    omi "Old you would’ve panicked and changed the subject by now."

    mc "Guess I’m learning."

    omi "Guess I’m… glad."

    "She steps inside the store first, holding the door open for you."
    stop music fadeout 1
    #$ renpy.sound.stop(channel="sfx_loop", fadeout=3.0)
    scene bg convenience store
    play music "Convenience store.mp3" volume 0.7

    omi "Come on."

    omi "You still owe me, remember?"

    mc "For what?"

    omi "For disappearing."

    "She says it lightly."

    "But she doesn’t let go of the door."

    mc "Come on, I'm buying you snacks now."

    omi "YAAAYYY!"

    "The moment we got in the store, I clenched at my wallet as I see her grabbing so much food."

    "You remember how much she actually likes to eat sweet stuff."

    "She's now heading your way carrying all the food she wants you to buy"

    omi "So.. this one's for you and this one's for me.{w=1} Ehe..."

    mc "Wow, you are so thoughtful, considering we're spending MY money.."

    omi "Ehehe.."

    "Oh well, since I wasn't going outside for a long time, my allowance did have kind of stacked up."

    "After you grab all the food in a paper bag, [omi] suggest you both eat at the rooftop of the arcade building."

    "You both exit the store and head back to the arcade."
    play music "Cinnamon.mp3" volume 0.7
    scene bg cityaft with dissolve
    scene bg arcade with dissolve
    "Your friends are all still playing, guess they really miss the arcade, huh."

    scene buildingstairs with dissolve

    scene roofaft with dissolve

    "We finally climbed up the stairs.{w=1} The rooftop is quiet."

    "Way quieter than the arcade below."

    "Ambience in the distance can be easily heard, and the city hum feels far away.{w=1} It really is so quiet up here."

    "Kinda chilly, but not too much. If anything, it's kind of comfortable."

    "Like I could sleep here right now."

    "I wonder how she feels about it up here.."

    omi "Wow…"

    omi "I forgot this place existed."

    mc "You forgot because you're always indoors eating sugar."

    omi "HEY!"

    "She plops down near the edge, legs dangling, already tearing open a snack."

    omi "This is why I brought you here."

    mc "For the view?"

    omi "Nope."

    omi "Because food tastes better when you're somewhere stupid."

    mc "That explains a lot about you."

    "She pouts."

    omi "Rude."

    "She hands you one of the snacks."

    omi "Here. Compensation."

    mc "For emotional damage?"

    omi "For buying everything I wanted."

    "You sit beside her."

    "For a moment, neither of you speaks."
    stop music fadeout 1

    omi "…You know."

    omi "Back then, I thought you'd come back."

    mc "Yeah?"

    omi "Every time I came here, I'd imagine you sitting right there."

    "She points to the spot next to you."

    omi "I even practiced what I'd say."

    mc "What was the line?"

    omi "Hmm…"

    "She smiles."

    omi "Probably something dumb."

    omi "Like… 'You're late.'"

    mc "Sounds like you."

    omi "Hey! That's..!"

    "She laughs, then quiets."
    play music "my feelings.ogg"

    omi "Seeing you actually here now feels… unreal."

    "The wind brushes past."

    "Her shoulder barely touches yours."

    "She doesn't move away."

    "Neither do you."

    omi "If this is a dream… don't wake me up yet."

    mc "It's not a dream."

    omi "You don't know that."

    mc "..."

    omi "..."

    omi "What if you just disappear again tomorrow?"

    mc "I won't."

    omi "You don't know that either."

    "She says it without heat."

    "Just quietly."

    "Like a fear she's been carrying around so long it doesn't even hurt to say anymore."

    "It just exists."

    "I'm afraid that she might be right.."

    mc "Then I'll just have to keep showing up until you believe me."

    "She goes quiet."

    "Picks at the edge of her snack wrapper."

    "Not looking at you."

    omi "..."

    omi "That's a very easy thing to say."

    mc "I know."

    omi "..."

    mc "I know, Omi."

    "Another silence."

    "But softer this time."

    "You look at her."

    "She's already looking at you."

    "Something sits in the air between you."

    "Heavy and warm and completely unspoken."

    "She looks away first."

    "Down at the city below."

    "Her jaw tightens slightly like she's swallowing something she decided not to say."

    omi "..."

    mc "Omi."

    omi "Don't."

    "She says it quietly."

    "Not harshly."

    "Just."

    "Not yet."

    mc "..."

    "You look back at the city too."

    "The lights are turning on now as the sun sets."

    "One by one."

    "Like the city is slowly becoming alive by itself."

    omi "..."

    omi "You know what's funny?"

    mc "What?"

    omi "I had this whole speech prepared."

    omi "For when you came back."

    omi "I spent so long thinking about what I'd say."

    mc "What happened to it?"

    omi "..."

    "She laughs once."

    "Small and tired and real."

    omi "I forgot it the second I actually saw you."

    omi "Whoops.. hehe.."

    mc "..."

    "You don't say anything."

    "There's nothing to say to that."

    "So you just sit there."

    "Together."

    "While the city lights come on one by one below you."

    omi "..."

    omi "I'm glad you're back."

    "She says it while looking at the sky."

    "Not to your face."

    "Like if she said it to your face it would mean too much."

    mc "Yeah."

    "You say it the same way."

    "While looking at nowhere in particular."

    "The moment passes."

    "But it doesn't leave."

    "It just settles between you like something patient."

    "Something that knows it has time."

    mc "Lets clean up."

    "[omi] looks visibly disappointed but ended up cheering up quickly."

    "She starts helping me clean up."

    "We eventually had to go down and meet with the others as the day was passing."

    scene bg arcade with dissolve




















    stop music fadeout 1.0






    mc "Hey guys, sorry we had some stuff to talk about."

    "You notice that [omi] is sobbing."



    hari "Oi, who made our [omi] cry?{w=1} Who did it, [mc]? I'll make sure this asshole gets what's comin to em."

    bas "Yo,{w=1} what's going on here?"

    kel "Hey guys, what is—{nw}"

    omi "It's okay, guys, I just miss [mc] so much.{w=1} Hehe."
    play music "Cinnamon.mp3" volume 0.7

    hari "Good. I wouldn't want anyone making our [omi] cry."

    bas "You're so cringe, [hari]."

    hari "...Man, I just want to stand up for our friend"

    kel "..."

    "[omi] laughs carefree"

    kel "*Maybe now isn't the time to tell them about my news..*"

    "We all go quiet for a second."

    hari "Man… I gotta wake up at 6 tomorrow."

    kel "Same. Work’s been killing me lately."

    bas "Yeah… adult life kinda sucks. I have so much responsibilities once I'm back in my college dorm."

    mc "Heh… yeah…"

    "Omi goes quiet for a second"

    hari "Guys, we should take a picture. For memories."

    bas "Oh yeah, like old times!"

    "They all look at you."

    mc "Lets do it."

    bas "Wow,[mc] is no longer afraid of cameras?{w=1} Shocker."

    kel "Haha, he actually used to act allergic to cameras all the time."

    hari "Yeah, I had to grab and forcefully bring this guy to our photos."

    "Omi chuckles once again."

    mc "Hey, come on{w=1}. Lets just get this over with"

    "[omi] glances at you subtly"

    "You decide to stand next to [omi] in the picture.{w=1}. You swear you just heard her giggle."

    "Once the picture gets taken, you all decide to finally part your ways."

    stop music
    scene bg cityaft with fade

    "Heh, can't believe I took them for granted."

    "Today was awesome."

    "Why did I ever even take them for granted..?"

    "Oh right.. that incident.."

    "But screw that, that's past now."

    "From this day forward, I shall finally put my life back together!"

    "Watch out, world! [mc] is back in town!!"

    "I'll fix everything!{w=1} Yeah!!"



















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
    "" "The Truck finally hits my body..{nw}"
    hide screen film_grain_effect
    "" "Augh!{nw}"
    with vpunch
    stop music
    $ renpy.sound.play("audio/ambient/carsqueel.mp3", channel="sfx")
    scene black
    $ renpy.sound.set_volume(2, delay=0, channel="sfx")
    with vpunch

    pause 1

    $ renpy.sound.play("audio/ambient/car_alarm.mp3", channel="sfx2")
    $ renpy.sound.set_volume(0.5, channel="sfx2")


    $ renpy.pause(3, hard=True)
    "{nw}"

    scene crash #OPTIONAL maybe put blood overlaying on screen, maybe put red and blue effects to simulate police sirens too
    window hide

    $ ambient.play("audio/ambient/heart.ogg")

    $ renpy.sound.play("audio/ambient/earringing.mp3", channel="sfx", loop=True) #Josh edit the mp3 file, make it loopable
    $ renpy.sound.set_volume(0.5, channel="sfx")

    $ renpy.pause(5, hard=True)

    "Ugh.."



    show screen incoming_call_mom1



    $ renpy.sound.play("audio/ambient/peoplescreaming.mp3", channel="sfx_loop", loop=True)
    $ renpy.sound.set_volume(0.5, channel="sfx_loop")





    "" "mom?"
    show screen incoming_call_mom1


    a "AHHHHHH!"

    a "Somebody call an ambulance!!"

    a "Oh my god this kid is done for.."

    show screen incoming_call_mom1
    "" "..."

    a "Everybody, PUSH!"



    $ renpy.sound.play("audio/ambient/phonering.mp3", channel="sfx1")
    $ renpy.sound.set_volume(0.5, channel="sfx1")

    show screen incoming_call_mom1
    "" "mom..."

    a "Oh lord help this man.. His guts are everywhere.."

    a "I-I can't look!"
    show screen incoming_call_mom1
    "" "..."
    show screen incoming_call_mom1
    "" "..."
    $ renpy.sound.play("audio/ambient/police.mp3", channel="sfx3")
    $ renpy.sound.set_volume(0.5, channel="sfx3")

    show screen incoming_call_mom1
    "" "Aughh.. fuck.."
    show screen incoming_call_mom1
    "" "It hurts.."

    a "Get the stretcher!"

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
    hide screen film_grain_effect

    #ISEKAI!!!
    $ renpy.sound.stop(channel="sfx", fadeout=3.0)
    $ renpy.sound.stop(channel="sfx1", fadeout=3.0)
    $ renpy.sound.stop(channel="sfx2", fadeout=3.0)
    $ renpy.sound.stop(channel="sfx3", fadeout=3.0)
    $ renpy.sound.stop(channel="sfx_loop", fadeout=3.0)
    $ renpy.sound.stop(channel="sound", fadeout=3.0)
    $ renpy.sound.stop(channel="sfx4", fadeout=3.0)
    $ ambient.stop()
    "..."

    "I guess I'm dead."
    "[mom].. [sis].. My friends.."
    "and..{w=1} [omi]..{w=1} I'm sorry I let you down."
    "I truly am the worst person ever."
    "I'm so sorry, everybody."
    "God please, give me a second chance."
    "I swear I'll fix everything"
    "I need{w=1.0} No.. I want to do it all again!"
    "I want to fix my life!"
    "Please.. if there even is a divine being out there.."

    $ renpy.sound.play("audio/ambient/whispering.mp3", channel="sfx")
    $ renpy.sound.set_volume(0.5, channel="sfx")
    "Give me a chance.. I beg you.."
    "I'll.. do anything."

    mc "Ugh.. Fuck.."

    $ renpy.sound.play("audio/ambient/buildup.mp3", channel="sfx1")
    $ renpy.sound.set_volume(0.5, channel="sfx1")

    mc "..."
    "My body feels light."
    "Like I've been somewhere inbetween sleeping and falling"
    "...[mcln]."
    "[mc]!"
    mc "Huh? What?"
    a "You're gonna be late for school!{w=1.0} Wake up!"
    "Strange.. Why do I feel fine."
    "I open my eyes"
    scene mc2room

    "..."
    ".."
    ".."
    "What the..?"
    "Where am I?{w=1.0} Who's room is this??"
    "And who is that calling me?"
    "I try to stand up from the bed I've been laying in that I do not recognize at all."
    "No..{w=1} I don't even recognize anything here."
    "The moment I tried to stand up, I almost fell infront of me {w=1} I feel light as hell that it's actually disorienting."
    mc "Crap.. I need to vomit."
    "I went out the bedroom to look for the bathroom. Thankfully, it was just across the hall and conveniently open with no one inside."

    scene mchallwayn with dissolve
    show screen dark_overlay
    scene bathroom with dissolve
    $ ambient.play("audio/ambient/rain.mp3")#ambient
    $ renpy.pause(3, hard=True)
    #water, washing sfx here
    $ ambient.stop()


    "I look at the mirror to wipe my face."

    "..."

    "I stop."

    "..."

    "What the fuck?"

    "That's not my face.."

    "I know that's not my face."

    "But my brain keeps trying to make it make sense."

    "Like if I stare long enough it'll just.."

    "Fix itself.."

    "Is this some sort of sick dream?!"

    "A sick social experiment??"

    "..."

    "It doesn't fix itself."

    "I raise my hand."

    "He raises his hand."

    "I turn my head."

    "He turns his head."

    "Every single time."

    "Every single time I move he moves with me and it's wrong."

    "It's so wrong."

    "The face is wrong and the shoulders are wrong and even the way the light hits is wrong because this isn't my bathroom and that isn't my face and I am."

    "I am."

    "..."

    "Okay."

    "Okay okay okay."

    scene black with fade

    "Breathe, [mc], Breathe.."

    "What is this.."

    "WHAT THE FUCK IS THIS?!"

    "Must be some hallucination after that fucked up accident."

    scene bathroom with dissolve

    "I grip the sink."

    "The reflection also grip the sink."

    "God.."

    "I look down at the drain instead."

    "That's easier."

    "The drain looks the same as any drain."

    "Just a drain."

    "I focus on that for a second."

    "The drain is also just a drain."

    "I look at my reflection again."

    "..."

    "Okay."

    "I'm dead."

    "I think I'm dead."

    "Or I'm dying."

    "Or this is what dying looks like from the inside."

    "Or."

    "..."

    "I don't know."

    "I genuinely don't know what is going on.."

    mc "Just.."


    a "[mc], hurry up or your sister will eat your breakfast!"

    "..."

    "That voice."

    "I know that voice."

    "Why do I know that voice."

    "The bathroom door slowly creaks open."

    show mom happy at right
    with moveinright
    play music "Family bonds.mp3" volume 0.8

    mom "Hey what are you doing in there?"

    "My mom."

    "That's my mom's voice coming out of a person who."

    "Who is looking at me like I'm her son."

    "..."

    "Say something."

    "Say literally anything."

    mc "Uh."

    "Great."

    mc "Yeah.. I'm gonna catch you guys soon."

    "She looks at me for a moment."

    "I don't know what my face is doing right now."

    "I have no idea what expression this face makes when it's scared."

    "I don't know this face."

    mom "Well alright then, don't take too long, you already know your sister."

    hide mom

    "She leaves, mumbling something about 'these kids nowadays'."

    "I turn back to the mirror."

    stop music

    "The reflection turns back with me."

    "..."

    "I have to go out there."

    "I have to sit down and eat breakfast with my mom."

    "Except.."

    "..."

    "Except nothing."

    "I have to go out there."

    "One thing at a time, [mc]."

    "Just.."

    "One thing.."

    "...At a time."

    ".."

    "No.."

    mc "Holy fucking shit."

    "I can't think straight.."

    "This isn't happening.."

    "This CANNOT be happening.."

    "I slap myself real hard it echoed the whole bathroom."

    "Okay, I don't know what the hell is going on but I need to figure something out."

    "..."

    "Wait."

    "Could it be that this is an ISEKAI?"

    "Like in anime?"

    "Like something or someone must've reincarnated me into this world or something.."

    "That has to be it, right? It has to be!"

    mc "I mean what other options do I have other than panic?"

    "I should.. try and look around for now before I go downstairs."

    mc "And maybe just play along for now until I gather more information about this place."

    hide screen dark_overlay
    scene mc2room with dissolve
    play music "phantom shadow.mp3" volume 0.8
    "I went back to 'my room' to look around for things."
    #put unsettling music here

    mc "I don't know this room but somehow it looks familiar. Wait, is that what I think it is..?"

    "There's a family picture on the wall, you can see 'Yourself', [sis], and [mom].{w=1} There are other pictures with people that you know,{w=1} games you've played,{w=1} and even the school you used to go to.."

    "Staring at all of it in disbelief, I started to slowly back away and ended up knocking some things from my shelf, hitting me in the head."
    with vpunch

    mc "Oww.. God damn it.. Do I own a pet rock or something?"

    "I stare at what hit me, it is 'my phone'."

    show screen incoming_call_mom1
    "put phone feature here, shows home ui (atleast contacts, files app, and gallery should be visible)"


    #phone

    mc "...Jackpot."

    mc "This should help me get more information about whatever is going on."

    mc "Le—{nw}"
    stop music

    a "Jeez, [mc], I'm getting hungrier looking at your untouched food."
    hide screen incoming_call_mom1
    show sis happy at left
    with moveinleft
    play music "Smiling Weekends.mp3" volume 0.8
    "The girl who just barged into my room is what seems to be my sister."

    sis "Oh and by the way mom told you to come downstairs now."

    mc "Just take it."

    sis "Wait, really?"
    show sis happy at run_left

    "I blinked once and she was already running downstairs for my food."

    sis "Mom!!! [mc] said I could have it!!"

    "Sigh.{w=1} I should probably head downstairs myself."
    scene bg kitchen with dissolve

    mom "About time you finally went downstairs."

    mom "[sis] said that she can have your food, is that true?"

    mc "Yeah, don't worry [mom], I'm not that hungry today."

    "Not that I have an appetite to eat anyway after what just happened to me a moment ago."

    "What did I overhear? My guts were everywhere?"

    "I somehow didn't feel it all that much. Guess that's what adrenaline does to you."

    sis "See?? I told you he said I could have it!"

    mom "Honey, you tried pulling this off so many times on your brother just so you can steal his food."

    sis "Hehe.."

    "..."

    mc "Uh. Hey. Strange question but do I have class today?"

    mom "Of course you do."

    mom "Why would you even ask that?"

    "This doesn't sound good.."

    mc "No reason. Just not feeling it today."
    stop music


    scene schoolhall with fade

    "The moment I said that sentence, my mom picked me up to her car and drove me here before I can even finish breakfast."

    "Just great."

    "Guess I'll have to navigate my way through this world's school."

    scene black with fade

    "Lets see.. So first I have to figure out who I apparently know in this world, their names, and maybe try and gather more information about who I am here."

    "What I do find interesting is how some people from my world are also in this world."

    "I should probab—{nw}"

    a "Look who finally decided to show up."
    hide scene with fade

    scene schoolhall
    show wagi at center
    play music "Happenings.mp3" volume 0.8 #change this into a tense or deliquent style music

    mc "…"

    "Why are they staring at me like that? Did I… walk in weird or something?"

    a "Hey, are you new here or something?"

    mc "Uh… yeah… new… I guess?"

    "You are trying to act normal but the others feel like it is way too confident. It's unsettling to everyone around."

    "Two girls are standing near the lockers. One's got a sharp gaze, the other is fiddling with her hair nervously."

    a "He's really acting dumb, [wagi]."

    "It seems like one of them is called [wagi]."

    wagi "H-h-yeah!"

    wagi "Come on, [mc], you know the rules."

    wagi "This is our spot and if we catch you.."

    "Huh, they apparently know me. Its best that I play along."

    a "[wagi], should I teach this loser a lesson, don't you think?"

    wagi "..."

    "The school bell rings and the hall has erupted into chaos."

    mc "…Right. I'll see you guys around."
    show wagi at run_right

    "I dart down the hall, heart racing but oddly calm."

    "Crap, I thought I could wing it today.."

    "Who the hell are these girls?"

    "What kind of stuff has this dude's body been up to.."

    "Hm, speaking of which.. What happened t-"

    a "Watch out!!{nw}"

    mc "Ah!"
    with vpunch
    #bump effect and sfx here

    "While deep in thoughts, I ended up bumping into another girl carrying a stack of books."

    mc "Oh! Sorry, my bad—"

    a "Hey! Watch it, jerk…! were you always this clumsy?"

    mc "Uh… yeah… clumsy, but barely surviving."

    "You both pause awkwardly."

    "She looks at you strange and noticed her expression is familiar, but couldn't explain why."

    a "Thanks alot, jerk, now I have to organize all of these all over again!"

    "I was about to apologize but she ran off immediately."

    mc "Shit! I don’t even know where my class is!"

    "Out of nowhere, a tall, friendly looking guy appears beside me."

    a "Hey, relax. Follow me. You’re in my class."

    "Wait what the hell..?"

    mc "[bas]..?"

    bas "Of course, the one and only. Come on, we're gonna be late, man."

    "I finally breathe a sigh of relief and follow [bas], grateful for at least one familiar face in this confusing world."

    "I glance behind me and spot [wagi] and her friend still looking at me with a weird look on their eyes."

    scene classmorn with dissolve
    play music "Student heart.mp3" volume 0.8

    mc "So this is my class.."

    "The moment I took a seat, I immediately started scanning the room for any helpful info that might help me later."

    "I first checked out the classroom itself. Seems pretty standard, there's a TV on top of that shelf filled with books, and there's a bulletin board infront of the class near the door."

    "I might as well check that out later for some info about schedules or whatever."

    "Now my classmates.. Apart from [bas], it seems like he's the only person I know in this class. I wonder who else also exists here who were from my old world, too."

    "There's a dude at the back with headphones in while immersed in something." #Kuro the otaku

    "There's these two girls talking to each other, one of them moves and looks so weird and immature.. What's up with the eyepatch?" #Ichika the class gossip and Chuuya the class chuunibyou

    "Then one girl in the corner quietly reading a book alone." #Chika the introvert

    "Oh, and there's a crowd left side from where I sit, seems like they're crowding over that one girl while asking general class stuff. I'm assuming the class president?" #Rei the president

    "I look at the back and see Basilo and an empty seat that belongs to someone not there yet at Basilo's right side."

    ".."

    "Gah, all this analyzing is giving me a headache."

    bas "Dude, you good? you seem a little out of it today."

    mc "Me? Oh yeah totally fine. Just never had breakfast today."

    bas "Yeah you're totally out of it."

    bas "You're sitting in [paul]'s spot. Of all people."

    "Who the hell is Paul? Better yet, where the hell is my seat?!"

    menu:
        "Who is Paul?":
            jump paul
        "Where is my seat?":
            jump seat

label paul:
    a "Get out of my seat."
    "..?"
    bas "Oh no.."
    paul "You wanna taste a beating so early in the morning?"

    bas "[paul], Please, my dude's really out of it today."
    "[paul] punches the table of the seat I'm sitting in while pointing at what I'm assuming to be my seat."
    mc "Okay okay, I'm sorry man."
    mc "Just had a rough night, okay?"
    paul "..!"
    mc "I'm getting out your seat, alright?"
    paul "..."
    "[paul] let me go for me to go to my supposed real seat."
    "That went smoothly than I expected."

    jump paulseat

#put boss music or sfx on paul encounter
label seat:
    "I can't believe I'm about to ask such a stupid question to [bas]."
    mc "Hey [bas]-"
    a "Get out of my seat."
    "..?"
    bas "Oh no.."
    paul "You wanna taste a beating so early in the morning?"
    bas "[paul], Please, my dude's really out of it today."
    "[paul] punches the table of the seat I'm sitting in while pointing at what I'm assuming to be my seat."
    mc "Okay okay, I'm sorry man."
    mc "Just had a rough night, okay?"
    paul "..!"
    mc "I'm getting out your seat, alright?"
    paul "..."
    "[paul] let me go for me to go to my supposed real seat."
    "That went smoothly than I expected."

    jump paulseat



label paulseat:
    bas "How did you do that?"
    mc "No idea."
    "Time passes for a while and the teacher seems to be late today."
    a "Interesting.."
    "The teacher finally arrived and everybody started rambling for their seats."
    t "Alright! Settle down everybody! Today we're-"

    scene black with fade

    "I space out until the class is over."

    scene schoolhall with dissolve

    "That class ends."

    "I find an empty corner of the hallway."

    "Just for a second."

    "I look at my hands."

    "This body's hands.."

    "..."

    "Yesterday I was going to fix my life."

    "I had this whole plan."

    "I was going to wake up tomorrow and actually start."

    "And now."

    "..."

    "Now I'm in someone else's hands looking at someone else's school trying to remember if I actually died or if I'm still dying or if this is something else entirely."

    "And I can't even.."

    "I can't even call my mom."

    "My actual mom."

    "..."

    "The bell rings."

    "I push off the wall."

    scene black with fade
    $ renpy.pause(2, hard=True)

    "I have to keep moving."

    stop music
    scene courtyard with dissolve
    play music "Free time.mp3" volume 0.8
    "I can't believe I bluffed my way till half the day."

    bas "Dude, be honest with me, are you actually okay?"
    "..!"
    mc "Yeah, honest. You seriously need to stop bugging me about it."
    bas "Jeez, sorry, just worried about you here."
    a "Did somebody say 'Hari'?"
    bas "[hari]!"
    hari "What's up bros."
    bas "Why were you absent this morning?"
    hari "Duh, someone had to take care of the cafe, plus I took the shift because the first week of the school semester means more customers means more tips."
    hari "It's just math, [bas], math."
    bas "Whatever. Hopefully messing up your grades is worth the four hours worth of money."
    hari "It is, check it out."
    "[hari] shows off all the tips he's received so far infront of [bas]."
    hari "Oh? Didn't notice you were with [mc]. What's up, man?"
    "I look and point at him."
    hari "Alright looking good."
    hari "Uh, I think I'm about to head out. My lunch break's almost over."
    hari "See you guys later at the cafe!"
    "Me and [bas] watch [hari] walk away then started sprinting."
    bas "Heh, too bad the cafe's lunch break isn't as long as ours, am I right [mc]?"
    mc "Uh, yeah. By the way what classes do we have next again?"
    mc "And who's gonna be our teacher for the day?"
    mc "Also do we have anything due soon?"
    bas "Woah, [mc], slow down."
    bas "Our next class is gonna be physics, after that is english. I don't think you've met the physics teacher yet so let me warn ya, she's a crazy lady, try not to stand out too much."
    bas "I believe that's all gonna be our remaining classes after lunch break."
    "I take mental notes and clock it in then gathered the info through my phone."
    mc "What's-{nw}"
    "Wait, I've already gathered decent information."
    "I don't think asking everything would be a wise move. I gotta play this safe."
    "I'm already in a messed up situation, wouldn't wanna dig myself in a deeper hole."
    mc "Got it. Thanks, man."

    bas "Oh, we should probably finish and clean up now. Class is about to start."
    mc "Right behind you."

    scene sky with fade
    "I spend the rest of the day talking to [bas], even almost got kicked out of class by the crazy physics teacher."
    $ renpy.pause(2.0, hard=True)
    scene skyaft with dissolve
    "[bas] ended up getting mad at me, but he forgave me anyway."
    $ renpy.pause(1.0, hard=True)


    scene sgateaft with fade
    play music "Daijoubu.mp3" volume 0.8
    "Just like that, I've survived my first day at school in this world."
    mc "Phew, what a day."
    scene black with fade
    mc "[bas] told me he's gonna work his shift at the cafe so he head out first."
    mc "Totally fine by me, though, I still don't know where this supposed 'cafe' is at."
    mc "Great one more thing to look for."
    a "[mc], you truly are something else, are you?"
    "Wait, did I just say my thoughts outloud?"
    scene sgateaft with fade

    show ich happy at center #FIND WAY TO MAKE SPRITE FADE IN THE SAME TIME WITH THE SCENE FADE
    show ich happy at center with easeinleft
    a "Hahaha!"
    show ich happy at left with easeinright
    show ich happy at right with easeinright
    "Who the hell is this?"
    a "First you act different in class, now you're also talking to yourself?!"
    a "That's comedy gold!"
    a "Can't wait to gossip this with everyone else!"
    mc "I'm sorry? Who do you think you are?"
    a "Ahem, hello? [ich]? Your classmate and class news provider or in other words gossip queen?"
    ich "It feels like an insult for you to even say that."
    ich "Jeez, what kind of revelation have you made that made you act differently, [mc]?"
    "Why the hell does everyone in school even know this guy?"
    mc "Yeah, got a problem with that ?"
    ich "Ha.. {w=1} Hahah.. {w=1} Hahahahhah!"
    "She grasps me at my shoulder with both her hands while laughing."
    ich "Oh boy, you really are something..!"
    ich "Fine, I guess after almost getting kicked outta class earlier, I'll give you a break!"
    ich "See you around, you strange boy!"
    show ich at run_left
    "..."
    "Wait, I don't even know which way is home."
    "Oh well, this path looks familiar."
    scene bg streetaft with fade
    stop music

    "I somehow found myself back home after looking lost for about thirty minutes."
    scene dooraft with fade

    scene livingroom with dissolve #make new image or code image in way that makes it look like afternoon/sunset time
    mc "I'm home.."
    "No one is home yet, but there is a note on the table on the fridge"
    "'[mc], the lasagna in the black container is for you, and [sis] the pasta on the plate is for you and please don't touch [mc]'s food.'"
    "I take the lasagna out the fridge along with a soda and bottled water."
    mc "This guy's family is rich.. Damn.."
    "After eating all of it in the kitchen and cleaning up, I head back to my room."
    show black with fade
    show screen dark_overlay
    scene mc2room with dissolve
    show screen dark_overlay

    "I survive day one. Barely. I finally have a moment alone to process everything and go through this guy's phone properly now that I have context for some of the names in it."
    "Lets see.. gallery, contacts, government documents.."
    "I should have enough time now that I'm alone with no interruptions.."


    play music "creepysus.mp3" volume 0.8
    show screen incoming_call_mom1 #placeholder for now, no phone feature yet

    menu:
        "Gallery":
            jump gallery
        "Contacts":
            jump contacts
        "Government documents":
            jump docs


label gallery:


    "I open the gallery."

    "Recent photos first."

    "School stuff. Food. Random city shots."

    "Nothing out of the ordinary so far."

    "He apparently documented his life more than I ever did."

    "I keep scrolling back."

    "There's a photo of the cafe [hari] and [bas] work at."
    "A group shot at what looks like a school festival."
    "A blurry photo of what looks like a cat."

    "The further back I scroll, the more familiar everything looks."

    "Too familiar."

    "I recognize these streets."
    "These places."
    "These people."

    "I stop at one photo."

    "It's the rooftop."

    "'Me' sitting alone up there. Same view of the city I know."
    "Same spot."

    "..."

    "I keep scrolling."

    "Then I stop completely."

    "..."

    ".."

    "."

    "No way."

    "I'm looking at a group photo."

    "Everyone is there."
    "[hari] with his arm around [bas] who looks like he's tolerating it."
    "[kel] slightly apart but smiling."
    "And [omi]."

    "Smiling the way [omi] smiles when something is genuinely good."

    "Standing next to someone."


    "Standing next to.. 'me'."

    "Same position."
    "Same spot."
    "Same everything."

    "Except that's not my face."

    mc "..."

    "I know this photo."

    "I was IN this photo."

    "I stood exactly where he's standing."
    "Right next to [omi]."
    "The group photo from that day."
    "My last day."

    "Except I'm not in it."

    "He is."

    mc "What the hell is this."

    "I put the phone face down on the bed."

    "..."

    "I pick it back up."

    "I stare at it again."

    "Same photo. Same people. Different face where mine should be."

    "My hands are steady."
    "I notice they're steady and I don't know why."

    mc "..."

    "I close the gallery."

    $ gallery_done = True
    jump phone_menu


label contacts:


    "I open the contacts."

    "Scrolling through."

    "Most names I recognize now from school."
    "[bas]. [hari]. Some classmates I haven't talked to yet."

    "Most of their conversations are mostly casual stuff."
    "Some banter here and there but nothing too crazy."

    "A few names I don't recognize at all."
    "Filed away for later."

    "One contact with no name."
    "Just a number."
    "No context."

    "I note it."

    "Then I find [kel]'s contact."

    "I open the message thread."

    "..."

    "It starts normal enough."
    "Casual back and forth. Easy energy."
    "The kind of conversation you have with someone you're actually comfortable with."

    "But then it starts thinning."

    "'My' messages getting shorter."
    "Longer gaps between responses."
    "One word answers where there used to be paragraphs."

    "And then."

    "One last message from 'me'."

    "I read it."

    "..."

    show screen incoming_call_mom1
    "Maybe you should just leave me alone."

    "It's short."
    "Vague, even."
    "The kind of message that ends something without saying it's ending something."
    "It did not leave me anything to work with."

    "[kel] never replied."

    mc "..."

    "I scroll back up and read through the whole thing again."

    "The shift in tone is gradual at first."
    "Then sudden."
    "Like something happened between these two messages that the chat doesn't show."

    "I don't know what this guy did."

    "But whatever it was."

    "[kel] never replied."

    mc "What did you do, man."
    hide screen incoming_call_mom1
    "I close the messages."


    $ contacts_done = True
    jump phone_menu


label docs:


    "I open the government documents folder."

    "Birth certificate. School enrollment records. Medical history. Insurance documents."

    "Standard stuff."


    "I open the birth certificate first."

    "[player_name] [mc2]."

    "Birth date: 14/03/93"

    "My father's name seems to have been faded through time."

    "The document file looks old. Looks like they don't have modern digital copies and its just a picture taken from the paper itself."

    "..."

    "Wait."

    mc "Hold on."

    "I read it again."

    "Same last name."

    "My last name."

    "..."

    "Okay. Okay that could be a coincidence."
    "It's not a rare name."
    "That doesn't mean anything."

    "But I can't help but wonder.."

    "Why are some things the same but the details are completely different?"

    "I open the school enrollment records."

    "Everything looks standard."
    "Name. Age. Year level. Emergency contacts."

    "It's even in my same old middle school, too."

    "I scroll to emergency contacts."

    "Mom's name."

    "Same as my mom's name."

    "..."

    mc "That's..."

    "I close that and open the medical history."

    "Routine checkups. Standard stuff."

    "But there's one entry near the top."

    "A note from a doctor."
    "Dated recently."

    "Patient presents with fatigue and irregular sleep patterns consistent with extended periods of inactivity."
    "Physical examination: Normal."
    "Mental evaluation: Normal."

    "Recommended increased physical activity and social engagement."

    "Patient is advised to spend more time outside."

    "Prescribed meds are advised to be taken on time."

    "I look at the prescribed meds."

    "It's mostly vitamins."


    "..."

    "I read that last line three times."

    mc "Spend more time outside."

    "..."

    "I was told the same thing."

    "By my actual doctor."

    "In my actual world."

    "Word for word."

    mc "This isn't a coincidence."

    "None of this is a coincidence."

    "Same last name."
    "Same mom's name."
    "Same doctor's note."

    "This isn't someone else's life."

    "This is my life."

    "Wearing a different face."

    "I put the phone down."

    "Stare at the ceiling."
    $ docs_done = True
    jump phone_menu


label phone_menu:
    "..."

    menu:
        "Gallery" if not gallery_done:
            jump gallery
        "Contacts" if not contacts_done:
            jump contacts
        "Government documents" if not docs_done:
            jump docs
        "Put the phone down" if gallery_done and contacts_done and docs_done:
            jump phone_complete


label phone_complete:
    stop music fadeout 2.0

    "I put the phone face down on the bed."

    "The room is quiet."

    "I lie back and stare at 'my' ceiling."

    "Same last name."
    "Same mom."
    "Same doctor's advice."
    "Same group photo."
    "Same people."
    "Different face."

    "I've been treating this like an isekai."
    "Like I just happened to land in some random parallel world."

    "But this isn't random."

    "Every single thing in this world is built from something I know."
    "Something I lived."
    "Something I remember."

    "Which means one of two things."

    "Either this world was constructed specifically for me."

    "Or."

    "..."

    "I don't finish that thought."

    "Not tonight."

    "Tonight I survived day one."
    "I have enough to think about."

    "I close my eyes."

    "I don't sleep for a long time."

    "But.."

    scene black with fade

    "The body can only sustain exhaustion for so long.."
    "..."
#play next day
    hide screen dark_overlay
    scene bg MC_room with fade
    "Ugh.."

    play music "DDLC bgm.mp3" volume 0.8
    "Wait what the fuck?"
    "I'm home??"
    mc "Oh, I gotta get moving.. maybe I should start with some breakfast."
    scene bg kitchen with dissolve
    play music "Family bonds.mp3" volume 0.7

    #put mom art here

    show mom happy at right

    $ ambient.play("audio/ambient/rain.mp3")#ambient

    with moveinright

    mom "Oh, you're up early, sweetie."

    mc "WhAT THE FUCK IS GOING ON?"

    mom "I was just kidding. Come eat, I got you your favorite!" #sprite no eyes

    mc "Mac and cheese again? Seriously?{nw}"
    #"God what an awful-{nw}"
    scene truck
    $ renpy.sound.play("audio/ambient/truckhorn.mp3", channel="sound", loop=False)
    $ renpy.sound.set_volume(1, delay=0, channel="sound")
    $ renpy.pause(0.75, hard=True)
    $ renpy.sound.play("audio/alarmclock.ogg", channel="sound", loop=True)
    $ renpy.sound.set_volume(1, delay=0, channel="sound")

    scene mc2room
    stop music
    mc "WHAT THE FUCK!"


    "God damn it."

    "I turn off the alarm."

    stop sound

    #DAY 2

    #Morning scene
    "I thought it was all just a dream. Damn it."

    "I got in my school uniform."


    scene bg kitchen with dissolve
    "Took a quick energy drink from the fridge and a slice of pizza from the table."

    scene door with dissolve
    "And headed to school."

    scene bg street2 with dissolve
    mc "I've survived a day and been doing pretty decently."
    mc "I already have a mental map of this place. I even know the route to school now."
    mc "Progress is looking good so far."
    "The school bell rings and students outside have started running to school. I do the same."
    scene sgate with dissolve
    scene classmorn with dissolve
    play music "Student heart.mp3" volume 0.8
    hari "Yo, what's up bro."
    mc "Oh hey, [hari]."
    "I settle on my seat"
    hari "[bas] not with ya?"
    mc "No, I came here alone actually."
    "Speak of the devil, [bas] came in while heavily breathing due to exhaustion."
    hari "I will always be faster than you!"
    bas "Haaah.. I just woke up late man, shut your ass up.."
    hari "Hahaha!"
    t "Alright alright settle down everybody!"
    t "I have an announcement to make."
    "The room went silent as everyone stopped chattering."
    t "There will be a class representative meeting today during lunch."
    t "Mandatory for students involved."
    hari "Heh, what kind of loser even willingly joins that meeting."
    "I check the list."
    "My skin goes pale."
    "I look at [bas]."
    "He shrugs."
    bas "Didn't know you were on the list, man."
    hari "Shit, neither do I."
    "Same here."
    mc "Screw this, another thing to figure out.."
    "Before the meeting even happens, Rei makes her presence known in class. Not dramtically, she's just doing her job."
    "Collecting assignment submissions, reminding people about upcoming deadlines, handling a minor dispute between two classmates with quiet efficiency."
    "She moves through the classroom like someone who has been running things so long she doesn't think about it anymore."
    mc "..."

    "She doesn't ask for attention. She just has it."

    "The crowd around her isn't there because she demanded it."
    "It's there because she's the person who actually has the answers."

    "I watch her for a second longer than I mean to."

    "She glances up."

    "Makes eye contact with me for exactly one second."

    "Then looks back down at her clipboard like I don't exist."

    mc "..."

    "Noted."

    "I look away first."

    bas "Don't stare, man."

    mc "I wasn't staring."

    bas "You were absolutely staring."

    hari "Bro, everyone stares at [Rei] at least once."
    hari "It's basically a rite of passage."
    bas "I wouldn't blame you, though."
    bas "She's beautiful."
    hari "Yeah, if it wasn't for those baggy eyes, she'd be so FINE."

    bas "And then when she gives you THAT look to you like that and you never do it again."

    mc "Yeah I noticed."

    "The three of us go quiet for a second."

    hari "Good luck at the meeting by the way."

    mc "Thanks."

    hari "You're gonna need it."

    mc "...Thanks."

    t "Alright, open your books to page forty."

    "I open whatever book is on my desk to page forty."
    "Close enough."

    #TIME SKIP TO LUNCH

    scene courtyard with fade
    play music "Free time.mp3" volume 0.8

    "Lunch hits and the school exhales."

    "Students spill out into the courtyard, the hallways, anywhere with sunlight."

    "I have approximately thirty minutes before the meeting."

    "I find a spot and eat from the takeout box I got from a nearby convenience store."

    "It's fine."

    "I'm thinking about the meeting."
    "Specifically about the fact that I have no idea what it's about."
    "Or why this guy was on the list."
    "Or what a class representative meeting even involves at this school."

    mc "Okay. What do I actually know."

    "Rei runs it. That much is obvious."
    "It's mandatory for students involved."
    "Basilo didn't know I was on the list."
    "Which means 'I' signed up for something at some point and then apparently forgot about it."

    mc "Great."

    "I finish my lunch."

    "Someone sits down nearby."

    "Not next to me. A few feet away. On the same low wall."

    "I glance over."

    "It's the guy from the back of the class."
    "Headphones around his neck now instead of on his ears."
    "He's eating alone, reading something on his phone, completely unbothered."

    "He doesn't look at me."

    "I look back at my own phone."

    "..."

    "He says something without looking up."

    cm "The meeting's in room 204."

    mc "...What?"

    cm "Class rep meeting. You looked like you were trying to remember where it was."

    "I was not visibly doing that."
    "I was just sitting here."

    mc "How did you—"

    cm "You've been staring at the building for four minutes."

    "..."

    mc "Thanks."

    cm "Mm."

    "He goes back to his phone."
    "Puts his headphones back on."
    "Conversation over apparently."

    "I look at him for a second."

    "This guy notices things."

    "I file that away."

    mc "Hey."

    "He doesn't take the headphones off but he tilts his head slightly."

    mc "What's your name?"

    "He looks at me then. Actually looks."
    "Like the question surprised him."
    "Like 'I' never asked."

    cm "..."

    ku "Kuro."

    mc "Cool."

    "I get up and head toward the building."

    "I can feel him watching me walk away."

    "Filed."

    scene classmorn with dissolve #use different classroom or angle of classroom for this one
    stop music

    "Room 204 is a regular classroom."
    "About twelve students."
    "Some I recognize, most I don't."

    "Rei is already there."
    "Of course she is."
    "She's probably been here since morning."

    "She has a stack of papers on the desk in front of her."
    "A whiteboard behind her with an agenda already written out."
    "She's talking to another student, calm and efficient, finishing a thought."

    "I take a seat toward the middle."
    "Not the front. Not the back."
    "Somewhere forgettable."

    show Rei happy at right
    with moveinright
    play music "Student heart.mp3" volume 0.6

    Rei "Alright, everyone's here."

    Rei "Let's get started. We'll keep this under twenty minutes."

    "She moves through the agenda with the energy of someone who prepared for this last night."
    "Event scheduling. Budget allocation. A noise complaint from the floor below the music room."
    "Practical. Efficient. No wasted words."

    "I follow along well enough."
    "Nod when other people nod."
    "Write something in the notebook I grabbed from 'my' bag."

    "It's going fine."

    "Then."

    Rei "The culture fest committee."

    Rei "We need someone to take the lead on coordinating the booth applications."

    Rei "According to last semester's records, [mc] volunteered for this."

    "..."

    "Everyone looks at me."

    mc "..."

    "I look at the whiteboard."
    "Then back at Rei."

    mc "Right. Yeah. I can handle that."

    Rei "..."

    "She looks at me for a moment."

    "Not suspicious exactly."
    "More like recalibrating."

    Rei "You seem different today."

    mc "Long night."

    Rei "..."

    Rei "The deadline for booth applications is next Friday."
    Rei "I'll send you the template."

    mc "Got it."

    "She holds eye contact for one second longer than necessary."

    "Then moves on."

    Rei "Next item."
    scene black with fade

    "I exhale quietly."

    "The meeting wraps in eighteen minutes."
    "Rei thanks everyone, reminds two people about separate deadlines by name without checking her notes, and starts collecting the sign-in sheet."
    scene classmorn with fade

    "People file out."

    "I'm almost at the door."

    Rei "[mc]."

    "I stop."

    "Turn around."

    "She's looking at me over her clipboard."

    Rei "You actually stayed for the whole meeting."

    mc "...Was I not supposed to?"

    Rei "Last semester you left twice before it even ended."

    mc "..."

    mc "Trying something new."

    "She looks at me."
    "That same recalibrating look."

    Rei "Glad you're taking it seriously this time."

    "She says it plainly."
    "Not warmly."
    "But not coldly either."
    "Like a fact she's noting for the record."

    "She turns back to her papers."

    "I leave."
    scene schoolhall with dissolve

    "..."

    "In the hallway I stand still for a second."

    mc "What did you sign up for, man."

    "I add culture fest coordinator to the mental list of things I have to figure out."
    "It's getting long."

    #AFTER SCHOOL - THE CAFE

    scene sgateaft with fade
    play music "Daijoubu.mp3" volume 0.8

    "School ends."

    "I remember [hari] said earlier in class to meet at the cafe."
    "I don't know where the cafe is."
    "I do know that [hari] runs somewhere when he's in a hurry."
    "And I know roughly which direction."

    mc "This is either good instinct or a complete waste of time."

    "It's good instinct."


    "I follow the general direction [hari] sprinted toward at lunch two days running."
    "Past the school gate."
    scene bg streetaft with dissolve
    "Down the main road."
    scene bg cityaft with dissolve
    "Left at the corner with the busted traffic light."

    "And then I smell coffee."

    scene black with fade

    scene cafeout with dissolve
    "Hopefully this is the place.."
    #play music "resto door ring"
    play music "welcome to our cafe.mp3" volume 0.7
    scene cafeaft with dissolve


    "It's a small place."
    "The kind that has four tables inside and two outside and somehow always has someone in it."
    "Handwritten chalkboard sign above the door."
    "Warm light through the window."

    "I can already hear [hari] before I open the door."

    hari "I'm telling you, the lemon ratio is the issue—"

    bas "The lemon ratio has always been the issue for three days—"

    hari "Because I haven't perfected it yet—"

    "I push the door open."

    "Both of them look up."

    hari "HE FOUND IT!"

    bas "I told you he'd find it eventually."

    hari "Bro I genuinely didn't think he'd find it, I just said that—"

    bas "Sit down man, you're embarrassing yourself."

    mc "What are you making."

    hari "Lemon coffee."

    mc "...Why."

    hari "Because nobody's done it right yet."

    bas "Many people have done it."

    hari "Nobody has done it RIGHT."

    "I sit at the counter."

    "The cafe is quiet except for them."
    "One other customer in the corner reading something."
    "Soft music from somewhere."

    mc "How long has this been going on."

    bas "Day three."

    hari "This is day three of attempting it. Not day three of it being possible."

    bas "He drew a diagram."

    hari "It's a ratio chart—"

    bas "He drew a diagram of a coffee cup."

    "I look at [hari]."

    hari "It's a ratio chart."

    mc "Can I see it."

    "He slides it across the counter immediately."

    "It is absolutely a diagram of a coffee cup."
    "With arrows."
    "And percentages."
    "And a note at the bottom that says 'MORE LEMON???' with three question marks."

    mc "..."

    mc "This is genuinely impressive."

    hari "Right?"

    bas "He said impressive not good."

    hari "Same thing."

    "I slide the diagram back."

    bas "You want something to drink? On the house since you found the place."

    bas "I suggest the cappuccino."

    hari "I suggest trying my lemon coffee!"

    hari "But it's up to you!"

    menu:
        "Cappuccino":
            jump capp

        "Lemon coffee":
            jump lemon

label capp:
    mc "Whatever's not lemon."

    bas "Smart man."

    hari "Coward."

    "He says it without heat."
    "Already turning back to his experiment."

    "A minute passes."

    "Then [bas] sets something in front of me."

    "I look at it."

    "It looks like a proper coffee."
    "Clean layers."
    "Small pattern on the foam that wasn't an accident."

    mc "You actually made this."

    bas "I work here, man."

    mc "No I mean.. This looks like something from an actual cafe."

    bas "This is an actual cafe."

    mc "You know what I mean."

    "He leans against the counter with the energy of someone trying not to look pleased with himself."

    bas "Just try it."

    "I try it."

    "..."

    "It's genuinely good."
    "Like properly, unexpectedly good."
    "The kind of good that makes you pause."

    mc "Okay."

    bas "Yeah."

    mc "Okay this is really good."

    bas "I know."

    hari "IT DOESN'T COUNT IF IT DOESN'T HAVE LEMON—"

    bas "Nobody asked you."

    hari "A cappuccino is a solved problem! I'm out here doing something NEW—"

    bas "You're out here doing something wrong."

    hari "INNOVATION LOOKS LIKE WRONG UNTIL IT LOOKS LIKE RIGHT—"

    mc "He has a point."

    bas "Don't encourage him."

    mc "I'm just saying the passion is there."

    bas "The passion has been there for three days and the coffee has been bad for three days."

    hari "TODAY IS NOT OVER."

    "I take another sip."

    "Watch [hari] consult his ratio chart with complete sincerity."

    "Watch [bas] shake his head with the exhaustion of someone who has been watching this for 72 hours."

    mc "How long have you two been working here together."

    bas "Two years."

    mc "And it's always like this?"

    bas "Only when he gets an idea."

    mc "How often does he get ideas."

    bas "..."

    bas "Frequently."
    jump cafe_continue





label lemon:
    bas "Your funeral."
    "I watch [hari] for a second."
    "He starts making it with such passion and determination."
    "I don't know if I should be worried or excited.."

    hari "Okay okay, taste it."

    "He slides a small cup across the counter."
    "The color is wrong."
    "The smell is interesting in a way that isn't entirely good."

    mc "..."

    "I drink it."

    "..."

    mc "It's not terrible."

    hari "NOT TERRIBLE! BAS, HE SAID NOT TERRIBLE!"

    bas "That's the lowest possible bar."

    hari "IT CLEARS THE BAR!"

    "I look at the cup."
    "It is genuinely not terrible."
    "It's also not good."
    "But something about the fact that he made it with a ratio chart and three question marks makes it taste better than it should."
    "I guess the real flavor is the wholesomeness" #Omi will drink this later and she will have the opposite reaction of MC, this will be funny

    mc "Keep working on it."

    hari "Oh I will."

    jump cafe_continue

label cafe_continue:

    "I look at my coffee."
    "Then at [hari] and his diagram."
    "Then back at [bas]."

    mc "You guys are good friends."

    "They look at me."
    "Something shifts slightly in their expression."
    "Not much."
    "Just a recalibration."
    "The same kind Rei did."

    bas "You really are different lately, dude."

    mc "So I've been told."

    "He doesn't push it."
    "Just picks up a cloth and wipes down the counter."

    bas "Glad you found the place."

    mc "Yeah."

    "I take a sip of my coffee."

    "It's the best thing I've had since arriving in this world."

    "Not necessarily because of the coffee."

    "But the experience of just hanging out with these two."

    "Eh, it's probably both."

    "The cafe hums around us."
    "Warm light."
    "The smell of actual good coffee underneath whatever [hari] is attempting."

    scene black with fade
    "I haven't felt this in a while. Not even in my own world, too."
    "It's really nice."

    "Just.. Somewhere to be.."


    "Not performing anything."
    "Not navigating anything."
    "Just sitting at a counter while two idiots argue about lemon ratios."

    mc "..."

    "I think I like this place."

    scene cafeaft with fade

    bas "Here."

    "He sets a sundae in front of me."
    "Simple. Nothing crazy."

    bas "How was the meeting by the way?"

    mc "I apparently volunteered to coordinate booth applications for the culture fest."

    bas "..."

    bas "[mc] you idiot."

    mc "Yeah."

    hari "What's a culture fest coordinator even do?"

    bas "Exactly what it sounds like."

    hari "So a lot of emailing."

    mc "Apparently."

    hari "Rough."

    "He goes back to his lemon ratio."

    "I finish my coffee and sundae."

    "Outside the window the street does its afternoon thing."
    "People heading home."
    "The light going that particular gold it goes at this hour."

    "Tomorrow I have to figure out the culture fest thing."
    "And what that meeting means for my relationship with Rei going forward."
    "And approximately forty other things."
    "Then the Kel situation from the phone. Still haven't met him in this world."
    "Speaking of which, I believe I haven't seen Omi, too.."

    "But right now."

    "I'm just here."

    "And that's enough for today."

    stop music fadeout 2.0

    scene black with fade

    "Day two. Done."

    #DAY 3
    #add filler scenes of all the side characters
    #specifically chuuya and kuro
    #maybe add waguri somewhere too
    scene classmorn with dissolve
    play music "Student heart.mp3"  volume 0.6

    "On my third day, I've already structured a daily routine myself."
    "I don't know what my routine originally used to be."
    "All I know is my mom and sis look at me weird while doing my routine."
    "I'm honestly kind of surprised that no one has questioned me so far.."
    "..."

    "I'm getting better at this."
    "I know most people's names from this life."
    "I know where the cafe is."

    "I do however have to worry about my role in the student council."

    hari "I refuse to be late..!"

    t "Alright class everyone please settle down. Our class is about to start."

    hari "I'M NOT GONNA BE LATE!"

    "He sits down."
    "ten seconds to spare."

    t "You're late. This counts as absent."

    hari "Wha-?!"
    hari "Sir I'm not late, you can see the time I had atleast a few more seconds to spare!"
    t "Where?"
    "They both look at the clock which was already passed the start of class time."
    t "I don't think so."

    "While the two of them argue, I decide to look around class to see what's going on."
    "Especially the whispering from the far back left side of the class."
    "I decide to eavesdrop."



    ich "-ou guys ever wonder why [bas] and [hari] are the only ones always being late?"
    ich "I bet they run some illegal operation business.."
    epg "Uhm, [ich], I believe they work as baristas in some cafe.."
    ich "Nah, that sounds boring!"
    ich "That cafe probably has strippers in them!"
    Rei "Stop, [ich]."
    Rei "If you're gonna make fun of them atleast get your facts right."
    ich "Oof!"
    "That definitely hurt her pride as the so called 'class gossip queen'."

    "I look at back center, I see [ku]. He's on his phone reading something with headphones on."
    mc "Weird kid.."


    "I'm starting to understand this world's rhythms."
    "The feel of a normal day for me here."
    "It's almost comfortable."

    "The teacher and [hari] seems to have come to an agreement and they both settle down to their respective roles."

    "I glance around the room while the teacher sets up."

    "And then."

    "The girl in the corner."

    "She's reading again."
    "Same seat."
    "Same quiet vibe."
    "I've clocked her every day but haven't looked properly until now."

    "I focus on checking her out."
    "She's actually kinda cute."
    "Her little waist bag I'm assuming where she keeps her books has some pins on them. Niches I've never seen before."
    "Her hair is nice and long and she wears glasses as if her bangs weren't already covering her eyes."
    "But more imporantly.."
    "The book in her hands.."
    "..."
    "Wait a minute.."
    "I know that book."
    "Not know of it."
    "I know it."
    "That specific edition."
    "That specific cover."

    "I had that exact copy on my desk in my real world for two years."
    "Never finished it."
    "But I've always meant to. Just didn't have the time.."

    mc "..."

    "She turns a page."
    "Completely unbothered by the noise of the classroom settling around her."

    "I look away before she notices."

    t "Alright, books out."

    "I spend the first half of class thinking about that book."

    #LUNCH - FIRST APPROACH

    scene courtyard with dissolve
    play music "Free time.mp3" volume 0.8

    "Lunch."

    "I get my food and look for somewhere to sit."

    "The courtyard is full."
    "The usual clusters."
    "[bas] is eating somewhere, nowhere to be found."
    "[hari] is probably being loud somewhere. Or maybe he's with [bas]? Who knows."

    mc "Seems like the perfect opportunity to check out the cafeteria."

    scene cafeteria with dissolve
    play music "chika theme.mp3" volume 0.8

    "Ironically enough it is much quieter here since students immediately leave to go somewhere after eating their lunch"
    "Still has some students chattering here and there but still.."

    "I pick a spot in a corner to sit down, lunch in hand."

    "While preparing to eat, I look to my right."

    "She's there."

    "Same book girl from class."
    "The table next to me."
    "Eating alone."
    "Book open beside her tray like she's having lunch with it."

    "I eat my food."

    "Don't stare."

    "..."

    "I'm going to say something."

    "I don't know why."
    "It's the book probably."
    "Or the fact that she's been in my peripheral vision for three days and I keep noticing her without meaning to."

    "Either way."

    "I pick up my tray."

    "Walk over."

    "She doesn't look up."

    mc "Hey."

    "..."

    "She looks up."

    show chi happy at right
    with moveinright

    "Up close she's—"

    "She looks at me with the specific wariness of someone who has learned that unexpected conversations usually mean something they don't want."

    bg "...Hi."

    mc "Sorry. You're reading that book."

    "She looks at the book."
    "Then back at me."

    bg "...Yes."

    mc "I have that exact copy."

    "..."

    "She looks at the cover."
    "Then back at me."
    "The wariness hasn't gone but something behind it shifted slightly."

    bg "Y-You've read it?"

    mc "Started it. Never finished."

    bg "..."

    bg "Why not..?"

    mc "Got busy. Then forgot. Then felt weird starting over."

    "She considers this."

    bg "That's-"
    bg "..a valid reason."

    mc "Is it?"

    bg "M-Most people just say they don't read. and.. and.. at least you started.."

    "I look at the cover."

    mc "Is it worth finishing?"

    "She looks at the book."
    "Then at me."
    "Like she's deciding something."

    bg "Yes..!"

    bg "The ending changes everything before it."

    mc "That's either a recommendation or a warning."

    bg "Both, maybe."

    "I notice her tone quickly changed quite a bit. More confidence."

    "The corner of her mouth moves."
    "Not quite a smile."
    "But close."

    bg "I will say that it is one of the more fascinating books I've ever read!"
    bg "The descriptiveness of the writing really makes you feel like you're in the book itself!"

    "I look at the bench across from her."

    mc "Can I sit here?"

    "She hesitates."
    "a few seconds pass."
    bg "...Okay."

    "I sit."

    "She goes back to her book."
    "I eat my food."

    "It's quiet."
    "Not awkward quiet."
    "Just quiet."

    "I don't push it."

    "After a few minutes I finish eating."

    mc "What's your name?"

    "She looks up."

    chi "...Chika."

    mc "I'm—"

    chi "I know who you are."

    mc "Right."

    "Of course she does."
    "Everyone knows 'me'."

    "I pick up my tray after consuming everything."

    mc "Thanks for letting me sit."

    chi "..."

    chi "You didn't talk much."

    mc "You were reading."

    "She looks at me."
    "That same slight recalibration everyone does."
    "Like 'I' wouldn't have thought of that."

    chi "...Yeah."

    "I leave."

    "She watches me go for a second."
    "Then goes back to her book."

    scene schoolhall with dissolve
    play music "Skips.mp3" volume 0.8

    "Our teacher for this class apparently called in sick. Guess, that's free time for us?"
    "Good thing they allow us to just wander around. My school from my world didn't allow us to just do that.."
    "Perfect time to check this place around."

    cm "Can't wait for the festival!"
    cm "I know, it's gonna be so hype..!"
    cm "I heard [hari] and [bas]'s cafe would be sponsored and be in one of the stalls."
    cm "You kiddin? That's awesome! I'm definitely buying from them."

    mc "..."

    "I continue to walk around."

    "Damn, this school is huge."
    "I think I can only explore one side of the school for today.."

    menu:
        "East hall": #kuro and chuuya interaction
            jump easthall
        "West hall": #wagi interaction
            jump westhall

label easthall:
    "kuro and chuuya"

    jump hallexploredone





label westhall:
    "waguri"

    jump hallexploredone



    #AFTER SCHOOL - SECOND BEAT
label hallexploredone:

    scene sgateaft with fade
    play music "Daijoubu.mp3" volume 0.8

    "School ends."

    "I'm heading toward the gate when I see her again."

    "She's walking in the same direction."
    "Slow."
    "Book in her bag now."
    "I fall into step a few feet behind her."

    "I'm not following her."
    "I'm just moving in the same direction."

    scene bg street2aft with dissolve

    "She notices and slightly slows down."

    "I slow down too."

    "..."

    chi "You live this way?"

    mc "Apparently."

    chi "..."

    "Okay, that was a weird answer. Why did I say that..."
    "She keeps walking."
    "I keep walking."

    "We're not walking together exactly."
    "More like two people going the same direction who have mutually acknowledged it."

    "It's comfortable in a way I don't fully understand."

    "After a while she speaks."

    chi "You were different at lunch."

    mc "Different..?"

    chi "You didn't try to fill the silence."

    mc "Was that okay?"

    chi "..."

    chi "Yes."

    "We walk a little further."

    chi "Most people can't do that."

    mc "Sit quietly?"

    chi "Not make it weird."

    mc "It wasn't weird."

    chi "I know."
    chi "That's what I mean."

    "I look at her."
    "She's looking straight ahead."

    mc "Do you always walk home alone?"

    chi "..."

    chi "I don't go outside much usually."

    mc "What changed today?"

    "She's quiet for a moment."

    chi "Nothing changed."
    chi "I just had to go to school."

    mc "Right.."

    "..."

    chi "I mean—"

    "She stops."

    "Looks at the street ahead."

    chi "I used to go straight home after school."
    chi "I'm trying to... not do that as much."

    "She says it carefully."
    "Like she rehearsed it."

    "I think about my own room."
    "My own straight home after everything habit."
    "Years of it."
    "Me and her aren't so different afterall."

    mc "Yeah."

    mc "I know that feeling."

    "She looks at me."

    "Not the recalibrating look."
    "Something different."
    "More direct."

    chi "..."

    chi "..Okay."

    "We reach a corner."

    chi "This is my turn.."

    mc "Okay."

    chi "..."

    chi "The book."

    mc "Yeah?"

    chi "You should finish it."

    chi "The ending is worth it."

    "She says it simply."
    "Then turns and walks down her street."

    "Doesn't look back."

    "I stand at the corner for a second."

    mc "..."

    "I'm going to finish that book."

    "I don't even have a copy here."

    "I'm going to find one."

    "Actually.. I'm gonna find one right now."
    scene livingroom with dissolve
    "I ran home to put down my bag then immediately went out to go to some bookstore."
    scene bg streetaft with dissolve
    scene bg cityaft with dissolve
    "I look around for some local bookstore around the city."
    "Aha, Bingo."
    scene libraryaft with dissolve
    play music "chika theme.mp3" volume 0.8
    #chika interactions at bookstore here, shes reading her book


    chi ""


    #mc and chika going home after, you walk her home up until the street corner where the two of you seperate


    stop music fadeout 2.0

    scene black with fade

    "Day three."
    "Done."


    "END"











#hari says bro, basilo says dude, kel says man









    ###SCENE DRAFTS ALL GO HERE###





    return
        
        #copy paste M dash here —



# label monika_call:
#     hide screen creepy_blue_screen
#     "" "I received a call from my phone."
#     "" "It's Monika."
#     $ result = renpy.call_screen("incoming_call")
#     if result == "accept":
#         jump monika_accept
#     else:
#         jump monika_decline


