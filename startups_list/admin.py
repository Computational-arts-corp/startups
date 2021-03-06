
from django.contrib import admin

from startups_list.models import Startup, MediaOutlet, Recruiter
from cities_users.models import Addressbookitem, CityBlock, Day, City

class StartupAdmin(admin.ModelAdmin):
  fieldsets = [
    ( None, { 'fields': [ 'name', 'website_url', 'descr', 'city', 'is_dead' ] } ),
    ( 'Status', { 'fields': [ 'has_vacancy', 'has_applied', 'applied_on' ] } ),
  ]

  list_display = ( 'name', 'website_url', 'city', 'is_dead', 'has_vacancy', 'has_applied', 'is_pursuitable' )

class AddressbookitemAdmin( admin.ModelAdmin):
#  fieldsets = [
#    ( None, { 'fields': [ 'name' ] } ),
#  ]
  list_display = ( 'name', 'city_block', 'city' )

class DayAdmin(admin.ModelAdmin):
  list_display = ( 'date', 'a1', 'a2', 'a3', 'a4', 'a5', 'work', 'dream' )

class CityBlockAdmin( admin.ModelAdmin ):
  list_display = ( 'name', 'date' )

class CityAdmin( admin.ModelAdmin ):
  list_display = [ 'name' ]

class RecruiterAdmin( admin.ModelAdmin ):
  list_display = ( 'name', 'website_url', 'has_applied' )

admin.site.register( Startup, StartupAdmin )
admin.site.register( MediaOutlet )
admin.site.register( Recruiter, RecruiterAdmin )
admin.site.register( CityBlock, CityBlockAdmin )
admin.site.register( City, CityAdmin )
admin.site.register( Addressbookitem, AddressbookitemAdmin )
admin.site.register( Day, DayAdmin )
