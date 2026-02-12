transform film_grain_transform:
    xpos 0
    ypos 0
    alpha 0.08
    linear 0.1 xpos 5 ypos -5 alpha 0.12
    linear 0.1 xpos -5 ypos 5 alpha 0.05
    repeat
screen film_grain_effect():
    modal False
    add Solid("#000000") at film_grain_transform
