# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:11:20 2021

@author: YAP
"""
import pyfirmata
import time
import datetime as dt

board = pyfirmata.Arduino('com3')

start=0
end=0

# trigpin = board.get_pin('d:5:o')
# echopin= board.get_pin('d:3:i')

# trigpin.write(0)
# time.sleep(5)

# while True:
#     trigpin.write(1)
#     time.sleep(3)
#     trigpin.write(0)

#     while echopin.write(0):
#         pass
#         start = time.time()
#     while echopin.write(1):
#         pass
#         end = time.time()

#     print((end - start)/58.0*1000000)
#     time.sleep(1)
   
    
it = pyfirmata.util.Iterator(board)
it.start()

sonarEcho = board.get_pin('d:3:i')
sonarTrig = board.get_pin('d:5:o')
while True:

    for i in range(10):
        sonarTrig.write(i)
    
    time.sleep(1)
    
    sonarTrig.write(1)
    time.sleep(0.000010)
    sonarTrig.write(0)
    # # # # # direct write doesnt work either => board.digital[12].write(0)
    
    while sonarEcho.read() is None:
        t1 = time.time()
        pass
    # t1 = dt.datetime.now()
    # t1 = time.time()
    
    while sonarEcho.read():
        t2 = time.time()
        pass
    # t2 = dt.datetime.now()
    # t2 = time.time()
    
    # t3 = (t2 - t1).microseconds
    t3 = (t2 - t1)*1000000
    # t3 = (t2 - t1)*0.034 / 2
    
    distance = t3 / 58
    print ('Distnce:', distance, 'cm:')
    print (t1, t2 ,t3)