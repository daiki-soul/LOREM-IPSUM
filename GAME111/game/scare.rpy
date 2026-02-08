
screen jumpscare():
    add "images/jumpscare.png" xysize (config.screen_width, config.screen_height)


transform zoom_in(duration=10.0, start_scale=3.0, end_scale=1.2):

    zoom start_scale
    xalign 0.5
    yalign 0.5
    linear duration zoom end_scale

transform dim_blue_screen:
    # Start fully opaque
    alpha 1.0
    linear 10.0 alpha 0.3  # over 10 seconds, dim to 30% opacity


screen creepy_blue_screen():
    add "images/bluescreen.png" at dim_blue_screen xysize (config.screen_width, config.screen_height)
    
