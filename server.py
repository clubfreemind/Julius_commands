import tornado.ioloop
import tornado.web
import tornado.template
from lxml import etree

tree = etree.parse("config.xml")

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		loader = tornado.template.Loader(".")
		self.write(loader.load("index.html").generate())
class onLoad(tornado.web.RequestHandler):
	def get(self):
		a = open("config.xml","r")
		self.write(a.read())
		a.close()

class SpeechRecognition(tornado.web.RequestHandler):
	def get(self):
		value = self.get_argument("value",True)
		if value == "on":
			value = "on"
		else:
			value = "off"
		#print value
		for element in tree.iter():
			if element.tag == "status":
				element.text = value
		a = open("config.xml","w")
		a.write(etree.tostring(tree))
		#print etree.tostring(tree)
		a.close()
class SystemControl(tornado.web.RequestHandler):
	def get(self):
		value = self.get_argument("value",True)
		if value == "on":
			value = "on"
		else:
			value = "off"
		#print value
		for element in tree.iter():
			if element.tag == "systemControl":
				element.text = value
		a = open("config.xml","w")
		a.write(etree.tostring(tree))
		#print etree.tostring(tree)
		a.close()
class InternetControl(tornado.web.RequestHandler):
	def get(self):
		value = self.get_argument("value",True)
		if value == "on":
			value = "on"
		else:
			value = "off"
		#print value
		for element in tree.iter():
			if element.tag == "internetControl":
				element.text = value
		a = open("config.xml","w")
		a.write(etree.tostring(tree))
		#print etree.tostring(tree)
		a.close()
class IntelSystemLock(tornado.web.RequestHandler):
	def get(self):
		value = self.get_argument("value",True)
		if value == "on":
			value = "on"
			for element in tree.iter():
				if element.tag == "IntelSystemLock":
					element.text = value
			a = open("config.xml","w")
			a.write(etree.tostring(tree))
			#print etree.tostring(tree)
			a.close()
		else:
			value = "off"
			for element in tree.iter():
				if element.tag == "IntelSystemLock":
					element.text = value
			a = open("config.xml","w")
			a.write(etree.tostring(tree))
			#print etree.tostring(tree)
			a.close()
			

application = tornado.web.Application([(r"/", MainHandler),
										(r"/speechRecognition", SpeechRecognition),
										(r"/internetControl", InternetControl),
										(r"/systemControl", SystemControl),
										(r"/IntelSystemLock", IntelSystemLock),
										(r"/onLoad", onLoad),
										(r"/web/(.*)", tornado.web.StaticFileHandler, {"path":"web"}),
										])
if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

