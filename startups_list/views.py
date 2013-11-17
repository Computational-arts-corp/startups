
from django.shortcuts import render

from startups_list.models import Startup

def index(request):
  startups = Startup.objects.order_by( 'name' )
  context = { 'nothing': 'nothing', 'startups': startups }
  return render(request, 'startups/index.html', context)

def sanity(request):
  context = {}
  return render(request, 'startups/sanity.html', context)

