#classe iterface do handler

class Handler:
	def __init__(self) -> None:
		self.__next = None
	
	def setNextHandler(self, next):
		if self.__next == None:
			self.__next = next
		else:
			self.__next.setNextHandler(next)
	
	def handle(self) -> bool:
		pass

	def handleNext(self, text: str) -> bool:
		if self.__next == None:
			return True
		return self.__next.handle(text)

