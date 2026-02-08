
screen jumpscare():
    add "images/jumpscare.png" xysize (config.screen_width, config.screen_height)


transform flicker():
    linear 0.05 alpha 0.7
    linear 0.05 alpha 1.0
    repeat

transform zoom_in(duration=10.0, start_scale=3.0, end_scale=1.2):

    zoom start_scale
    xalign 0.5
    yalign 0.5
    linear duration zoom end_scale

screen creepy_blue_screen():
    add "images/bluescreen.png" at zoom_in(5.0, 1.0, 1.2) xysize (config.screen_width, config.screen_height)
