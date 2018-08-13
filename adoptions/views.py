from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})
    #return HttpResponse('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>The HTML5 Herald</title><meta name="description" content="The HTML5 Herald"><meta name="author" content="SitePoint"><link rel="stylesheet" href="css/styles.css?v=1.0"></head><body><p>This is the home page</p><script src="js/scripts.js"></script></body></html>')
    
def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet Not Found')
    return render(request, 'pet_detail.html', {'pet': pet})
    
    #return HttpResponse('<p>pet_detail view with the id {}</p>'.format(id))