def getDest(destString):
	return {
		'' : "000",
		'M' : "001",
		'D' : "010",
		"MD" : "011",
		"A" : "100",
		"AM" : "101",
		"AD" : "110",
		"AMD" : "111" 
	}[destString]

def getJump(jumpString):
	return {
		'' : "000",
		'JGT' : "001",
		'JEQ' : "010",
		"JGE" : "011",
		"JLT" : "100",
		"JNE" : "101",
		"JLE" : "110",
		"JMP" : "111" 
	}[jumpString]

def getComp(compString):
	return {
		'0' : "0101010",
		'1' : "0111111",
		'-1' : "0111010",
		"D" : "0001100",
		"A" : "0110000",
		"!D" : "0001101",
		"!A" : "0110001",
		"-D" : "0001111",
		"-A" : "0110011",
		"D+1" : "0011111",
		"A+1" : "0110111",
		"D-1" : "0001110",
		"A-1" : "0110010",
		"D+A" : "0000010",
		"D-A" : "0010011",
		"A-D" : "0000111",
		"D&A" : "0000000",
		"D|A" : "0010101",
		"M" : "1110000",
		"!M" : "1110001",
		"M+1" : "1110111",
		"M-1" : "1110010",
		"D+M" : "1000010",
		"D-M" : "1010011",
		"M-D" : "1000111",
		"D&M" : "1000000",
		"D|M" : "1010101"
	}[compString]

symbolsDic = {
	'R0' : "0",
	'R1' : "1",
	'R2' : "2",
	"R3" : "3",
	"R4" : "4",
	"R5" : "5",
	"R6" : "6",
	"R7" : "7",
	"R8" : "8",
	'R9' : "9",
	'R10' : "10",
	'R11' : "11",
	"R12" : "12",
	"R13" : "13",
	"R14" : "14",
	"R15" : "15",
	"SCREEN" : "16384",
	"KBD" : "24576",
	"SP" : "0",
	"LCL" : "1",
	"ARG" : "2",
	"THIS" : "3",
	"THAT" : "4"
}

def getPredefinedSymbol(symbol):
	return symbolsDic[symbol]
	
fileName = input("File to translate: ") 
file1 = open(fileName, "r")
file = open(fileName, "r")
newFile = open(fileName[:-4] + ".hack", "w")
#First iteration to store pseudo commands
lineNum = 0
variableCounter = 16
for newLine in file1:
	line = newLine.strip()
	if (line[0:1] == ""):
		continue
	if (line[0:2] == "//"):
		continue
	if (line[0] == "("):
		pseudoCommand = line[1:-1]
		symbolsDic[pseudoCommand] = str(lineNum)
		continue
	lineNum = lineNum + 1
for newLine in file:
	line = newLine.strip()
	#Ignore whitespace and comments
	if (line[0:1] == ""):
		continue
	if (line[0:2] == "//"):
		continue
	if (line[0] == "("):
		continue
	#Handle A commands
	line = line.split(" ")[0]
	if (line[0] == "@"):
		binaryNum = ""
		try:
			intValue = int(line[1:])
			binaryNum = bin(intValue)[2:]
		except ValueError:
			#If this is a known symbol
			if (line[1:] in symbolsDic):
				binaryNum = bin(int(getPredefinedSymbol(line[1:])))[2:]
			#otherwises it is a variable we need to declare
			else:
				symbolsDic[line[1:]] = variableCounter
				variableCounter = variableCounter + 1
				binaryNum = bin(int(getPredefinedSymbol(line[1:])))[2:]
		newFile.write(binaryNum.zfill(16) + "\n")
		continue
	#Handle C commands
	cDest, cRamining = "", ""
	if "=" in line:
		cDest, cRemaining = line.split("=")
	else:
		cDest = ""
		cRemaining = line
	
	cComp, cJump = "", ""
	if ";" in cRemaining:
		cComp, cJump = cRemaining.split(";")
	else:
		cComp = cRemaining
		cJump = ""

	cCommand = "111" + getComp(cComp) + getDest(cDest) + getJump(cJump)
	newFile.write(cCommand + "\n")

