'''
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"	
()	Capture and group

'''



import re

s="cli_42514"

x=re.search("^os_client_.\d+$",s)
y=re.search("^client_.\d+$",s)
z=re.search("^cli_.\d+$",s)

print(x)
print(y)
print(z)
if x or y or z:
  print("yes")
