def on_received_string(message):
    # basic.clear_screen()
    serial.write_string("" + (message))
radio.on_received_string(on_received_string)

# Set up the callback for when a named value is received
def on_received_value(name, value):
    global stored_time
    # Store the received data
    stored_time = value
    # Store the received numeric value
    if name == "temp":
        serial.write_value("temp", stored_time)
    else:
        serial.write_value("value", stored_time)
    # Write the actual received value to serial
    basic.show_number(stored_time)
    pause(5000)
    basic.clear_screen()
radio.on_received_value(on_received_value)

stored_time = 0
radio.set_group(213)
