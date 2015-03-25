class Colors:
	
	#we can add more colors here
	def returnRGBVal(self, color):
#		if color == 'yellow':
#			return "225,225,0"
#		elif color == 'red':
#			return "225,0,0"
#		elif color == 'lime':
#			return "0,225,0"
#		elif color == 'blue':
#			return "0,0,225"
#		elif color == 'green':
#			return "0,128,0"
#		elif color == 'purple':
#			return "128,0,128"
#		elif color == 'navy':
#			return "0,0,128"
#		else:
#			return 'test'


	switch(color)
	{
  		case'yellow': {return "225,225,0";}
  		case'red': {return "225,0,0";}
		case'lime': {return "0,225,0";}
  		case'blue': {return "0,0,225";}
		case'green': {return "0,128,0";}
  		case'purple': {return "128,0,128";}
		case'navy': {return "0,0,128";}
  		default: {return 'test';}
	}

	
	#process string
	def returnRed(self,RGBVal):
		return int(RGBVal.split(",")[0])
		
	def returnGreen(self,RGBVal):
		return int(RGBVal.split(",")[1])
	
	def returnBlue(self, RGBVal):
		return int(RGBVal.split(",")[2])
		
		