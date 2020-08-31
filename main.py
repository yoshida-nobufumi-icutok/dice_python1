#これはテストです。
def on_gesture_shake():
    rand_set = randint(1, 6)
    basic.show_number(rand_set)
    basic.pause(500)
    basic.show_number(rand_set+1)
    basic.clear_screen()

input.on_gesture(Gesture.SHAKE, on_gesture_shake)
