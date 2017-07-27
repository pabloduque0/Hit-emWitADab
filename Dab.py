from naoqi import ALProxy
import almath

tts = ALProxy("ALTextToSpeech", "your_robot_ip", 9559)
motionProxy = ALProxy("ALMotion", "your_robot_ip", 9559)

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
motionProxy.openHand("RHand")
motionProxy.openHand("LHand")
motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
tts.say("Daab")
