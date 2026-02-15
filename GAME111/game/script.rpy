#ALL SCRIPT GO HERE

#declare all characters here
#can change color of character names, declare here

# #MAIN CAST
# default player_name = ""

define a = Character("???") #placeholder for unknown
define mc = Character("[player_name]") #original mc
define mcln = Character("[last_half_name]") #half of player name
define mc2 = Character("Lawrence") #unofficial name, the isekai'd new body of mc

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

define wagi = Character("Waguri") #f #HEROINE
define ros = Character("Rosie") #f
define yui = Character("Yui") #f (wagi, ros, yui are childhood friends)

    #SIDE CHARACTERS USELESS FOR MOST PART
define ichi = Character("Ichika") #f classmate #POSSIBLE HEROINE
define paul = Character("Paul") #m school delinquent
define emu = Character("Emu") #f a cheerful, lively, very pleasant girl, much like Sayori (no depression) someone who dies later on (pretends to be important character early in the story) (this ending for her depends on the story flow and route)
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
image bg cityaft = im.Scale("bg city_aft.png", 1920, 1080)
image bg cityn = im.Scale("bg city_night.png", 1920, 1080)
image bg arcade = im.Scale("bg arcade.jpg", 1920, 1080)
image bg arcade2 = im.Scale("bg arcade2.jpg", 1920, 1080)
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


image omiscene = im.Scale("scenewithomi.png", 1920, 1080)

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

    play music "My Feelings.mp3"
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

    "You really done it now this time, [mc].{w=1} You've made the most bubbly, energetic, clumsy, optimistic, kind, cheerful, innocent, caring, affectionate and warmhearted girl cry."

    "What the fuck is wrong with you."

    "I think the others heard us by now."

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

    omi "I'd love that."

    "Thus, you've made your first step to earning her forgiveness."

    "You both quietly leave the arcade."

    stop music fadeout 1.0

    scene bg cityaft
    with dissolve

    play music "rain.mp3" fadein 1.5

    "The noise of the arcade dies the moment the door shuts behind you."

    "Outside, the air feels cooler. Lighter. Like the world isn’t pressing down as hard."

    omi "…It’s weird."

    play music "Piece By Piece.mp3" fadein 1

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

    "She says it suddenly, like she just remembered hunger exists."

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

    omi "Wow…"

    omi "I forgot this place existed."

    mc "You forgot because you’re always inside eating sugar."

    omi "HEY!"

    "She plops down near the edge, legs dangling, already tearing open a snack."

    omi "This is why I brought you here."

    mc "For the view?"

    omi "Nope."

    omi "Because food tastes better when you’re somewhere stupid."

    mc "That explains a lot about you."

    omi "Rude."

    "She hands you one of the snacks."

    omi "Here. Compensation."

    mc "For emotional damage?"

    omi "For buying everything I wanted."

    "You sit beside her."

    "For a moment, neither of you speaks."
    stop music fadeout 1

    omi "…You know."

    omi "Back then, I thought you’d come back."

    mc "Yeah?"

    omi "Every time I came here, I’d imagine you sitting right there."

    "She points to the spot next to you."

    omi "I even practiced what I’d say."

    mc "What was the line?"

    omi "Hmm…"

    "She smiles."

    omi "Probably something dumb."

    omi "Like… ‘You’re late.’"

    mc "Sounds like you."

    omi "Hey! That’s charming."

    "She laughs, then quiets."
    play music "Sparks Ignite.mp3"

    omi "Seeing you actually here now feels… unreal."

    "The wind brushes past."

    "Her shoulder barely touches yours."

    omi "If this is a dream… don’t wake me up yet."

    mc "Omi—"

    "She turns her head."

    "You’re closer than you realized."

    "Way closer."

    "She freezes."

    omi "…Oh."

    "Her eyes flick down."

    "Then back up."

    "She swallows."

    omi "This is probably a bad idea."

    mc "Yeah."

    "Neither of you moves."

    omi "…You won’t disappear if I do this, right?"

    mc "I won’t. I already made a promise, right?"

    mc "I already told you that I'd make it up to you, right?"

    omi "True..{w=1} so.."



    "She leans in."

    "I lean in too, to reciprocate"

    scene scenewithomi with dissolve

    "The kiss is soft."

    "Brief."

    "Like she’s afraid to take more than a second."

    "She pulls back fast, covering her mouth."

    scene roofaft with dissolve

    omi "I— I’m sorry!"

    omi "That was— I wasn’t thinking!"

    mc "Omi—"

    omi "Just— just pretend that didn’t—"

    "She stops talking."

    "She’s still right there."

    "Not pulling away."

    "Not leaving."

    omi "…You’re still here."

    mc "Yeah."

    "She lets out a shaky laugh."

    omi "Good."

    "She scoots a tiny bit closer."

    omi "Just… don’t make me regret that, okay?"

    "The city keeps glowing below."

    "And for now.."

    "She doesn’t let go."

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

    "Heh, can't believe I took them for granted."

    "Today was awesome."

    "From this day forward, I shall finally put my life back together!"

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
    "" "The Truck finally hits my body.."
    hide screen film_grain_effect
    "" "Augh!{nw}"
    with vpunch
    $ renpy.sound.play("audio/ambient/carsqueel.mp3", channel="sfx")
    $ renpy.sound.set_volume(2, delay=0, channel="sfx")

    pause 1

    $ renpy.sound.play("audio/ambient/car_alarm.mp3", channel="sfx2")
    $ renpy.sound.set_volume(0.5, channel="sfx2")



    stop music

    $ renpy.pause(3, hard=True)
    "{nw}"

    scene crash #OPTIONAL maybe put blood overlaying on screen, maybe put red and blue effects to simulate police sirens too
    window hide

    $ ambient.play("audio/ambient/heart.wav")

    $ renpy.sound.play("audio/ambient/earringing.mp3", channel="sfx")
    $ renpy.sound.set_volume(0.5, channel="sfx")

    $ renpy.pause(5, hard=True)

    "Ugh.."



    show screen incoming_call_mom1



    $ renpy.sound.play("audio/ambient/peoplescreaming.mp3", channel="sfx_loop", loop=True)
    $ renpy.sound.set_volume(0.5, channel="sfx_loop")


    "" "mom?"
    show screen incoming_call_mom1

    pause 3
    show screen incoming_call_mom1
    "" "..."

    $ renpy.sound.play("audio/ambient/phonering.mp3", channel="sfx1")
    $ renpy.sound.set_volume(0.5, channel="sfx1")

    show screen incoming_call_mom1
    "" "mom..."
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
    "What the hell?"
    "Where the fuck am I?{w=1.0} Who's room is this??"
    "And who is that calling me?"
    "I try to stand up from the bed I've been laying in that I do not recognize at all."
    "No..{w=1} I don't even recognize anything here."
    "The moment I tried to stand up, I almost fell infront of me {w=1} I feel light as hell that it's actually disorienting."
    mc "Fuck.. I need to vomit."
    "I went out the bedroom to look for the bathroom. Thankfully, it was just across the hall and conveniently open with no one inside."

    scene mchallwayn with dissolve

    scene bathroom with dissolve


    ".."









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

