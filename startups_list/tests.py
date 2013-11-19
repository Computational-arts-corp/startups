from django.test import TestCase
from django.core.urlresolvers import reverse, resolve, get_resolver
from django.test.client import Client

import startups_list
from startups_list.models import Startup

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

  def test_sanity(self):
    a = self.resolver.resolve('/startups/sanity')
    self.assertEqual( a.url_name, 'sanity' )

class TestViews(TestCase):
  def setUp(self):
    self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')

  def test_index(self):
    response = self.client.get('/startups/')
    self.assertEqual( 0, len(response.context['startups']))

class TestStartupModel(TestCase):
  def setUp(self):
    Startup.objects.create( name='Startup Name', website_url='http://example.com', is_dead=False, has_vacancy=True, has_applied=False )

  def tearDown(self):
    b = 'b'

  def test_list_pursuitable(self):
    result = Startup.list_pursuitable()
    expected = Startup.objects.all()
    # print '+++ +++'
    # print expected
    # print result

    self.assertEqual( expected[0].name, result[0].name )
