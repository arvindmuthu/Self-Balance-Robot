#!/usr/bin/python
"""
*************************************************
* @Project: Self Balance                         
* @Description: Trace module
* @Owner: Guilherme Chinellato                   
* @Email: guilhermechinellato@gmail.com                              
*************************************************
"""

import logging

'''
NOTSET = 0
DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
'''

NOTSET = 0
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50

#Flag debug control: Max 32 Modules
BASE_ADDR = 0x01
MODULE_MANAGER = BASE_ADDR
MODULE_BALANCE = BASE_ADDR << 1
MODULE_BLUETOOTH = BASE_ADDR << 2
MODULE_CLIENT_UDP = BASE_ADDR << 3
MODULE_SERVER_UDP = BASE_ADDR << 4
MODULE_CV = BASE_ADDR << 5
MODULE_MOTION = BASE_ADDR << 6
MODULE_PANTILT = BASE_ADDR << 7
MODULE_IMU = BASE_ADDR << 8
MODULE_IMU_ACCEL = BASE_ADDR << 9
MODULE_IMU_GYRO = BASE_ADDR << 10
MODULE_IMU_MAG = BASE_ADDR << 11
MODULE_IMU_BAROM = BASE_ADDR << 12
MODULE_I2C = BASE_ADDR << 13

#Verbosity level
#logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(processName)s) (%(threadName)s) (%(module)s) %(message)s')
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(processName)s) (%(threadName)s) (%(module)s) %(message)s')
#logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(processName)s) (%(threadName)s) (%(module)s) (%(filename)s) (Fct: %(funcName)s) (Line:%(lineno)d) %(message)s')

