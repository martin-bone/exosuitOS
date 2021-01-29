#exosuitOS main.py

#To do:
#move Commands to separate file
#add more commands
#investigate bug mentioned in notes

#Notes:
#First loop of main behaves erratically, most of the time it doesn't work or slow
#however subsequent loops work fine, sometimes the first one does too
#problem only appears in Visual Studio Python Interactive
#python.exe works fine, only 3.7


def FMain():
	'''Main loop'''

	#Every new command needs to be added here
	DCommands = {
				'stop' : lambda : CStop(),
				'shut down' : lambda : CShutDown(),
				'restart' : lambda : CRestart(),
				'confirm' : lambda : CConfirm()
				}

	while True:
		VCommand = input('Command to be executed:')
		if VCommand == 'quit':
			break
		DCommands.get(VCommand, lambda : print('This command does not exist'))()




def FVoiceRecognition():
	import speech_recognition as sr

	vr = sr.Recognizer()
	vmic = sr.Microphone()

	with vmic as source:
		print('Listening:')
		vaudio = vr.listen(source)

	vdata = ''
	try:
		vdata = vr.recognize_google(vaudio)
		print(vdata)
	except sr.UnknownValueError:
		print("Not recognizable!")
	except sr.RequestError:
		print('Request Error!')
	return vdata


class CCommand():
	'''Parent class for all commands
		Every new command has to be added to DCommands in FMain'''

	def __init__(self, VCommand):
		'''VCommand is the command to be excecuted'''
		self.VCommand = VCommand
		self.VErrorCode = FExecute()
		
	
	def FExecute(self):
		'''Executes the command
			return value 0 is OK'''
		print('Default FExecute')
		return 0


##############################################################
#Essential system commands

class CStop(CCommand):
	'''Pauses everything'''

	def __init__(self):
		'''VCommand is the command to be excecuted'''
		self.VCommand = 'Stop'
		self.VErrorCode = self.FExecute()


	def FExecute(self):
		'''Executes the command
			return value 0 is OK'''
		print(self.VCommand)
		return 0


class CShutDown(CCommand):
	'''Shuts down the system'''

	def __init__(self):
		'''VCommand is the command to be excecuted'''
		self.VCommand = 'Shut down'
		self.VErrorCode = self.FExecute()


	def FExecute(self):
		'''Executes the command
			return value 0 is OK'''
		print(self.VCommand)
		return 0


class CRestart(CCommand):
	'''Restarts the system'''

	def __init__(self):
		'''VCommand is the command to be excecuted'''
		self.VCommand = 'Restart'
		self.VErrorCode = self.FExecute()


	def FExecute(self):
		'''Executes the command
			return value 0 is OK'''
		print(self.VCommand)
		return 0

#This command cannot be issued on its own, only if other commands require it
class CConfirm(CCommand):
	'''Confirmation after another command'''

	def __init__(self):
		'''VCommand is the command to be excecuted'''
		self.VCommand = 'Confirm'
		self.VErrorCode = self.FExecute()


	def FExecute(self):
		'''Executes the command
			return value depends on whether confirmation is given'''
		print(self.VCommand)
		return False

##############################################################
#Smartphone control

##############################################################
#Equipment control

##############################################################
#Camera control

##############################################################
#Media control


FMain()
