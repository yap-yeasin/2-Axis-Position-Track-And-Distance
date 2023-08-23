# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:11:20 2021

@author: YAP
"""
import serial

# Arduino = serial.Serial('COM3',9600)
Arduino = serial.Serial('COM3',57600)

while True:
    if (Arduino.inWaiting()>0):
        data = Arduino.readline()
        print(data)