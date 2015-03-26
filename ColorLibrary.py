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

	
	#process string
	def returnRed(self,RGBVal):
		return int(RGBVal.split(",")[0])
		
	def returnGreen(self,RGBVal):
		return int(RGBVal.split(",")[1])
	
	def returnBlue(self, RGBVal):
		return int(RGBVal.split(",")[2])
		
		