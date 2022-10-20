#example 1
import requests
def func():
  i=requests.get("https://en.wikipedia.org/wiki/Premchand")
  return i is not None
k=func()
print(k)

#example 2
def func():
  i=0
  return i is not None
k=func()
print(k)

#example 3
def func():
  i=1
  return i is not None
k=func()
print(k)



#example 4
def func():
  i=None
  return i is not None
k=func()
print(k)






