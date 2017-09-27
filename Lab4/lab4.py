import re

f= open("mbox-short.txt")
for each in f:
	line = each.rstrip()
	#results = re.findall("From .+\s.+\s.+\s ([0-9:].+)", line)
	results = re.findall("From (\S+)@", line)
	print(results)
	


