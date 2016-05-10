from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .models import Airports

def airpot_list(request):
    airports = Airports.objects.all()
    paginator = Paginator(airports,200)
    page = request.GET.get('page')

    try:
        airports = paginator.page(page)
    except PageNotAnInteger:
        airports = paginator.page(1)
    except EmptyPage:
        airports = paginator.page(page.num_pages)

    return render(request,'myPort/layout.html',{'airports':airports})




