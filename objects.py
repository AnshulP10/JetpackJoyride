from board import Board

class Obj:
	def __init__(self, x, y, bg):
		self.x = x
		self.y = y
		self.user = ["",]
		self.bg = bg

	def insert(self, obj):
		for i in range(len(obj)):
			for j in range(len(obj[i])):
				self.bg.grid[self.y+i][self.x+j] = self.user[i][j]

	def remove(self, obj):
		for i in range(len(obj)):
			for j in range(len(obj[i])):
				self.bg.grid[self.y+i][self.x+j] = ' '

class Mand(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user1 = """__.-._   
'-._"7'  
 /'.-c   
 |  /T   
_)_/LI""".split("\n")
		self.user2 = """__.-._ S 
'-._"7'  S  
 /'.-c   S
 |  /T   S
_)_/LI  S""".split("\n")
		self.insert(self.user2)

	def up(self, flag = 0):
		if self.y < 20:
			return
		self.remove(self.user)
		if flag == 0:
			self.y = self.y - 10
		else:
			self.y = self.y - 3
		self.insert(self.user)

	def left(self, flag = 0):
		if self.x < 7:
			return
		self.remove(self.user)
		if flag == 0:
			self.x = self.x - 3
		else:
			self.x = self.x - 1
		self.insert(self.user)

	def right(self, flag = 0):
		if self.x > 120:
			return
		self.remove(self.user)
		if flag == 0:
			self.x = self.x + 3
		else:
			self.x = self.x + 1
		self.insert(self.user)

	def down(self, flag = 0):
		if self.y > 42:
			return
		self.remove(self.user)
		self.y = self.y + 1
		self.insert(self.user)		

class Coin(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = 'O'
		self.insert(self.user)
	
	def left(self, flag):
		self.remove(self.user)
		if flag == 0:			
			self.x = self.x - 2
		else:
			self.x = self.x - 4
		self.insert(self.user)

class Laser1(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = """|
|
|
|""".split("\n")
		self.insert(self.user)
	
	def left(self, flag):
		self.remove(self.user)
		if flag == 0:
			self.x = self.x - 3
		else:
			self.x = self.x - 5
		self.insert(self.user)

class Laser2(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = """====
====""".split("\n")
		self.insert(self.user)
	
	def left(self, flag):
		self.remove(self.user)
		if flag == 0:
			self.x = self.x - 3
		else:
			self.x = self.x - 5
		self.insert(self.user)

class Laser3(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = """\\
 \\
  \\
   \\""".split("\n")
		self.insert(self.user)
	
	def left(self, flag):
		self.remove(self.user)
		if flag == 0:
			self.x = self.x - 3
		else:
			self.x = self.x - 5
		self.insert(self.user)

class Beam(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = """>>>>""".split("\n")
		self.insert(self.user)
	
	def right(self, flag):
		self.remove(self.user)
		if flag == 0:
			self.x = self.x + 3
		else:
			self.x = self.x + 5
		self.insert(self.user)

class Dragon(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = """                    
         /\\_/\\
     /\\  |6 6|  /\\
    /  \\ \\<">/ /  \\
   / ,__`~)-(~___, \\
  /.',-'`/_/`'-,  '.\\
   ,'    \\_\\    ',
  :       \\|\\     ;
   ',     /|/    ,'
     '-,__\\W\\_,-))
               ((
                )
""".split("\n")
		self.insert(self.user)
	def rem(self):
		return super().remove(self.user)

class Ball(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = """*""".split("\n")
		self.insert(self.user)

	def left(self):
		self.remove(self.user)
		self.x = self.x - 3
		self.insert(self.user)

class Background(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = """                                        |
                                      \\ _ /
                                    -= (_) =-
   .\\/.                               /   \
.\\//o\\                      ,\\/.      |              ,~
//o\\|,\\/.   ,.,.,   ,\\/.  ,\\//o\\                     |\\
  |  |//o\\  /###/#\\  //o\\  /o\\|                      /| \\
^^|^^|^~|^^^|' '|:|^^^|^^^^^|^^|^^^""""""""("~~~~~~~~/_|__\\~~~~~~~~~~
 .|'' . |  '''""'"''. |`===`|''  '"" "" " (" ~~~~ ~ ~======~~  ~~ ~
    ^^   ^^^ ^ ^^^ ^^^^ ^^^ ^^ ^^ "" ""\"( " ~~~~~~ ~~~~~  ~~~ ~""".split("\n")
		self.insert(self.user)

class Speed(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = """SPD""".split("\n")
		self.insert(self.user)

	def left(self):
		self.remove(self.user)
		self.x = self.x - 2
		self.insert(self.user)

class Magnet(Obj):
	def __init__(self, x, y, bg):
		super().__init__(x, y, bg)
		self.user = """MAG""".split("\n")
		self.insert(self.user)
