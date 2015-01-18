class top(Exception):
#all self-defined exception should inherit from the exception superclass
	pass

class middle(top):
	pass

class bottom(middle):
	pass


for instance in [top, middle, bottom]:
	try:
		raise instance()

	except bottom:
		print("bottom exception caught!")

	except middle:
		print("middle exception caught!")

	except top:
		print("top exception caught!")