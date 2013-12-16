import os, sys, string, re, time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#sys.setdefaultencoding('gbk')
# File utils

def createFile(fName):
	f = os.open(fName, os.O_RDWR | os.O_CREAT)
	os.close(f)

def removeFile(fName):
# make sure it is writable first
	if os.path.exists(fName):
		os.chmod(fName, 0644); 
		os.remove(fName)

def renameFile(oldName, newName):
	if os.path.exists(oldName):
		os.rename(oldName, newName)
	
def writeFile(fName, buf):
	f = open(fName, 'w')
	f.write(buf)
	f.close()
	
def appendFile(fName, buf):
	f = open(fName, 'a')
	f.write(buf)
	f.close()
	
# ===== get leaf name from a file path =====

def getFileLeafName(filePath):

	if (filePath == ""):
		return filePath

	if (os.name == "nt"):
		fileSeparator = "\\"
	elif (os.name == "posix"):
		fileSeparator = "/"

	idx = string.rfind(filePath, fileSeparator)

	# If already a leaf, return it.
	if (idx == -1):
		return filePath

	tokens = string.split(filePath, fileSeparator)
	count = len(tokens)

	leafName = tokens[count-1]
#	print "leafName", leafName

	return leafName

# ===== log msg to a file with a timestamp =====

def logMessage(filePath, msg):
	
	newMsg = time.strftime('%X %x %Z')
	newMsg += ": " 
	newMsg += msg
	print msg
	newMsg += "\n"
	appendFile(filePath, newMsg)


# concatenate a list of strings as one string
# mostly is for stack trace

def combineStrings(msgs):
	msgBuf = ""
	i=0
	while (i < len(msgs)):
		msgBuf += msgs[i]
		i = i + 1
		
	return msgBuf

# parse a file with a list of key=value pairs into a dictionary
# ";" is used as the leading char for comments

def parseFileToDictionary(filepath):
	#print "parseFileToDictionary filepath=" + filepath
	"returns a dictionary of key/value pairs"
	d = {}
	if os.path.exists(filepath) == False:
		return d;

	f = open( filepath );
	for line in f:
		#print "EBUG: " + line
		m = re.search( r'^\s*([^;=][^=]*)=(.*)', line )
		if m:
			key = m.group(1).strip()
			value = m.group(2).strip()
			d[key] = value
	f.close()
	return d
		
def stripFileSuffix(filepath, suffix):

	if filepath.endswith(suffix):
		s = filepath.replace(suffix, "")	
		return s
	else:
		return filepath
