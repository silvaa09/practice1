music.play(music.string_playable("- - - - - - - - ", 120),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    pass
basic.forever(on_forever)
