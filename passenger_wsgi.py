#def application(environ, start_response):
#  start_response('200 OK', [('Content-Type', 'text/plain')])
#  return [b"hello world!\n"]

import sys, os
# from startups import settings

sys.path.append("/home/piousbox/projects/startups") # I used the actual path in my file
os.environ['DJANGO_SETTINGS_MODULE'] = 'startups.settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# def application(environ, start_response):
#   write = start_response('200 OK', [('Content-type', 'text/plain')])
#   return ["Hello, world!"]
