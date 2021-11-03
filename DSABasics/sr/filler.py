def evalFiller(inputfile):
    text_file = open(inputfile, 'r')
    text = text_file.read()
    
    #cleaning
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]
    
    #finding unique
    fillerWordCount=0;
    fillerReport = {}
    fillerwords =['like','so','okay','ok','basically','you know', 'i mean', 'right','actually']
    
    '''for fileWord in words:
        for fillerwd in fillerwords:
            if fillerwd == fileWord:
                fillerWordCount = fillerWordCount +1'''   
    
    for fileWord in words:
        for filler in fillerwords:
            if filler == fileWord:
                value = filler
                fillerWordCount = fillerWordCount +1
                if value in fillerReport:
                    fillerReport[value] += 1
                else:
                    fillerReport[value] = 1
          
    print("Filler Word :", fillerWordCount)
    print("Filler Report :", fillerReport)