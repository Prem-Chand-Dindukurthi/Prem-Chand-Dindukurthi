
import sys
import os


file_path = '/home/appster/freshKills/deleted_users.tsv'

if os.path.isfile(file_path):
    print('File exists')
else:
    print('File does not exists')
    sys.exit(0)


if os.stat(file_path).st_size == 0:
    print('File is empty')
    sys.exit(0)


