from django.test import TestCase
from django.core.urlresolvers import reverse, resolve, get_resolver
from django.test.client import Client

import startups_list

# >>> from django.core.urlresolvers import get_resolver
# >>> resolver = get_resolver(None)
# >>> resolver.resolve('/some/path/')
# ResolverMatch(func=...)

class TestUrlsRoot(TestCase):
  def setUp(self):
    self.resolver = get_resolver(None)

  def test_startups(self):
    b = self.resolver.resolve('/startups/')
    self.assertEqual( b.url_name, 'index' )

  def test_root(self):
    a = self.resolver.resolve('/')
    self.assertEqual(a.url_name, 'django.views.generic.base.RedirectView')
    # print '+++ +++'
    # print a

  def test_sanity(self):
    a = self.resolver.resolve('/startups/sanity')
    # print '+++ +++'
    self.assertEqual( a.url_name, 'sanity' )

class TestViews(TestCase):
  def setUp(self):
    self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')

  def test_index(self):
    response = self.client.get('/startups/')
    self.assertEqual( 0, len(response.context['startups']))
