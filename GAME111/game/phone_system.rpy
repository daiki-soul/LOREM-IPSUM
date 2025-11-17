default phone_open = False

screen phone_screen():
    tag phone          
    zorder 1000
    add "images/home_ui.png"
    key "p" action Function(toggle_phone)



init python:
    def toggle_phone():
        if store.phone_open:
            store.phone_open = False
            renpy.hide_screen("phone_screen")
        else:
            store.phone_open = True
            renpy.show_screen("phone_screen")



init python:
    def incoming_monika():
        store.phone_open = True
        renpy.show_screen("phone_screen")
        renpy.show("incoming_monika.png")

        def incoming_placeholder():
        store.phone_open = True
        renpy.show_screen("phone_screen")
        renpy.show("incoming_placeholder.png")
    config.overlay_screens.append("phone_key_listener")



screen phone_key_listener():
    key "p" action Function(toggle_phone)



screen incoming_monika():
    tag phone           # exclusive screen tag
    zorder 1000         # very high layer
    add "images/incoming_monika.png"  # your phone image


screen incoming_placeholder():
    tag phone           # exclusive screen tag
    zorder 1000         # very high layer
    add "images/incoming_placeholder.png"  # your phone image
    




