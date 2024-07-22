import cv2
import numpy as np
from Coordinate import camera
from ModelLabelDetector import Label_Detector
from IntegrationCode.Rpi import motor_control as mc
from IntegrationCode.Rpi import ultrasonic
import threading 
import time

cam=cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()
    if ret is None:
        break
    time.sleep(8)

    coordinates=camera.boxdetection(frame)
    label=Label_Detector.labelcamera(0)
    print(coordinates)
    print(label)
    x=coordinates[0]
    y=coordinates[1]
    thread_x = threading.Thread(target=mc.move_stepper_motor_MX,args=(x,-5))
    thread_y = threading.Thread(target=mc.move_stepper_motor_MZ1,args=(y,5))
    thread_x.start()
    thread_y.start()
    thread_x.join()
    thread_y.join()
    dist=ultrasonic.measure_distance()
    if dist<=270:
        # thread.motorcontrolz1_threading.start(dist,1)
        mc.move_stepper_motor_MZ1(dist,1)
    else:
        thread_z1=threading.Thread(target=mc.move_stepper_motor_MZ,args=(270,1))
        thread_z2=threading.Thread(target=mc.move_stepper_motor_MZ1,args=(dist-270,1))
        thread_z1.start()
        thread_z2.start()
        
        thread_z1.join()
        thread_z2.join()

    mc.suction_on()
    if dist<=270:
        # thread.motorcontrolz1_threading.start(dist,1)
        mc.move_stepper_motor_MZ1(dist,-1)
    else:
        thread_z11=threading.Thread(target=mc.move_stepper_motor_MZ,args=(270,-1))
        thread_z21=threading.Thread(target=mc.move_stepper_motor_MZ1,args=(dist-270,-1))
        thread_z11.start()
        thread_z21.start()
        
        thread_z11.join()
        thread_z21.join()

    if label==1:
        print("Label Found")
        mc.move_stepper_motor_MX(x,5)
        mc.move_stepper_motor_MY(y,-5)

        mc.move_stepper_motor_MZ1(150,5)
        mc.suction_off()
        mc.move_stepper_motor_MZ1(150,-5)

    else :
        mc.move_stepper_motor_MX(x,5)
        mc.move_stepper_motor_MY(y,-5)
        if(Label_Detector.labelcamera(2)==1 & Label_Detector.labelcamera(4)==0): #label is on side face
            print('rotating MZ2')
            mc.move_stepper_motor_MZ2(50,1)
            mc.move_stepper_motor_MZ1(150,5)
            print('rotated one time MZ2')
            dist1=ultrasonic.measure_distance()
            dist2=ultrasonic.measure_distance()
            mc.move_stepper_motor_M21(dist1,5)
            mc.move_stepper_motor_M22(dist2,5)
            mc.suction_off()
            mc.move_stepper_motor_M1(50,-5)

        if(Label_Detector.labelcamera(2)==0 & Label_Detector.labelcamera(4)==1): #label is on front face
            mc.move_stepper_motor_MZ2(50,1)
            mc.move_stepper_motor_MZ1(150,5)
            dist1=ultrasonic.measure_distance()
            dist2=ultrasonic.measure_distance()
            mc.move_stepper_motor_M21(dist1,5)
            mc.move_stepper_motor_M22(dist2,5)
            mc.suction_off()
            mc.move_stepper_motor_M1(50,-5)
        
        if(Label_Detector.labelcamera(2)==0 & Label_Detector.labelcamera(3)==0): #label is not present on both faces
            print('rotating MZ2')
            mc.move_stepper_motor_MZ2(200,1)
            print('rotated one time MZ2')
            if(Label_Detector.labelcamera(2)==1 & Label_Detector.labelcamera(4)==0): #label is on side face
                print('rotating MZ2')
                mc.move_stepper_motor_MZ2(50,1)
                mc.move_stepper_motor_MZ1(150,5)
                print('rotated one time MZ2')
                dist1=ultrasonic.measure_distance()
                dist2=ultrasonic.measure_distance()
                mc.move_stepper_motor_M21(dist1,5)
                mc.move_stepper_motor_M22(dist2,5)
                mc.suction_off()
                mc.move_stepper_motor_M1(50,-5)
            elif(Label_Detector.labelcamera(2)==0 & Label_Detector.labelcamera(4)==1): #label is on front face
                mc.move_stepper_motor_MZ2(50,1)
                mc.move_stepper_motor_MZ1(150,5)
                dist1=ultrasonic.measure_distance()
                dist2=ultrasonic.measure_distance()
                mc.move_stepper_motor_M21(dist1,5)
                mc.move_stepper_motor_M22(dist2,5)
                mc.suction_off()
                mc.move_stepper_motor_M1(50,-5)
            else: 
                mc.move_stepper_motor_MZ1(150,5)
                dist1=ultrasonic.measure_distance()
                dist2=ultrasonic.measure_distance()
                mc.move_stepper_motor_M21(dist1,5)
                mc.move_stepper_motor_M22(dist2,5)
                mc.suction_off()
                mc.move_stepper_motor_M1(100,-5)
                mc.move_stepper_motor_M21(dist1,-5)
                mc.move_stepper_motor_M22(dist2,-5)

        mc.move_stepper_motor_MZ1(150,-5)




