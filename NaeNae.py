from naoqi import ALProxy
import almath


def naeNae(motion_proxy):
    motion_proxy.openHand("RHand")

    names      = ["RKneePitch", "LKneePitch","LHipPitch", "RHipPitch",
                  "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
                  "RWristYaw"]
    angleLists = [25*almath.TO_RAD, 25*almath.TO_RAD, -32*almath.TO_RAD, -32*almath.TO_RAD,
                  -100*almath.TO_RAD, -76*almath.TO_RAD, 20*almath.TO_RAD, 60*almath.TO_RAD,
                  10*almath.TO_RAD]

    timeLists = 1.0
    isAbsolute = True

    #motionProxy.stiffnessInterpolation(stiffnessNames, stiffnessList, timeLists)
    motion_proxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    motion_proxy.waitUntilMoveIsFinished()

    names2 = ["LHipRoll", "RHipRoll", "RElbowRoll"]
    angleLists2 = [-10 * almath.TO_RAD, -10 * almath.TO_RAD, 88.5 * almath.TO_RAD]
    timeLists = 0.6
    motion_proxy.angleInterpolation(names2, angleLists2, timeLists, isAbsolute)



    names3 = ["LHipRoll", "RHipRoll", "RElbowRoll"]
    angleLists3 = [10 * almath.TO_RAD, 10 * almath.TO_RAD, 30 * almath.TO_RAD]
    timeLists = 0.6
    motion_proxy.angleInterpolation(names3, angleLists3, timeLists, isAbsolute)


def whip(motion_proxy):

    motion_proxy.closeHand("RHand")

    names = ["RElbowYaw", "RWristYaw"]
    angleLists = [80 * almath.TO_RAD, 80 * almath.TO_RAD]
    timeLists = 0.5
    isAbsolute = True
    motion_proxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)


    names = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RWristYaw" , "RElbowYaw"]
    angleLists = [-10 * almath.TO_RAD, -0 * almath.TO_RAD, -50* almath.TO_RAD, -10* almath.TO_RAD, -15* almath.TO_RAD]
    motion_proxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    motion_proxy.waitUntilMoveIsFinished()

    naeNae(motion_proxy)

def armDown(arm):


tts = ALProxy("ALTextToSpeech", "169.254.123.55", 9559)
try:
    motion_proxy = ALProxy("ALMotion", "169.254.123.55", 9559)
except Exception as e:
    print("Could not create proxy to ALMotion")
    print('{}{}'.format("Error was: ", e))

isEnabled = True
motion_proxy.wbEnable(isEnabled)

namesStiff = ["Body"]
stiffnessList = 1.0
stiffTime = 5.0
motion_proxy.stiffnessInterpolation(namesStiff, stiffnessList, stiffTime)

whip(motion_proxy)

