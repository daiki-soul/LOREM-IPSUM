screen incoming_call_monika():
    modal True
    zorder 100

    # Background phone image
    add "incoming_monika.png"

    # ACCEPT button
    imagebutton:
        idle "accept_idle.png"
        # hover "accept_hover"
        xpos 0.832
        ypos 0.660
        action Return("accept")

    # DECLINE button
    imagebutton:
        idle "decline_idle.png"
        # hover "decline_hover"
        xpos 0.927
        ypos 0.660
        action Return("decline")


        
# screen incoming_call_mom():
#     modal True
#     zorder 101
#     add "incoming_mom.png"
#     imagebutton:
#         idle "idle_accept_mom.png"
#         hover "ongoing_mom_hover1.png"
#         xpos 0.832
#         ypos 0.660
#         action Return("accept")
#     imagebutton:
#         idle "idle_decline_mom.png"
#         hover "ongoing_mom_hover2.png"
#         xpos 0.927
#         ypos 0.660
#         action Return("decline")

