from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'ProjectTracker Admin'
admin.site.site_title = 'ProjectTracker admin'
admin.site.index_title = 'ProjectTracker Administration'
admin.site.site_title = 'ProjectTracker Administration'
admin.site.site_header = 'ProjectTracker Admin Login'


urlpatterns = [
    path('admin/docs/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
