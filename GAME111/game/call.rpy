screen incoming_call():
    modal True
    zorder 100

    # Background phone image
    add "incoming_monika.png"

    # ACCEPT button
    imagebutton:
        idle "accept_idle.png"
        hover "accept_hover"
        xpos 0.832
        ypos 0.659
        action Return("accept")

    # DECLINE button
    imagebutton:
        idle "decline_idle.png"
        hover "decline_hover"
        xpos 0.927
        ypos 0.659
        action Return("decline")

screen ongoing_call():
    add "ongoing_monika.png"
    zorder 100
   
        
