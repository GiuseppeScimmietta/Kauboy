# Kauboy
Kauboy

step("sdfsdfsfsdf"):
    OPC.Connect()
    realize(setSpeedReference):
        Drive.setSpeed(refSpeed)
        setMove =Drive.move()
    observe:
        speed = readSpeed()*100 
        moving = readStatus()
    expect:
        moving = true
        intolerance =  speed > Speed Tolerance
