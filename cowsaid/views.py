from django.shortcuts import render, reverse
from cowsaid.forms import InputForm
from cowsaid.forms import Quote
import subprocess
# Create your views here.
def index(request):
    html = "index.html"

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cowsaid = __ask_cow__(data["text"])
            form = InputForm()
            return render(request, html, {'form':form, 'cow':cowsaid, 'history':reverse("history")})
    form = InputForm()
    return render(request, html, {'form': form, 'history':reverse("history")})

def __ask_cow__(text):
    Quote.objects.create(text=text)
    if Quote.objects.count() > 10:
        Quote.objects.first().delete()
    ask = subprocess.run(['cowsay', text], stdout=subprocess.PIPE)
    return ask.stdout.decode('utf-8')

def history(request):
    html = "history.html"
    quotes = Quote.objects.all()
    cow_quotes = []
    for quote in quotes:
        ask = subprocess.run(['cowsay', quote.text], stdout=subprocess.PIPE)
        cow_quotes.append(ask.stdout.decode('utf-8'))
    cow_quotes.reverse()
    return render(request, html, {'homepage':reverse('homepage'), "cow_quotes":cow_quotes})