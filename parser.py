import sys
from optparse import OptionParser

http_proxy = "http://127.0.0.1:4440"
https_proxy = "https://127.0.0.1:4440"
proxyDict = {"http": http_proxy, "https": https_proxy}
proxyDict=None

#usage
# python file_name.py -a 152
# or
# python file_name.py --agencyId 152

def parse_args(args):
    agency_id = None
    parser = OptionParser()
    parser.add_option("-a","--agencyId",dest="agency_id")
    (options, args)  = parser.parse_args()

    agency_id = options.agency_id
    print(agency_id)
    return


parse_args(sys.argv[1:])


