from Tkinter import *
import pyaudio
import  wave
import  math
import tkFileDialog
from scipy.io.wavfile import read
import struct
from Compresion import Compresion
from openfile import open
ventana = Tk()
ventana.title('Compressor')
ventana.geometry("550x250")
imageL=PhotoImage(file="compresor.gif")
lblImagen=Label(ventana,image=imageL).place(x=0,y=1)
import matplotlib.pyplot as plt
audio_file_name = ''
audio_file_name2 = ''
Audio1=[]

def main():
    global primero, segundo
    def open_masker():
        global audio_file_name
        onda= open()
        wav=onda.open_masker()
        print "nuevo",wav
        return wav

    def archivo():
        #global Audio
        global wav, peaklevel, valorthresh,dBFs

        #Audio=open_masker()
        wav=[]

        audio_file_name = tkFileDialog.askopenfilename(filetypes=(("Audio Files", ".wav"),   ("All Files", "*.*")))
        Audio1 = read(audio_file_name)
        wav.append(Audio1[1])
        wav.append(Audio1[1])
        print "array",wav[1]
        print "audio_file_name",audio_file_name


        Archivo = wave.open(audio_file_name ,'rb')
        tamano = Archivo.getnframes()
        sumatoria=0

        for i in range(0, tamano):

             DatosArray = Archivo.readframes(1)
             Datos = struct.unpack('<h',DatosArray)
             sumatoria = sumatoria + int(Datos[0])**2
             ValorRms = math.sqrt(sumatoria / tamano)

        ValorpicoRms = 20 * math.log(ValorRms/(2**16))
        peaklevel = max(abs(wav[1]))
        attack=float(int(sliderattack.get()))/1000
        aframes = float(attack*44100)
        print 'attack',attack
        print 'attack en frames',aframes

        print 'Valor Rms=',ValorRms
        print 'Valor pico Rms=',ValorpicoRms
        print 'Pico maximo=',peaklevel
        dBFS= 20 * math.log(float(peaklevel)/(2**16))
        print 'dB del audio original=',dBFS

        # threshold
        level=int(sliderthresh.get())
        valueLevel = (10**float(level/20))*((2**16)/2.0)


    def comprimir():
        global Ratio

        Ratio=int(sliderratio.get())

        print 'Ratio',Ratio
        n=[]
        #Hace el cambio de los dB del threshold a lineal
        level=int(sliderthresh.get()) #valor obtenido del slider
        threshold = (10**float(level/20))*((2**16)/2.0)
        attack=float(int(sliderattack.get()))/1000
        if attack<5:
            attack=0
        aframes = int(attack*44100)
        print 'attack',attack
        print 'attack en frames',aframes
        print 'Threshold lineal',threshold

        #N.1
        w=0
        for j in range(1,aframes):
            l=(float(Ratio-1)/aframes)
            m=(1+float(l*j))
            n.append(m)

        a=Compresion(wav[1],threshold,n,Ratio,aframes)
        b=a.compre()
        plt.plot(b, color="blue", linewidth=1.0, linestyle="-")
        plt.savefig('Comp1.png')
        #Image.open('Tipo1.png').save('Tipo1.jpg','JPEG')
        #plt.show()

        c=a.tipo2()
        plt.plot(c, color="green", linewidth=1.0, linestyle="-")
        plt.savefig('Comp2.png')
        #Image.open('Tipo2.png').save('Tipo2.jpg','JPEG')
        #plt.show()


    cuadrothresh= Label(ventana, fg="black", padx=15, pady=10, text="Threshold")
    cuadrothresh.pack(side=LEFT)
    sliderthresh=Scale(ventana,from_=0,to=-50)
    sliderthresh.pack(side=LEFT)
    cuadrothresh= Label(ventana, fg="black", padx=15, pady=10, text="Ratio")
    cuadrothresh.pack(side=LEFT)
    sliderratio=Scale(ventana,from_=5,to=2)
    sliderratio.pack(side=LEFT)
    cuadroattack= Label(ventana, fg="black", padx=15, pady=10, text="Attack")
    cuadroattack.pack(side=LEFT)
    sliderattack=Scale(ventana,from_=10,to=0)
    sliderattack.pack(side=LEFT)
    cuadrorel= Label(ventana, fg="black", padx=15, pady=10, text="Release")
    cuadrorel.pack(side=LEFT)
    sliderrel=Scale(ventana,from_=10,to=0)
    sliderrel.pack(side=LEFT)
    #sliderknee=Scale(ventana,from_=10,to=0)



    b1 = Button(ventana,text="AUDIO",command = archivo ,font=("Arial Black", 14),width=14).place(x=200,y=20)
    b4 = Button(ventana,text="COMPRIMIR",command = comprimir, font=("Arial Black", 14),width=20).place(x=175,y=200)





    ventana.mainloop()

if __name__=="__main__":
    main()