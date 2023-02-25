from django.shortcuts import render

import gtts
from playsound import playsound

def hello(request):
    if request.method=='POST':
        words=request.POST['words']
        print(words)
        tts=gtts.gTTS(words)
        tts.save("hello.mp3")
        playsound("hello.mp3")
    return render (request,'voiceapp/index.html')