import time #for time
from datetime import datetime #for date
from .signal import mysignal #this will import the signal file 

def signalhandle(sender, **kwargs):
    print("Signal received at:", datetime.now())
    time.sleep(2)
    print("Handler finished at:", datetime.now())
mysignal.connect(signalhandle)
