default phone_open = False
config.overlay_screens.append("phone_key_listener")

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

screen phone_key_listener():
    key "p" action Function(toggle_phone)


screen time_2pm()://for time purposes
    add "images/2PM.png"





