import pyaudio
import  wave
import numpy as np
import tkFileDialog
from scipy.io.wavfile import read
audio_file_name = ''
audio_file_name2 = ''
Audio1=[]

class open:

    global primero, segundo
    def open_masker(self):
        global audio_file_name


        audio_file_name = tkFileDialog.askopenfilename(filetypes=(("Audio Files", ".wav"),   ("All Files", "*.*")))
        rf = wave.open(audio_file_name, 'rb')
        prof = rf.getsampwidth()
        channels = rf.getnchannels()
        rate = rf.getframerate()
        audioN = pyaudio.PyAudio()
        streamN = audioN.open(format=audioN.get_format_from_width(prof), channels=channels, rate=rate, output=True)
        datos = rf.readframes(1024)


        while datos != '':

                streamN.write(datos)
                datos = rf.readframes(1024)

        print rate,channels

        Audio1 = read(audio_file_name)
        frame=rf.getnframes()


        #Total=np.asarray(Audio1[1])
        wav=[]
        wav.append(Audio1[1])


        print "array",Audio1[1], "FRAMES!!!!", frame
        print "array",wav, "FRAMES!!!!"


        return wav