from django.http import HttpResponse
from datetime import datetime
from .signal import mysignal
def myview(request):
    print("Sending signal at:", datetime.now())
    mysignal.send(sender=None)
    print("Signal sent at:", datetime.now())
    return HttpResponse("Signal has been sent.")
