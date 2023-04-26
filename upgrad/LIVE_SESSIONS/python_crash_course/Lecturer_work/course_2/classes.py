class Enemy:

	# life = 10

	def __init__(self, y):
		self.life = y

	def damage(self, x):
		print('ouch!')
		self.life -= x

	def checkLife(self):
		if self.life <= 0:
			print('I am dead')
		else:
			print('Available life: ', self.life)


soldier = Enemy(10)
soldier2 = Enemy(10)

boss = Enemy(100)

# soldier.life = 15

soldier.damage(2)
soldier2.damage(5)
boss.damage(12)


soldier.checkLife()
soldier2.checkLife()
boss.checkLife()