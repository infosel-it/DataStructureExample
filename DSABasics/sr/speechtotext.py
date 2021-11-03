import speech_recognition as sr 
import moviepy.editor as mp

def speechToText(audioFile, txtFile):

    r = sr.Recognizer()
    audio = sr.AudioFile(audioFile)
    
    with audio as source:
        audio_file = r.record(source)
        result = r.recognize_google(audio_file)
    
    # exporting the result 
    with open(txtFile,mode ='w') as file: 
        #file.write("Recognized Speech:") 
        #file.write("\n") 
        file.write(result) 
        print("Speech to Text Conversion Completed Successfully!")