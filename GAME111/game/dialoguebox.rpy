screen say(who, what):
    if who:#dialogue
        window:
            add "gui/dialogue_box.png"
            text who id "who" xpos gui.name_xpos ypos gui.name_ypos style "dialogue_text_left"
            text what id "what" xpos gui.dialogue_xpos ypos gui.dialogue_ypos xmaximum gui.dialogue_width style "dialogue_text_left"
    else:#monologue
        window:
            add "gui/monologue_box.png"
            text what id "what" xpos gui.dialogue_xpos ypos gui.dialogue_ypos xmaximum gui.dialogue_width style "monologue_text_left"
