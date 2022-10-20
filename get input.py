import sys
import getopt
import logging
from osUtils.file_utils import FileUtils
import time

def usage():
    print("python geoLocationIdVerication.py --type url --path https://docs.google.com/spreadsheets/d/e/2PACX-1vSRlq7Gqx3_p2E6MVB0Mwhh0EKTAt=csv (or)\n"+
          "python geoLocationIdVerication.py --type file --path local_file_path\n"+
          )


def parse_sheet_data(inputType, path):
    local_file_path = None

    if inputType.lower() == "url":
        local_file_path = FileUtils.download_file(
            url = path,
            prefix="backfill_geo_targeting_data" + str(int(time.time())),
            suffix=".tsv"
        )
    elif inputType.lower() == "file":
        local_file_path = path
    else:
        raise Exception("Invalid input_type provided.")

    if local_file_path:

        return local_file_path

    else:
        raise Exception("Couldn't download file from url.")


def main(argv):
    try:
        opts , args= getopt.getopt(argv,"t:p:",["type=","path="])
    except getopt.GetoptError as e:
        logging.error(e)
        usage()
        sys.exit(1)

    for opt , arg in opts:
        if opt in ["-t","--type"]:
            inputFileType=arg
        elif opt in ["-p","--path"]:
            inputFilePath=arg
        else:
            usage()
            sys.exit(1)

    inputFile = parse_sheet_data(inputFileType, inputFilePath)
    logging.debug("Input File Path" + inputFile)






    return

main(sys.argv[1:])
