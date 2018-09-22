""" Description """  

___title___  = "hackme2"
___license___ = "MIT"
___dependencies___ = ["sleep", "app", "ugfx_helper", "buttons", "homescreen" ]
___categories___ = ["Homescreens"]

import wifi, ugfx, http, os, time, sleep, ugfx_helper, math

ugfx.init()
ugfx.clear()

from tilda import Buttons
from homescreen import *

width = 240
height = 320
ugfx_helper.init()

s = ugfx.Style()
s.set_background(ugfx.WHITE)
s.set_enabled([ugfx.BLACK, ugfx.html_color(0x800080), ugfx.html_color(0x800080), ugfx.html_color(0x800080)])
ugfx.set_default_style(s)

def draw_name():
    intro_text = "Hi! I'm"
    intro_height = 30
    name_height = 60
    max_name = 8

    ugfx.orientation(90)
    ugfx.set_default_font(ugfx.FONT_TITLE)
    # Process name
    name_setting = name("Set your name in the settings app")
    if len(name_setting) <= max_name:
        ugfx.set_default_font(ugfx.FONT_NAME)
    else:
        ugfx.set_default_font(ugfx.FONT_MEDIUM_BOLD)
    
    ugfx.Label(0, ugfx.height() - name_height - intro_height, ugfx.width(), intro_height, intro_text, justification=ugfx.Label.CENTER)
    ugfx.Label(0, ugfx.height() - name_height, ugfx.width(), name_height, name_setting, justification=ugfx.Label.CENTER)

ugfx.orientation(270)

def go():
    ugfx.clear(ugfx.WHITE)
draw_name() # yjis displays names ei print 

image = ("hackme2/LHS.png")

ugfx.display_image(35, 15,image)


