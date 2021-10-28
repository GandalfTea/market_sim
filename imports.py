

#from market import market
import sys

# ANSI colors 
class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


NUM_OF_PARTICIPANTS = 10000
NUM_OF_SECURITIES = 10
#CYCLES_PER_MINUTE = 100
IRRATIONALITY = 0.5     # no clue how to use this yet 
VERBOSE = False
VERBOSE_PARTICIPANTS = False 
VERBOSE_SECURITIES = False 
VERBOSE_MARKET = False 
TIME_ELAPSED = False


if len(sys.argv) >= 2:
    argv = sys.argv[1:]
    for i in argv:
        if i.isdigit(): 
            continue
        if i in ("-v", "-verbose"):
            VERBOSE = True
        elif i == ("-vp"):
            VERBOSE_PARTICIPANTS = True 
        elif i == "-vs":
            VERBOSE_SECURITIES = True 
        elif i == "-vm":
            VERBOSE_MARKET = True 
        elif i == "-t":
            TIME_ELAPSED = True
        elif i in ("-p", "-participants"):
            try:
                NUM_OF_PARTICIPANTS = int(argv[argv.index(i) + 1])
            except ValueError:
                sys.exit("Error: input is not int.")
            except IndexError:
                sys.exit("Error: no input detected")
        elif i in ("-s", "-securities"):
            try:
                NUM_OF_SECURITIES = int(argv[argv.index(i) + 1])
            except ValueError:
                sys.exit("Error: input is not int.")
            except IndexError:
                sys.exit("Error: no input detected")
        elif i in ("--h", "--help"):
            print("\nCommands : " \
                "\n\t-p [int] : \tnumber of participants" \
                "\n\t-s [int] : \tnumber of securities" \
                "\n\t-v, -verbose :  verbose" \
                "\n\t-t  \t :\tprocessing time" \
                "\n\t-vp \t :\tverbose participants" \
                "\n\t-vs \t :\tverbose securities" \
                "\n\t-vm \t :\tverbose market")
            #print(str(can_buy[i][0]) + " " + str(can_buy[i][1][0]))
            sys.exit("")
        else:
            print("DICKS")
            sys.exit("Command not recognized. Type --h or --help for help")


