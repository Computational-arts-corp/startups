from django.shortcuts import render

def index(request):
  context = { 'nothing': 'nothing' }
  return render(request, 'startups/index.html', context)

def sanity(request):
  context = {}
  return render(request, 'startups/sanity.html', context)

