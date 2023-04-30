function rockpaperscissors () {
    play = randint(1, 3)
    if (play == 1) {
        radio.sendString("scissors")
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            . # . # .
            `)
    } else if (play == 2) {
        radio.sendString("rock")
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else if (play == 3) {
        radio.sendString("paper")
        basic.showLeds(`
            # . # . #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
}
function loose () {
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 100)
    basic.pause(1000)
    maqueen.motorStop(maqueen.Motors.All)
}
function win () {
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 100)
    basic.pause(1000)
    maqueen.motorStop(maqueen.Motors.All)
}
input.onGesture(Gesture.Shake, function () {
    rockpaperscissors()
})
let play = 0
radio.setGroup(1)
