label splashscreen:#intro
    scene black
    with fade
    play music "a life for granted.mp3"
    show text "Eupho CO. Studios"
    with dissolve
    pause 2
    hide text
    with fade
    #intro art here
    with fade
    "In a world where you can change everything..."
    pause 2
    with Fade(2.0, 0.0, 0.0)
    stop music fadeout 2.0
    return

init python:#menu music
    config.main_menu_music = "title.mp3"
