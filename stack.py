class Stack:

	def __init__(self):
		self.items = []
		self.length = 0
		self.temp = 0

	# Empty list checker
	def is_empty(self):
		return self.items == []

	def push(self, x):
		self.items.insert(0, x)
		self.length += 1

	def pop(self):
		self.length -= 1
		return self.items.pop()

	# Regular Iteration

	def __iter__(self):

		class Stack_iter:

			def __init__(self, items, ind):
				self.items = items
				self.index = ind
				self.tmp = 0

			def __next__(self):
				Cur = self.tmp
				if self.tmp == self.index:
					raise StopIteration
				self.tmp = self.tmp + 1
				return self.items[Cur]

			def __iter__(self):
				return self

		return Stack_iter(self.items, self.length)

	# Destructive

	def destructive_iterator(self):

		class dest_iter:	

			def pop(self):
				return self.items.pop()		

			def __init__(self, items, index):
				self.items = items
				self.index = index
				self.tmp = 0
			
			def __next__(self):
				if self.tmp == self.index:
					raise StopIteration
				self.tmp = self.tmp + 1
				return self.pop()

			def __iter__(self):
				return self

		After = dest_iter(self.items, self.length)
		self.length = len(self.items)
		return After





