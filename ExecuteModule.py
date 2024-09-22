import ExecutorConfig as ExCfg
import mySerial as mySerial
from Config import *
def CallExecutable(data:str):
    if not data:
        return 1
    try:
        formatedData = data.split(" ")
        for keyWord in formatedData:
            if ExCfg.keys.get(keyWord)!= None:
                file = open(ExCfg.BasePath + ExCfg.keys.get(keyWord),"r")
                for lines in file:
                    mySerial.SW(ExCfg.ComPort, ExCfg.baudrate,lines)
    except:
        print("Error When execute")
def PlayAutorizedMusic(Music_Name):
    chunk = 1024 
 
    # Open the soaudio/sound file 
    af = wave.open(Music_Name, 'rb')
    
    # Create an interface to PortAudio 
    pa = pyaudio.PyAudio()
    
    # Open a .Stream object to write the WAV file
    # 'output = True' indicates that the 
    # sound will be played rather than
    # recorded and opposite can be used for recording
    stream = pa.open(format = pa.get_format_from_width(af.getsampwidth()),
                    channels = af.getnchannels(),
                    rate = af.getframerate(),
                    output = True)
    
    # Read data in chunks
    rd_data = af.readframes(chunk)
    
    # Play the sound by writing the audio
    # data to the Stream using while loop
    while rd_data != '':
        stream.write(rd_data)
        rd_data = af.readframes(chunk)
    
    # Close and terminate the stream
    stream.stop_stream()
    stream.close()
