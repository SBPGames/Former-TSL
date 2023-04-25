import sys, getopt
from sevenlives import *

mode = Mode.PRODUCTION

try:
    options, args = getopt.getopt(sys.argv[1:], "d", ["mode="])

    for o, v in options:
        if o == "--mode":
            for m in Mode.getValues():
                if v in m.getNames():
                    mode = m
                    break
            else:
                raise getopt.GetoptError(f"Unknown \"{v}\" as a {o} value.", o)
        elif o == "-d":
            mode = Mode.DEVELOPMENT
except getopt.GetoptError as e:
    if e.opt == "--mode": print(e)

print(f"Launching game in {str(mode.getId()).capitalize()} mode...")

TheSevenLives(mode).run()