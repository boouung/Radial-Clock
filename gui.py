#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys
import time
import logging
import spidev as SPI
from PIL import Image,ImageDraw,ImageFont
import RPi.GPIO as GPIO
import LCD_2inch

class Wavescreen:
	def __init__(self, bg):
		#RST = 27
		#DC = 25
		#BL = 18
		#bus = 0
		#device = 0
		#disp = LCD_2inch.LCD_2inch(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
		#disp = LCD_2inch.LCD_2inch() 
		
		if GPIO.getmode() != GPIO.BCM:
			GPIO.setmode(GPIO.BCM)
		logging.basicConfig(level=logging.DEBUG) # debugging
		try:
			# display with hardware SPI: Warning!!!Don't  creation of multiple displayer objects!!!
			self.disp = LCD_2inch.LCD_2inch()
			self.disp.Init()
			self.disp.clear()
			
			self.image = Image.new("RGB", (self.disp.height, self.disp.width), bg)
			self.Font1 = ImageFont.truetype(os.getcwd() + "/Font/Font01.ttf",25)
			self.Font2 = ImageFont.truetype(os.getcwd() + "/Font/Font01.ttf",35)
			self.Font3 = ImageFont.truetype(os.getcwd() + "/Font/Font02.ttf",64)
			
			self.disp.bl_DutyCycle(15) # set backlight x/25
			
		except IOError as e:
			logging.info(e)
	
	def show(self, bg, x, y, text, color, style, r):
		try:
			draw = ImageDraw.Draw(self.image)
			draw.rectangle([(0, 0), (self.disp.height, self.disp.width)], bg)
			if text is not None:
				draw.text((x, y), text, fill = color,font=style)
			image = self.image.rotate(r)
			self.disp.ShowImage(image)
		except IOError as e:
			logging.info(e)
			
			
	def fin(self):
		GPIO.cleanup()
		self.disp.clear()
		self.disp.module_exit()
		logging.info("quit:")
		exit()
