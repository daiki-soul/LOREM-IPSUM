
# screen navigation():
#     tag menu

#     add "gui/menu.png"

#     vbox:
#         style_prefix "navigation"

#         xalign 0.5   
#         yalign 0.9

#         spacing gui.navigation_spacing

#         if main_menu:

#             textbutton _("Start") action Function(Start())

#         else:

#             textbutton _("History") action ShowMenu("history")

#             textbutton _("Save") action ShowMenu("save")

#         textbutton _("Load") action ShowMenu("load")

#         textbutton _("Settings") action ShowMenu("preferences")


#         if _in_replay:

#             textbutton _("End Replay") action EndReplay(confirm=True)

#         elif not main_menu:

#             textbutton _("Main Menu") action MainMenu()

#         if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

#             textbutton _("Credits") action ShowMenu("Credits")

#         if renpy.variant("pc"):

#             textbutton _("Quit") action Quit(confirm=not main_menu)


# style navigation_button:
#     xminimum 260
#     xalign 0.5
#     padding (24, 6, 24, 6)
#     background None

# style navigation_button_text:
#     xalign 0.5
#     size 40
#     font "font/Cinzel-Regular.ttf"
#     color "#cce8ff"
#     outlines [(2, "#0a1a3a", 0, 0)]
#     hover_color "#ffffff"
#     hover_outlines [(2, "#2266aa", 0, 0)]
#     insensitive_color "#445566"

# style navigation_quit_text is navigation_button_text:
#     color "#ff6666"
#     outlines [(2, "#3a0000", 0, 0)]
#     hover_color "#ffaaaa"
#     hover_outlines [(2, "#880000", 0, 0)]

