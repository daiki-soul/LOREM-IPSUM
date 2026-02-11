init python:
    import random

screen phone_glitch():

    default current_image = "images/crackedhomescreen_phone.png"
    default glitch_x = 0
    default glitch_y = 0

    add current_image:
        xpos glitch_x
        ypos glitch_y

    timer 0.25 repeat True action [
        SetScreenVariable("current_image",
            random.choice([
                "images/crackedhomescreen_phone.png",
                "images/crackedoff_phone.png"
            ])
        ),
    ]