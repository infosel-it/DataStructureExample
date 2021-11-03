def evalWordFrequency(inputfile, audioTime):
    text_file = open(inputfile, 'r')
    text = text_file.read()
    #cleaning
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]
    
    wordCount = len(words)
    frequency = wordCount / audioTime
          
    print("wordCount Count :", wordCount)
    print("Frequency :", frequency)