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
				self.tmp = 0
				self.current = ()
				self.rest = self.items

			def __next__(self):
				if self.tmp == self.index:
					raise StopIteration
				self.current, self.rest = self.rest
				self.tmp = self.tmp + 1
				return self.current
				
				return self.items[Cur]

			def __iter__(self):
				return self

		return Stack_iter(self.items, len(self.items))

	# Destructive

	def destructive_iterator(self):

		class dest_iter:	

			def __init__(self, items, ind):
				self.items = items
				self.index = ind
				self.tmp = 0

			def __next__(self):
				if self.tmp == self.index:
					raise StopIteration

				self.tmp = self.tmp + 1
				x, y= self.items
				self.items = y
				return x

			def __iter__(self):
				return self
 
		after = dest_iter(self.items, self.length)
		self.items = ()
		self.length = 0
		return after

s = Stack()
s.push(1)
s.push(2)
for x in s:
    for y in s:
        print(x, y)
for x in s.destructive_iterator():
    print(x)

print(s.pop())
print(s.pop())


		# It works, but feels bad.
