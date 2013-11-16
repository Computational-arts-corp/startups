
from django.contrib import admin

from startups_list.models import Startup, MediaOutlet, Recruiter
from cities_users.models import Addressbookitem, CityBlock

class StartupAdmin(admin.ModelAdmin):
  fieldsets = [
    ( None, { 'fields': [ 'name', 'website_url', 'descr', 'city_name', 'is_dead' ] } ),
    ( 'Status', { 'fields': [ 'has_vacancy', 'has_applied', 'applied_on' ] } ),
  ]

  list_display = ( 'name', 'website_url', 'has_vacancy', 'has_applied' )

class AddressbookitemAdmin( admin.ModelAdmin):
#  fieldsets = [
#    ( None, { 'fields': [ 'name' ] } ),
#  ]
  list_display = ( 'name', 'city_block' )

class CityBlockAdmin( admin.ModelAdmin ):
  list_display = ( 'name', 'date' )

admin.site.register( Startup, StartupAdmin )
admin.site.register( MediaOutlet )
admin.site.register( Recruiter )
admin.site.register( CityBlock, CityBlockAdmin )
admin.site.register( Addressbookitem, AddressbookitemAdmin )

