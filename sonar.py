# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:11:20 2021

@author: YAP
"""
import time
from pymata4 import pymata4

trigger_pin = 5
echo_pin = 3

board  = pymata4.Pymata4('com3')

# dis= ''

def the_callback(data):
    the_callback.dis = data[2]
    
    # print("distance", the_callback.dis,'cm')
    

### param timeout: a tuning parameter. 80000UL equals 80ms.
# board.set_pin_mode_sonar(trigger_pin, echo_pin, the_callback,timeout=8000)
# board.set_pin_mode_sonar(trigger_pin, echo_pin,the_callback)
board.set_pin_mode_sonar(trigger_pin, echo_pin,the_callback)

# c=0
# while c<5:
#     board.set_pin_mode_sonar(trigger_pin, echo_pin)
#     c+=1
while True:    
    # board.set_pin_mode_sonar(trigger_pin, echo_pin, the_callback,timeout=8000)
    try:
        time.sleep(1)
        board.sonar_read(trigger_pin)
        print(the_callback.dis)
        
    except Exception: 
        board.shutdown()
        # board.exit()
