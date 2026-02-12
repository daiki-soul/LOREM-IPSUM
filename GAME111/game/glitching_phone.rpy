init python:
    import random

screen incoming_call_mom():
    modal True
    zorder 100

    default show_crack = False
    default glitch_x = 0
    default glitch_y = 0

    add "images/incoming_mom.png":
        xpos glitch_x
        ypos glitch_y

    imagebutton:
        idle "idle_accept_mom.png"
        hover "ongoing_mom_hover1.png"
        xpos 0.832
        ypos 0.660
        action Return("accept")

    imagebutton:
        idle "idle_decline_mom.png"
        hover "ongoing_mom_hover2.png"
        xpos 0.927
        ypos 0.660
        action Return("decline")

    if show_crack:
        add "images/crackedoff_phone.png":
            xpos glitch_x
            ypos glitch_y

    # Glitch timer
    timer 0.15 repeat True action [
        SetScreenVariable("show_crack", random.choice([True, False, False])),
    ]



screen incoming_call_mom1():
    modal False
    zorder 100

    default show_crack = False
    default glitch_x = 0
    default glitch_y = 0

    add "images/incoming_mom.png":
        xpos glitch_x
        ypos glitch_y

    imagebutton:
        idle "idle_accept_mom.png"
        hover "ongoing_mom_hover1.png"
        xpos 0.832
        ypos 0.660
        action Return("accept")

    imagebutton:
        idle "idle_decline_mom.png"
        hover "ongoing_mom_hover2.png"
        xpos 0.927
        ypos 0.660
        action Return("decline")

    if show_crack:
        add "images/crackedoff_phone.png":
            xpos glitch_x
            ypos glitch_y

    # Glitch timer
    timer 0.15 repeat True action [
        SetScreenVariable("show_crack", random.choice([True, False, False])),
    ]
