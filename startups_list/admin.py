
from django.contrib import admin

from startups_list.models import Startup, MediaOutlet, Recruiter

class StartupAdmin(admin.ModelAdmin):
  fieldsets = [
    ( None, { 'fields': [ 'name', 'website_url', 'descr', 'city_name' ] } ),
    ( 'Status', { 'fields': [ 'has_vacancy', 'has_applied', 'applied_on' ] } ),
  ]

  list_display = ( 'name', 'website_url', 'has_vacancy', 'has_applied' )

admin.site.register( Startup, StartupAdmin )
admin.site.register( MediaOutlet )
admin.site.register( Recruiter )


