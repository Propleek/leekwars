class bcolors:
	HEADER = '\033[95m'		# purple
	OKBLUE = '\033[94m'		# blue
	OKGREEN = '\033[92m'	# green
	WARNING = '\033[93m' 	# yellow
	FAIL = '\033[91m'		# red
	ENDC = '\033[0m'		# end char
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class g:
	# keep those IDS as is, I use this implicitly in id detection & behavior
	_FARMER_= 0
	_LEEK_1_= 1
	_LEEK_2_= 2
	_LEEK_3_= 3
	_LEEK_4_= 4
	_DELAY_ = 2 # seconds between each check when waiting for fight result
	_WINNERSWITCH_ = {
		0: bcolors.WARNING+"DRAW"+bcolors.ENDC,
		1: bcolors.OKGREEN+"WIN "+bcolors.ENDC,
		2: bcolors.FAIL+"LOSE"+bcolors.ENDC,
	}

class shutdown:
	ON = 2
	ASK= 1
	OFF= 0
