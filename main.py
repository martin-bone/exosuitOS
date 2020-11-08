#exosuitOS main.py
import sys

#To do:
#move CCommand and to separate file
#add more commands
#

#Notes:
#

def FMain():
	'''Main loop'''
	v=CStop()



def FVoiceRecognition():
	'''Recognizes commands'''
	pass



class CCommand():
	'''Parent class for all command'''

	def __init__(self, VCommand):
		'''VCommand is the command to be excecuted
			return value 0 is OK'''
		self.VCommand = VCommand
		VErrorCode = FExecute()
		return VErrorCode
	
	def FExecute(self):
		'''Executes the command
			return value 0 is OK'''
		print('Default FExecute')
		return 0



class CStop(CCommand):
	'''Pauses everything'''

	def __init__(self):
		'''VCommand is the command to be excecuted
			return value 0 is OK'''
		self.VCommand = 'Stop'
		VErrorCode = self.FExecute()
		return VErrorCode

	def FExecute(self):
		'''Executes the command
			return value 0 is OK'''
		print(self.VCommand)
		return 0



FMain()
