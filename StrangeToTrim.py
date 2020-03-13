import re

index = 0
lines = avsp.GetSelectedText()
match = re.findall(r'\b\d+[^\D]', lines)

while index < len(match):
	list  = match[index:index+2]
	list  = ",".join(list)
	if index == len(match)-2:
		avsp.InsertText("Trim("+str(list)+")")
	else:
		avsp.InsertText("Trim("+str(list)+") ++ ")
	index += 2
	
	
	