from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'contact.html')


def coming_soon(request):
    return render(request, 'coming_soon.html')



