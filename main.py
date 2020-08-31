def on_gesture_shake():
    basic.show_number(randint(1, 6))
    
input.on_gesture(Gesture.Shake, on_gesture_shake)