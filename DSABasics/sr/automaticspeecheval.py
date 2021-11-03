from speechtotext import *
from crutches import *
from filler import *
from repeationofwords import *
from wordfrequency import * 

audioFile = "selva.wav"
txtFileName = 'recognized.txt'

#speechToText(audioFile,txtFileName)
evalCrutches(txtFileName)
evalFiller(txtFileName)
evalSingleRepetationWords(txtFileName)
evalWordFrequency(txtFileName,1.5)