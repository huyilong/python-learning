class Reverse:
	"""Iterator for looping over a sequence backwards."""
	def _init_(self, data):
		self.data = data
		self.index = len(data) 
		#actually here the index should be 1 less than len(data)
		def _iter_(self):
			return self
			def _next_(self):
				if self.index == 0:
					raise StopIteration
					self.index = self.index - 1
					return self.data[self.index]

					if _name_ == "_main_":
						import sys
						exe = Reverse(sys.argv[1])
						iter(exe)
