#text_file = open('data.txt', 'r')

def evalCrutches(inputfile):
    text_file = open(inputfile, 'r')
    text = text_file.read()
    
    #cleaning
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]
    
    #finding unique
    ahcount = 0
    hmmcount = 0
    ercount = 0
    for word in words:
        if word == "ah":
            ahcount = ahcount +1
        elif word == "hmm": 
            hmmcount = hmmcount +1
        elif word == "er":
            ercount = ercount+1
    
    fileName = "ahcount.txt"
    fileCrutchesSound = open(fileName, 'w')
    
    ahCountStr = "Ah Count :" + str(ahcount) 
    newLine ="\n"
    hmmCountStr = "Hmm Count :" + str(hmmcount)
    erCount = "Er Count :" + str(ercount)
    
    fileCrutchesSound.write(ahCountStr)
    fileCrutchesSound.write(newLine)
    fileCrutchesSound.write(hmmCountStr)
    fileCrutchesSound.write(newLine)
    fileCrutchesSound.write(erCount)
    fileCrutchesSound.write(newLine)