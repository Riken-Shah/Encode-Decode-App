from django.shortcuts import render
from . import Logic

def home(request):
    return render(request, 'index.html')

def encode(request):
    try:
        encodei = request.POST["encodei"]
        app = Logic.Main()
        encode_text = app.to_encode(str(encodei))
    except:
        encode_text = ''

    return render(request, 'answer.html',{'encode_or_decode': 'Encoded text', 'answer': encode_text})


def whats_it(request):
    return render(request, 'what_is_it.html')

def decode(request):
    try:
        encodei = request.POST["decode"]
        app = Logic.Main()
        encode_text = app.to_decode(str(encodei))
    except:
        encode_text = ''

    return render(request, 'answer.html', {'answer': encode_text, 'encode_or_decode': 'Decoded text'})

