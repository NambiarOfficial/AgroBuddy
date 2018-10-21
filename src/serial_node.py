#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import Int16
import time
rospy.init_node('arduino_serial_node')
imu_publisher = rospy.Publisher('imu_data',Int16,queue_size=10)

ser = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',115200)

print('Initialised')
while True:
	data = ser.read()
	if data.isdigit():
		print(int(data))
		data = int(data)
		imu_publisher.publish(data)
	# time.sleep(1)