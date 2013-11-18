
from django.contrib import admin

from startups_list.models import Startup, MediaOutlet, Recruiter
from cities_users.models import Addressbookitem, CityBlock, Day

class StartupAdmin(admin.ModelAdmin):
  fieldsets = [
    ( None, { 'fields': [ 'name', 'website_url', 'descr', 'city_name', 'is_dead' ] } ),
    ( 'Status', { 'fields': [ 'has_vacancy', 'has_applied', 'applied_on' ] } ),
  ]

  list_display = ( 'name', 'website_url', 'is_dead', 'has_vacancy', 'has_applied', 'is_pursuitable' )

class AddressbookitemAdmin( admin.ModelAdmin):
#  fieldsets = [
#    ( None, { 'fields': [ 'name' ] } ),
#  ]
  list_display = ( 'name', 'city_block' )

class DayAdmin(admin.ModelAdmin):
  list_display = ( 'date', 'a1', 'a2', 'a3', 'a4', 'a5', 'work', 'dream' )

class CityBlockAdmin( admin.ModelAdmin ):
  list_display = ( 'name', 'date' )

admin.site.register( Startup, StartupAdmin )
admin.site.register( MediaOutlet )
admin.site.register( Recruiter )
admin.site.register( CityBlock, CityBlockAdmin )
admin.site.register( Addressbookitem, AddressbookitemAdmin )
admin.site.register( Day, DayAdmin )
