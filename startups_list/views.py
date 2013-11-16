from django.shortcuts import render

def index(request):
  context = { 'nothing': 'nothing' }
  return render(request, 'startups/index.html', context)
