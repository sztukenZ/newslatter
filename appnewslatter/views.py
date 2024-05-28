from django.shortcuts import render
from django.contrib import messages
from .models import NewsLatterEmail


# Create your views here.
def home(request):
    if "subscribe" in request.POST:
        email = NewsLatterEmail()
        email.userEmail = request.POST.get("email")
        email.save()
        messages.info(request, "You have successfully subscribed to our newsletter")
    if "unsubscribe" in request.POST:
        NewsLatterEmail.objects.get(userEmail=request.POST.get("email")).delete()
        messages.info(request, "Sorry to see you")
    return render(request, "news.html")
