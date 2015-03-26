class Colors:
	
	
	#we can add more colors here
	def returnRGBVal(self, color):
		if color == 'yellow':
			return "225,225,0"
		elif color == 'red':
			return "225,0,0"
		elif color == 'lime':
			return "0,225,0"
		elif color == 'blue':
			return "0,0,225"
		elif color == 'green':
			return "0,128,0"
		elif color == 'purple':
			return "128,0,128"
		elif color == 'navy':
			return "0,0,128"
		else:
			return 'not a valid color'

		

	#Get colors from http://www.cloford.com/resources/colours/500col.htm
		if color == 'indian red':
			return "176,23,31"
		elif color == 'crimson':
			return "220,20,60"
		elif color == 'lightpink':
			return "255,182,193"
		elif color == 'lightpink 1':
			return "255,174,185"
		elif color == 'lightpink 2':
			return "238,162,173"
		elif color == 'lightpink 3':
			return "205,140,149"
		elif color == 'lightpink 4':
			return "139,95,101"
		else:
			return 'not a valid color'



	
	#process string
	def returnRed(self,RGBVal):
		return int(RGBVal.split(",")[0])
		
	def returnGreen(self,RGBVal):
		return int(RGBVal.split(",")[1])
	
	def returnBlue(self, RGBVal):
		return int(RGBVal.split(",")[2])
		
		