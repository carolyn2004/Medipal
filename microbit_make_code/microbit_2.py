def on_received_string(receivedString):
    global signal, volume
    signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    # Map signal strength to a range of volume levels (0 to 255)
    volume = Math.map(signal, -95, -42, 0, 255)
    music.set_volume(max(0, min(255, volume)))
    # Ensure volume is within valid range
    if signal > -60:
        # If close, play louder sound
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    elif signal <= -60 and signal > -80:
        # If further, play softer sound
        music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)), music.PlaybackMode.UNTIL_DONE)
    radio.send_number(signal)

radio.on_received_string(on_received_string)

start_time = 0
volume = 0
signal = 0
radio.set_group(213)
pill_count = 14

def on_every_interval():
    global start_time, pill_count
    start_time += 1
    if start_time == 31 or start_time == 62 or start_time == 93:
        music.set_volume(255)
        while True:
            music.play_tone(252, music.beat(BeatFraction.WHOLE))
            if input.acceleration(Dimension.Y) < -1000 or input.acceleration(Dimension.Y) > 1000:
                basic.clear_screen()
                pill_count -= 2
                pill_count = max(0, pill_count)
                radio.send_value("num_pills", pill_count)
                music.stop_all_sounds()

    # Reset `start_time` every 9000 seconds
    if start_time == 9000:
        start_time = 0

loops.every_interval(1000, on_every_interval)
