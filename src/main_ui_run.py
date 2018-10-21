#!/usr/bin/env python

import rospy
from main_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import sys
from std_msgs.msg import UInt8
from agrobuddy.msg import sensors
from weather_plot import plot_weather

button_off_stylesheet = 'QPushButton {background-color : #FF0000; color : black;}'
button_on_stylesheet = 'QPushButton {background-color : #005000; color : white;}'

class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent=parent)
		self.setupUi(self)
		
		rospy.init_node('base_node')
		self.navigation_publisher = rospy.Publisher('navigation', UInt8, queue_size=10)
		rospy.Subscriber('sensor_data',sensors, self.air_quality_callback)
		
		self.all_components = [self.air_quality_label_temp, self.air_quality_label_humidity, self.air_quality_label_pressure, self.air_quality_label_methane, self.air_quality_label_nitrogen, self.air_quality_label_oxygen, self.air_quality_label_carbon_dioxide, self.weather_label_1, self.weather_label_2, self.weather_label_3]

		self.button_status = {
			True : button_on_stylesheet,
			False : button_off_stylesheet
			}
		self.button_values = {
				'AIR' : {
						'active' : False, 
						'button' : self.air_quality_button,
						'components' : [self.air_quality_label_temp, self.air_quality_label_humidity, self.air_quality_label_pressure, self.air_quality_label_methane,self.air_quality_label_nitrogen, self.air_quality_label_oxygen, self.air_quality_label_carbon_dioxide]
						},
				'WEA' : {
						'active' : False, 
						'button' : self.weather_button,
						'components' : [self.weather_label_1, self.weather_label_2, self.weather_label_3]
						},
				'CRO' : {
						'active' : False, 
						'button' : self.crop_selection_button,
						'components' : []
						},
				'PLA' : {
						'active' : False, 
						'button' : self.plant_health_button,
						'components' : []
						},
				'NEW' : {
						'active' : False, 
						'button' : self.news_button,
						'components' : []
						},
				'ASS' : {
						'active' : False, 
						'button' : self.assistance_button,
						'components' : []
						},
				'FOR' : {
						'active' : False, 
						'button' : self.forum_button,
						'components' : []
						}
			}
		for component in self.all_components:
			component.hide()

		self.air_quality_button.setStyleSheet(button_off_stylesheet)
		self.weather_button.setStyleSheet(button_off_stylesheet)
		self.crop_selection_button.setStyleSheet(button_off_stylesheet)
		self.plant_health_button.setStyleSheet(button_off_stylesheet)
		self.news_button.setStyleSheet(button_off_stylesheet)
		self.assistance_button.setStyleSheet(button_off_stylesheet)
		self.forum_button.setStyleSheet(button_off_stylesheet)

		self.air_quality_button.clicked.connect(lambda: self.toggle_stylesheet('AIR'))
		self.weather_button.clicked.connect(lambda: self.toggle_stylesheet('WEA'))
		self.weather_button.clicked.connect(lambda: plot_weather)
		self.crop_selection_button.clicked.connect(lambda: self.toggle_stylesheet('CRO'))
		self.plant_health_button.clicked.connect(lambda: self.toggle_stylesheet('PLA'))
		self.news_button.clicked.connect(lambda: self.toggle_stylesheet('NEW'))
		self.assistance_button.clicked.connect(lambda: self.toggle_stylesheet('ASS'))
		self.forum_button.clicked.connect(lambda: self.toggle_stylesheet('FOR'))
		self.show()

	def air_quality_callback(self,msg):
		'''
			Displays data from the bot on the UI
		'''
		print(msg)
		self.air_quality_label_temp.setText('Temp : ' + str(msg.temp))
		self.air_quality_label_humidity.setText('Humidity : ' + str(msg.humidity))
		self.air_quality_label_pressure.setText('Pressure : ' + str(msg.pressure))
		self.air_quality_label_methane.setText('Methane : ' + str(msg.methane))
		self.air_quality_label_nitrogen.setText('Nitrogen : ' + str(300))
		self.air_quality_label_oxygen.setText('Oxygen : ' + str(300))
		self.air_quality_label_carbon_dioxide.setText('CO2 : ' + str(300))

	def toggle_stylesheet(self,button):
		'''
			Toggles the stylesheet on button click
		'''
		self.button_values[button]['active'] = not self.button_values[button]['active']
		curr_status = self.button_values[button]['active']
		self.button_values[button]['button'].setStyleSheet(self.button_status[curr_status])

		for component in self.all_components:
			component.hide()

		if curr_status:
			for component in self.button_values[button]['components']:
				component.show()

	def keyPressEvent(self, event):
		'''
			Checks key press event and moves bot accordingly
		'''
		key = event.key()
		if key == QtCore.Qt.Key_W:
			print('Moving Forward')
			self.navigation_publisher.publish(1)
		elif key == QtCore.Qt.Key_S:
			print('Moving Back')
			self.navigation_publisher.publish(2)
		elif key == QtCore.Qt.Key_A:
			print('Moving Left')
			self.navigation_publisher.publish(4)
		elif key == QtCore.Qt.Key_D:
			print('Moving Right')
			self.navigation_publisher.publish(3)

	def keyReleaseEvent(self, event):
		if event.isAutoRepeat:
			return
		print('Stop')


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()