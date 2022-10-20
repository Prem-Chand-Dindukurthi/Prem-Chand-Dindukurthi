import sys
import getopt
import logging

    

def main(argv):
    inputFileType=''
    inputFilePath=''

    try:
        opts, args = getopt.getopt(argv, "t:p:",["type=","path="])
    except getopt.GetoptError as e:
        logging.error(e)
        sys.exit(1)
    for opt, arg in opts:
        if opt in ["-t","--type"]:
            inputFileType=arg
        elif opt in ["-p","--path"]:
            inputFilePath=arg

    inputFile=

    return

main(sys.argv[1:])
