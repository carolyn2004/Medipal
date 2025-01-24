def on_forever():
    global pill_count
    # new code here
    if input.logo_is_pressed():
        basic.show_number(2)
    else:
        basic.clear_screen()
    if input.button_is_pressed(Button.B):
        pill_count = 14
        radio.send_value("Refill", pill_count)
        basic.pause(1000)
basic.forever(on_forever)
