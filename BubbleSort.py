import pygame, random, time

pygame.init()

class BubbleSort():

	def __init__(self):
		self.end = False
		self.running = True
		self.width, self.height = 1000, 600
		self.arr = []
		size  = random.randint(100,100)
		for i in range(size):
			self.arr.append(random.randint(1,151))
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
		self.xsize = self.width / len(self.arr)
		largest = 0
		for i in range(len(self.arr)):
			if largest < self.arr[i]:
				largest = self.arr[i]
		self.ysize = self.height / largest

	def draw(self):
		self.px = 0
		self.py = 600
		if self.end == False:
			for i in range(len(self.arr)):
				colour = 'white'
				if i == self.i:
					colour = 'red'
				pygame.draw.rect(self.screen,colour,[self.px + i * self.xsize + 1, self.py - self.ysize * self.arr[i], self.xsize - 1, self.ysize * self.arr[i]])
			pygame.display.update()
		if self.end == True:
			for i in range(len(self.arr)):
				colour = 'green'
				pygame.draw.rect(self.screen,colour,[self.px + i * self.xsize + 1, self.py - self.ysize * self.arr[i], self.xsize - 1, self.ysize * self.arr[i]])			
				pygame.display.update()
				time.sleep(0.02)
			self.end = 'final'
		if self.end == 'final':
			pygame.display.update()

	def Bubblesort(self):
		flag = True
		self.var = 0
		self.calcSizes()
		while flag == True and self.running == True:
			flag = False
			for self.i in range(len(self.arr) - 1 - self.var):
				if self.arr[self.i] > self.arr[self.i+1]:
					temp = self.arr[self.i]
					self.arr[self.i] = self.arr[self.i+1]
					self.arr[self.i+1] = temp
					flag = True

				self.run()
			self.var += 1
		self.i = 0
		self.run()
		if self.running == True and flag == False:
			self.run()
			self.end = True
			self.run()
		while self.running == True and self.end == 'final':
			self.run()
		pygame.quit()

	def getName(self):
		return 'Bubble Sort'
go = BubbleSort()
go.Bubblesort()
