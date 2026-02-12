init -2 python:
    renpy.music.register_channel(
        "ambient",
        mixer="music", 
        loop=True,
        tight=True
    )

init python:
    class Ambient:
        def play(self, file, fadein=2.0):
            renpy.music.play(
                file,
                channel="ambient",
                loop=True,
                fadein=fadein
            )

        def stop(self, fadeout=2.0):
            renpy.music.stop(
                channel="ambient",
                fadeout=fadeout
            )

        def set_volume(self, volume):
            renpy.music.set_volume(
                volume,
                channel="ambient"
            )

        def is_playing(self):
            return renpy.music.is_playing(channel="ambient")

    ambient = Ambient()
