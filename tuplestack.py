class Stack:

	def __init__(self):
		self.items = ()
		self.length = 0
		self.temp = 0

	# Empty list checker
	def is_empty(self):
		return self.items == ()

	def push(self, x):
		self.items = (x, self.items)
		self.length += 1

	def pop(self):
		if len(self.items) == 0:
			return "Underflow"
		a, b = self.items
		self.items = b
		self.length -= 1
		return a

	# Regular

	def __iter__(self):

		class Stack_iter:

			def __init__(self, items, ind):
				self.items = items
				self.index = ind
				self.current = ()
				self.rest = self.items

			def __next__(self):
				if self.rest == ():
					raise StopIteration

				self.current, self.rest = self.rest
				return self.current

			def __iter__(self):
				return self

		return Stack_iter(self.items, len(self.items))

	# Destructive

	def destructive_iterator(self):

		class dest_iter:	

			def __init__(self, items, ind):
				self.items = items

			def __next__(self):
				if self.items == ():
					raise StopIteration
				x, y= self.items
				self.items = y
				return x

			def __iter__(self):
				return self
 
		after = dest_iter(self.items, self.length)
		self.items = ()
		return after

		# It works, but feels bad.
