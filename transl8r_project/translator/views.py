# translator/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from googletrans import Translator 

@csrf_exempt
def translate(request):
    if request.method == 'POST':
        source_text = request.POST.get('source_text')
        target_language = request.POST.get('target_language')

        # Perform translation using Googletrans
        translator = Translator()
        translation = translator.translate(source_text, dest=target_language).text

        return JsonResponse({'translation': translation})

    return render(request, 'translate.html')
