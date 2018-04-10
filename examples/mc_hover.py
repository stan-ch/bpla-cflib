# -*- coding: utf-8 -*-
"""
This script show control Z when hovering by means of MotionCommander class.
"""
import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/250K'
TIME_SEC = 1
# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        # We take off when the commander is created
        input("Press <RET> to take off. Z = 0.3m ")

        with MotionCommander(scf) as mc:
            time.sleep(TIME_SEC)

            input("Press <RET> to up. Z = 0.6m ")
            mc.up(0.3)
            time.sleep(TIME_SEC)

            input("Press <RET> to up. Z = 1.0m ")
            mc.up(0.4)
            time.sleep(TIME_SEC)

            input("Press <RET> to turn left 360 degrees then turn right 360 degrees")
            mc.turn_left(360)
            time.sleep(TIME_SEC)
            mc.turn_right(360)
            time.sleep(TIME_SEC)

            input("Press <RET> to down. Z = 0.6m ")
            mc.down(0.4)
            time.sleep(TIME_SEC)

            # We land when the MotionCommander goes out of scope
            input("Press <RET> to land ")
