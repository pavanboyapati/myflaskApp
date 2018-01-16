 # import itertools

# list = [1,2,3]

# result = itertools.permutations(list, 2)
# for r in result:
# 	print (r)

class Person:
	def __init__(self, name,age,salary):
		# super(Person, self).__init__()
		self.name = name
		self.age = age
		self.salary = salary

p1 = Person('James',23,70000)

l = ['james',23,80000]


sentence = 'My name is {0[0]} and I am {0[1]} old with salary ${0[2]:,.2f}'.format(l)
print(sentence)



