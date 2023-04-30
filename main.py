def rockpaperscissors():
    global play
    play = randint(1, 3)
    if play == 1:
        radio.send_string("scissors")
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        . # . # .
        """)
    elif play == 2:
        radio.send_string("rock")
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    elif play == 3:
        radio.send_string("paper")
        basic.show_leds("""
            # . # . #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
def loose():
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 100)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)
def win():
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)

def on_gesture_shake():
    rockpaperscissors()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

play = 0
radio.set_group(1)