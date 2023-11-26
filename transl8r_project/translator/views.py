from django.shortcuts import render, redirect
from .models import Translation
from googletrans import Translator

def translate_text(request):
    if request.method == 'POST':
        original_text = request.POST['original_text']
        translator = Translator()
        translated_text = translator.translate(original_text).text
        Translation.objects.create(original_text=original_text, translated_text=translated_text)
        return render(request, 'translator/translate.html', {'original_text': original_text, 'translated_text': translated_text})
    return render(request, 'translator/translate.html')

def home(request):
    return render(request, 'home.html')
