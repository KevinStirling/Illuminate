class Colors:
	
	
	#we can add more colors here
	def returnRGBVal(self, color):
		if color == 'yellow':
			return "225,225,0"
		elif color == 'black':
			return "0,0,0"
		elif color == 'white':
			return "255,255,255"
		elif color == 'black':
			return "0,0,0"
		elif color == 'cyan':
			return "0,255,255"
		elif color == 'magenta':
			return "255,0,255"
		elif color == 'silver':
			return "192,192,192"
		elif color == 'gray':
			return "128,128,128"
		elif color == 'maroon':
			return "128,0,0"
		elif color == 'olive':
			return "128,128,0"
		elif color == 'red':
			return "225,0,0"
		elif color == 'lime':
			return "0,225,0"
		elif color == 'blue':
			return "0,0,225"
		elif color == 'green':
			return "0,128,0"
		elif color == 'brown':
			return "139,69,19"
		elif color == 'purple':
			return "128,0,128"
		elif color == 'teal':
			return "0,128,128"
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
		
		
