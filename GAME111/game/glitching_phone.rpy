init python:
    import random
screen phone_glitch_off():
        add images/crackedoff_phone.png


screen phone_glitch():
    modal False
    zorder 100
    default current_image = "images/incoming_mom.png"
    default glitch_x = 0
    default glitch_y = 0

    add current_image:
        xpos glitch_x
        ypos glitch_y

    timer 1 repeat True action [
        SetScreenVariable("current_image",
            random.choice([
                "images/incoming_mom.png",
                "images/crackedoff_phone.png"
            ])
        ),
    ]

