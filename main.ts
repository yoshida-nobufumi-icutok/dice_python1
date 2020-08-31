// これはテストです。
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    let rand_set = randint(1, 6)
    basic.showNumber(rand_set)
    basic.pause(500)
    basic.showNumber(rand_set + 1)
    basic.clearScreen()
})
