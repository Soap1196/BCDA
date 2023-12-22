from django.shortcuts import render, HttpResponse

# Create your views here
def home(request):
    return render(request, "home.html")

def PaymentIntegrityDisplay(request):
    args = {}
    text = "It worked"
    args['mytext'] = text
    return render(request, "PaymentIntegrityDisplay.html", args)