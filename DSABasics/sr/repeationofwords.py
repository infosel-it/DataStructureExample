# Naive Pattern Searching algorithm
def NaviePatternSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
        
        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            print("Pattern found at index ", i)
            return True

def evalSingleRepetationWords(inputfile):
    text_file = open(inputfile, 'r')
    text = text_file.read()
    #cleaning
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]
    
    repeatWordCount=0;
    repeatWordReport = {}
    
    for fileWord in words:
        retVal = NaviePatternSearch(fileWord,text)
        if(retVal):
                value = fileWord
                repeatWordCount = repeatWordCount +1
                if value in repeatWordReport:
                    repeatWordReport[value] += 1
                else:
                    repeatWordReport[value] = 1
          
    print("Repeat Word :", repeatWordCount)
    print("Repeat Report :", repeatWordReport)