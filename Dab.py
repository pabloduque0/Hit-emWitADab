from naoqi import ALProxy
import almath


try:
    tts = ALProxy("ALTextToSpeech", "your_robot_ip", 9559)
except Exception as e:
    print("Could not create proxy to ALTextToSpeech")
    print('{}{}'.format("Error was: ", e))


try:
    motion_proxy = ALProxy("ALMotion", "169.254.123.55", 9559)
except Exception as e:
    print("Could not create proxy to ALMotion")
    print('{}{}'.format("Error was: ", e))

names      = ["LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw",
              "LShoulderPitch", "RElbowRoll", "LHipPitch", "RHipPitch",
              "HeadPitch", "HeadYaw", "RShoulderPitch", "RShoulderRoll",
              "RElbowYaw"]

angleLists = [76.0*almath.TO_RAD, 88.5*almath.TO_RAD, -10*almath.TO_RAD, -10*almath.TO_RAD,
              119*almath.TO_RAD, 88.5*almath.TO_RAD, -8*almath.TO_RAD, -8*almath.TO_RAD,
              25*almath.TO_RAD, -20*almath.TO_RAD, -20*almath.TO_RAD, 75.0*almath.TO_RAD,
              10*almath.TO_RAD]

timeLists = 1.3
isAbsolute = True
motion_proxy.openHand("RHand")
motion_proxy.openHand("LHand")
motion_proxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
tts.say("Daab")
