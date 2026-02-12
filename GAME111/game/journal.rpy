# journal.rpy

init python:
    import os

    # Ensure persistent variable exists
    if not hasattr(persistent, "journal_text") or persistent.journal_text is None:
        persistent.journal_text = ""

    # Optional backup to game root folder
    def save_journal():
        path = renpy.exports.config.gamedir + "/journal.txt"
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(persistent.journal_text)
        except:
            pass
