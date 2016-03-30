from System import *
from System.Collections.Concurrent import *
from System.Collections.Generic import *
from System.Collections import *
from System.Threading import *

class Consumer(object):
	Runnable = property()

	def __init__(self, sharedQueue):
		self._i = 0
		self._sharedQueue = sharedQueue

	def run(self):
		while True:
			try:
				personne = self._sharedQueue.take()
				Console.WriteLine("Consumed: " + personne)
				ProducerConsumerPattern.writeToFile(personne)
				self._i += 1
