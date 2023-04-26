class Parent():

	def last_name(self):
		print('Gunjal')


class Child(Parent):

	def first_name(self):
		print('Tanu')

	def last_name(self):
		print('ahgastgwergf')


Me = Child()

Me.first_name()
Me.last_name()


class Mario():

	def move(self):
		print("I'm moving")


class Shroom():

	def collect(self):
		print('collected mashroom')


class BigMario(Mario, Shroom):
	print("I'm big now")


bm = BigMario()

bm.move()

bm.collect()