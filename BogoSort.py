import pygame, random, time

pygame.init()

class BogoSort():

	def __init__(self):
		self. attempts = 0
		self.end = False
		self.running = True
		self.width, self.height = 1000, 600
		self.arr = []
		size  = random.randint(7,15)
		for i in range(size):
			self.arr.append(random.randint(1,8))
		self.calcSizes()

		pygame.display.set_caption('BubbleSort')

		self.screen = pygame.display.set_mode((self.width, self.height))

	def run(self):
		if self.end == False:
			self.screen = pygame.display.set_mode((self.width, self.height))
		self.draw()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def calcSizes(self):
		self.xsize = self.width // len(self.arr)
		largest = 0
		for i in range(len(self.arr)):
			if largest < self.arr[i]:
				largest = self.arr[i]
		self.ysize = self.height // largest

	def draw(self):
		self.px = 0
		self.py = 600
		if self.end == False:
			for i in range(len(self.arr)):
				colour = 'white'
				if self.first == i or self.second == i:
					colour = 'red'
				pygame.draw.rect(self.screen,colour,[self.px + i * self.xsize + 1, self.py - self.ysize * self.arr[i], self.xsize - 1, self.ysize * self.arr[i]])
			#time.sleep(0.1)
			pygame.display.update()
		if self.end == True:
			for i in range(len(self.arr)):
				colour = 'green'
				pygame.draw.rect(self.screen,colour,[self.px + i * self.xsize + 1, self.py - self.ysize * self.arr[i], self.xsize - 1, self.ysize * self.arr[i]])			
				pygame.display.update()
				time.sleep(0.1)
			self.end = 'final'
		if self.end == 'final':
			#print(self.attempts)
			pygame.display.update()

	def Bogosort(self):
		flag = True
		self.calcSizes()

		while flag == True and self.running == True:

			self.attempts += 1
			time.sleep(0.08)

			self.first = random.randint(0, len(self.arr) - 1)
			self.second = self.first
			while self.second == self.first:
				self.second = random.randint (0, len(self.arr) - 1)

			temp = self.arr[self.second]
			self.arr[self.second] = self.arr[self.first]
			self.arr[self.first] = temp

			flag = False
			i = 0
			while flag == False and i <= len(self.arr) - 2:
				if self.arr[i] > self.arr[i+1]:
					flag = True
				i += 1
			self.run()

		if self.running == True and flag == False:
			self.end = True
			self.run()
		while self.running == True and self.end == 'final':
			self.run()

		pygame.quit()

	def getName(self):
		return 'Bogo Sort'
go = BogoSort()
go.Bogosort()
