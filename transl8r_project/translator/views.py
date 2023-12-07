#from django.shortcuts import render, redirect
#from .models import Translation
#from googletrans import Translator

#def translate_text(request):
    #if request.method == 'POST':
        #original_text = request.POST['original_text']
       # translator = Translator()
        #translated_text = translator.translate(original_text).text
       # Translation.objects.create(original_text=original_text, translated_text=translated_text)
        #return render(request, 'translator/translate.html', {'original_text': original_text, 'translated_text': translated_text})
    #return render(request, 'translator/translate.html')

#def home(request):
   # return render(request, 'home.html')

from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse
# all the views are here
def home(request):
    if request.method == 'POST':
        contact = Contact()
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        country = request.POST.get('country')
        subject = request.POST.get('subject')
        contact.first_name = first_name
        contact.last_name = last_name
        contact.email = email
        contact.country = country
        contact.subject = subject
        contact.save()
        return HttpResponse("<h1>Babel Fish has received your message . Thank you for contacting me .</h1>")
    return render(request, 'home.html')