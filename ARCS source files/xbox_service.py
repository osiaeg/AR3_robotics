import time


### BUTTON JOGGING DEFS ############################################################################################################## BUTTON JOGGING DEFS ###
def xbox():
    def xbox_thread():
        from inputs import get_gamepad
        global xboxUse
        jogMode = 1
        if xboxUse == 0:
            xboxUse = 1
            mainMode = 1
            jogMode = 1
            grip = 0
            almStatusLab.config(text='JOGGING JOINTS 1 & 2', bg="lightgreen")
            almStatusLab2.config(text='JOGGING JOINTS 1 & 2', bg="lightgreen")
            xbcStatusLab.config(text='Xbox ON', bg="lightgreen")
            change_distance(2)
        else:
            xboxUse = 0
            almStatusLab.config(text='XBOX CONTROLLER OFF', bg="salmon")
            almStatusLab2.config(text='XBOX CONTROLLER OFF', bg="salmon")
            xbcStatusLab.config(text='Xbox OFF', bg="salmon")
        while xboxUse == 1:
            try:
                events = get_gamepad()
                for event in events:
                    ##DISTANCE
                    if event.code == 'ABS_RZ' and event.state >= 100:
                        change_distance(0)
                    elif event.code == 'ABS_Z' and event.state >= 100:
                        change_distance(1)
                    ##SPEED
                    elif event.code == 'BTN_TR' and event.state == 1:
                        change_speed(0, speedEntryField)
                    elif event.code == 'BTN_TL' and event.state == 1:
                        change_speed(1, speedEntryField)
                    ##JOINT MODE
                    elif event.code == 'BTN_WEST' and event.state == 1:
                        if mainMode != 1:
                            mainMode = 1
                            jogMode = 1
                            almStatusLab.config(text='JOGGING JOINTS 1 & 2', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING JOINTS 1 & 2', bg="lightgreen")
                        else:
                            jogMode += 1
                        if jogMode == 2:
                            almStatusLab.config(text='JOGGING JOINTS 3 & 4', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING JOINTS 3 & 4', bg="lightgreen")
                        elif jogMode == 3:
                            almStatusLab.config(text='JOGGING JOINTS 5 & 6', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING JOINTS 5 & 6', bg="lightgreen")
                        elif jogMode == 4:
                            jogMode = 1
                            almStatusLab.config(text='JOGGING JOINTS 1 & 2', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING JOINTS 1 & 2', bg="lightgreen")
                    ##JOINT JOG
                    elif mainMode == 1 and event.code == 'ABS_HAT0X' and event.state == 1 and jogMode == 1:
                        J1jogNeg()
                    elif mainMode == 1 and event.code == 'ABS_HAT0X' and event.state == -1 and jogMode == 1:
                        J1jogPos()
                    elif mainMode == 1 and event.code == 'ABS_HAT0Y' and event.state == -1 and jogMode == 1:
                        J2jogNeg()
                    elif mainMode == 1 and event.code == 'ABS_HAT0Y' and event.state == 1 and jogMode == 1:
                        J2jogPos()
                    elif mainMode == 1 and event.code == 'ABS_HAT0Y' and event.state == -1 and jogMode == 2:
                        J3jogNeg()
                    elif mainMode == 1 and event.code == 'ABS_HAT0Y' and event.state == 1 and jogMode == 2:
                        J3jogPos()
                    elif mainMode == 1 and event.code == 'ABS_HAT0X' and event.state == 1 and jogMode == 2:
                        J4jogNeg()
                    elif mainMode == 1 and event.code == 'ABS_HAT0X' and event.state == -1 and jogMode == 2:
                        J4jogPos()
                    elif mainMode == 1 and event.code == 'ABS_HAT0Y' and event.state == -1 and jogMode == 3:
                        J5jogNeg()
                    elif mainMode == 1 and event.code == 'ABS_HAT0Y' and event.state == 1 and jogMode == 3:
                        J5jogPos()
                    elif mainMode == 1 and event.code == 'ABS_HAT0X' and event.state == 1 and jogMode == 3:
                        J6jogNeg()
                    elif mainMode == 1 and event.code == 'ABS_HAT0X' and event.state == -1 and jogMode == 3:
                        J6jogPos()
                    ##CARTESIAN DIR MODE
                    elif event.code == 'BTN_SOUTH' and event.state == 1:
                        if mainMode != 2:
                            mainMode = 2
                            jogMode = 1
                            almStatusLab.config(text='JOGGING X & Y AXIS', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING X & Y AXIS', bg="lightgreen")
                        else:
                            jogMode += 1
                        if jogMode == 2:
                            almStatusLab.config(text='JOGGING Z AXIS', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING Z AXIS', bg="lightgreen")
                        elif jogMode == 3:
                            jogMode = 1
                            almStatusLab.config(text='JOGGING X & Y AXIS', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING X & Y AXIS', bg="lightgreen")
                    ##CARTESIAN DIR JOG
                    elif mainMode == 2 and event.code == 'ABS_HAT0Y' and event.state == -1 and jogMode == 1:
                        XjogNeg()
                    elif mainMode == 2 and event.code == 'ABS_HAT0Y' and event.state == 1 and jogMode == 1:
                        XjogPos()
                    elif mainMode == 2 and event.code == 'ABS_HAT0X' and event.state == 1 and jogMode == 1:
                        YjogNeg()
                    elif mainMode == 2 and event.code == 'ABS_HAT0X' and event.state == -1 and jogMode == 1:
                        YjogPos()
                    elif mainMode == 2 and event.code == 'ABS_HAT0Y' and event.state == 1 and jogMode == 2:
                        ZjogNeg()
                    elif mainMode == 2 and event.code == 'ABS_HAT0Y' and event.state == -1 and jogMode == 2:
                        ZjogPos()
                    ##CARTESIAN ORIENTATION MODE
                    elif event.code == 'BTN_EAST' and event.state == 1:
                        if mainMode != 3:
                            mainMode = 3
                            jogMode = 1
                            almStatusLab.config(text='JOGGING Rx & Ry AXIS', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING Rx & Ry AXIS', bg="lightgreen")
                        else:
                            jogMode += 1
                        if jogMode == 2:
                            almStatusLab.config(text='JOGGING Rz AXIS', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING Rz AXIS', bg="lightgreen")
                        elif jogMode == 3:
                            jogMode = 1
                            almStatusLab.config(text='JOGGING Rx & Ry AXIS', bg="lightgreen")
                            almStatusLab2.config(text='JOGGING Rx & Ry AXIS', bg="lightgreen")
                    ##CARTESIAN ORIENTATION JOG
                    elif mainMode == 3 and event.code == 'ABS_HAT0X' and event.state == -1 and jogMode == 1:
                        RxjogNeg()
                    elif mainMode == 3 and event.code == 'ABS_HAT0X' and event.state == 1 and jogMode == 1:
                        RxjogPos()
                    elif mainMode == 3 and event.code == 'ABS_HAT0Y' and event.state == 1 and jogMode == 1:
                        RyjogNeg()
                    elif mainMode == 3 and event.code == 'ABS_HAT0Y' and event.state == -1 and jogMode == 1:
                        RyjogPos()
                    elif mainMode == 3 and event.code == 'ABS_HAT0X' and event.state == 1 and jogMode == 2:
                        RzjogNeg()
                    elif mainMode == 3 and event.code == 'ABS_HAT0X' and event.state == -1 and jogMode == 2:
                        RzjogPos()
                    ##TRACK MODE
                    elif event.code == 'BTN_START' and event.state == 1:
                        mainMode = 4
                        almStatusLab.config(text='JOGGING TRACK', bg="lightgreen")
                        almStatusLab2.config(text='JOGGING TRACK', bg="lightgreen")
                    ##TRACK JOG
                    elif mainMode == 4 and event.code == 'ABS_HAT0X' and event.state == 1:
                        TrackjogPos()
                    elif mainMode == 4 and event.code == 'ABS_HAT0X' and event.state == -1:
                        TrackjogNeg()
                    ##TEACH POS
                    elif event.code == 'BTN_NORTH' and event.state == 1:
                        teachInsertBelSelected()
                    ##GRIPPER
                    elif event.code == 'BTN_SELECT' and event.state == 1:
                        if grip == 0:
                            grip = 1
                            outputNum = DO1offEntryField.get()
                            command = "OFX" + outputNum + "\n"
                            serial_arduino.write(command.encode())
                            serial_arduino.flushInput()
                            time.sleep(.2)
                            serial_arduino.read()
                        else:
                            grip = 0
                            outputNum = DO1onEntryField.get()
                            command = "ONX" + outputNum + "\n"
                            serial_arduino.write(command.encode())
                            serial_arduino.flushInput()
                            time.sleep(.2)
                            serial_arduino.read()
                            time.sleep(.1)
            except:
                almStatusLab.config(text='XBOX CONTROLLER NOT RESPONDING', bg="red")
                almStatusLab2.config(text='XBOX CONTROLLER NOT RESPONDING', bg="red")
                tab6.ElogView.insert(tk.END, get_current_time() + " - " + "XBOX CONTROLLER NOT RESPONDING")
                value = tab6.ElogView.get(0, tk.END)
                pickle.dump(value, open("ErrorLog", "wb"))

    t = threading.Thread(target=xbox_thread)
    t.start()


# Xbox func
def change_distance(val):
    curSpd = int(J1jogDegsEntryField.get())
    if curSpd >= 100 and val == 0:
        curSpd = 100
    elif curSpd < 5 and val == 0:
        curSpd += 1
    elif val == 0:
        curSpd += 5
    if curSpd <= 1 and val == 1:
        curSpd = 1
    elif curSpd <= 5 and val == 1:
        curSpd -= 1
    elif val == 1:
        curSpd -= 5
    elif val == 2:
        curSpd = 5
    J1jogDegsEntryField.delete(0, 'end')
    J2jogDegsEntryField.delete(0, 'end')
    J3jogDegsEntryField.delete(0, 'end')
    J4jogDegsEntryField.delete(0, 'end')
    J5jogDegsEntryField.delete(0, 'end')
    J6jogDegsEntryField.delete(0, 'end')
    XjogEntryField.delete(0, 'end')
    YjogEntryField.delete(0, 'end')
    ZjogEntryField.delete(0, 'end')
    RxjogEntryField.delete(0, 'end')
    RyjogEntryField.delete(0, 'end')
    RzjogEntryField.delete(0, 'end')
    TXjogEntryField.delete(0, 'end')
    TYjogEntryField.delete(0, 'end')
    TZjogEntryField.delete(0, 'end')
    TRxjogEntryField.delete(0, 'end')
    TRyjogEntryField.delete(0, 'end')
    TRzjogEntryField.delete(0, 'end')
    J1jogDegsEntryField.insert(0, str(curSpd))
    J2jogDegsEntryField.insert(0, str(curSpd))
    J3jogDegsEntryField.insert(0, str(curSpd))
    J4jogDegsEntryField.insert(0, str(curSpd))
    J5jogDegsEntryField.insert(0, str(curSpd))
    J6jogDegsEntryField.insert(0, str(curSpd))
    XjogEntryField.insert(0, str(curSpd))
    YjogEntryField.insert(0, str(curSpd))
    ZjogEntryField.insert(0, str(curSpd))
    RxjogEntryField.insert(0, str(curSpd))
    RyjogEntryField.insert(0, str(curSpd))
    RzjogEntryField.insert(0, str(curSpd))
    TXjogEntryField.insert(0, str(curSpd))
    TYjogEntryField.insert(0, str(curSpd))
    TZjogEntryField.insert(0, str(curSpd))
    TRxjogEntryField.insert(0, str(curSpd))
    TRyjogEntryField.insert(0, str(curSpd))
    TRzjogEntryField.insert(0, str(curSpd))
    time.sleep(.3)


# Xbox func
def change_speed(val, speed_field):
    curSpd = int(speed_field.get())
    if curSpd >= 100 and val == 0:
        curSpd = 100
    elif curSpd < 5 and val == 0:
        curSpd += 1
    elif val == 0:
        curSpd += 5
    if curSpd <= 1 and val == 1:
        curSpd = 1
    elif curSpd <= 5 and val == 1:
        curSpd -= 1
    elif val == 1:
        curSpd -= 5
    elif val == 2:
        curSpd = 5
    speed_field.delete(0, 'end')
    speed_field.insert(0, str(curSpd))