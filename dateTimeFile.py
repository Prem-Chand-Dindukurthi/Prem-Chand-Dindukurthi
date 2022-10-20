import datetime

date_time_str = '2022-08-25 09:32:09'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')


print(date_time_obj)



print(date_time_obj.isoformat())

print(type(date_time_obj.isoformat()))



print(datetime.datetime.utcnow())


print(datetime.datetime.now().isoformat())


k=datetime.datetime.now()

print(k)

epoch = date_time_obj.timestamp()
print("epoch:",epoch)






import datetime

present_date = datetime.datetime.utcnow()
print(present_date)
# 2021-08-24 13:05:42.736781

creation_date = '2021-07-22 05:17:36'
creation_date = datetime.datetime.strptime(creation_date, '%Y-%m-%d %H:%M:%S')
print(creation_date)
# 2021-07-22 05:17:36

difference = present_date - creation_date
print(difference)
# 33 days, 7:48:06.736781

print(type(difference))
# <type 'datetime.timedelta'>

print(difference.total_seconds())
# 2879286.73678






'''
import datetime
datetime.datetime.now().isoformat()
k=datetime.datetime.now()
k

k.isoformat()

print(datetime.datetime.utcnow())

import datetime

date_time_str = '2018-06-29 08:15:27'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

date_time_obj

date_time_obj.isoformat()

type(date_time_obj.isoformat())
'''
















