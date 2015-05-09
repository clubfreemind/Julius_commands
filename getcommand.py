#!/usr/bin/python
import sys
import api
from lxml import etree
from api import Data


def command(speech_object):
	while(True):
		tree = etree.parse("config.xml")
		for element in tree.iter():
			if element.tag == "status":
				xmlspeech = element.text
			elif element.tag == "systemControl":
				xmlsystem = element.text
			elif element.tag == "internetControl":
				xmlinternet = element.text
		line = speech_object.readline()
		if(line.startswith("sentence1: ")):
			com = line[15:-6]
			print com
			if xmlspeech == "on":

				if xmlinternet == "on":
					if(com == "OPEN FOX"):
						userin = Data(["firefox"],"Opening firefox")
						userin.interact()

				if xmlsystem == "on":
					if(com == "LOCK COMPUTER"):
						userin = Data(["gnome-screensaver-command","-l"],"Computer Locked",True)
						userin.interact()
					if(com == "OPEN COMMAND CENTER"):
						userin = Data(["gnome-terminal"],"Starting Terminal")
						userin.interact()

			if(com == "RESPOND"):
				currentstate = "Listening"
				if xmlspeech == "off":
					currentstate = "Not listening"
				userin = Data("",currentstate,True)
				userin.interact()
			if(com == "STOP LISTENING"):
				userin = Data("","Paused listening", True)
				userin.interact()
				xmlspeech = "off"
			if(com == "RESUME LISTENING"):
				userin = Data("","Started listening", True)
				userin.interact()
				xmlspeech = "on"

if __name__ == '__main__':
	try:
		command(sys.stdin)
	except KeyboardInterrupt:
		sys.exit(1)
