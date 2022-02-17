import os


def convertList(path):
	if not ".txt" in path:
		return
	if ".adguard" in path or ".pihole" in path:
		return
	with open(path, "r", encoding="utf-8") as f:
		adguardOut, piholeOut = "", ""
		for line in f.readlines():
			forbiddenSubstrings = ["<", "! ", "  ", "!--"]
			if any(x in line for x in forbiddenSubstrings):
				continue
			commentSubstrings = ["# ", " #"]
			if any(x in line for x in commentSubstrings):
				line = line.split("#")[0].replace(" ", "") + "\n"
				if line == "\n":
					continue
			if line == "\n":
				continue
			line = line.replace("0.0.0.0 ", "").replace("127.0.0.1 ", "")
			adguardOut += line
			if not "!+ " in line:
				piholeOut += line
	with open(path.replace(".txt", ".adguard.txt"), "w",
	          encoding="utf-8") as f:
		f.write(adguardOut)
	with open(path.replace(".txt", ".pihole.txt"), "w", encoding="utf-8") as f:
		f.write(piholeOut)


for category in os.listdir():
	if category == ".git" or category == ".github" in category:
		continue
	try:
		for list in os.listdir(category):
			convertList(category + "/" + list)
	except NotADirectoryError:
		convertList(category)