from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/load-customer-locations/', views.load_locations, name='api-load-customer-locations'),


    path('jobs/create/', AddJob.as_view(), name='addjob'),
    path('jobs/<pk>/update/', UpdateJob.as_view(), name='updatejob'),

    path('customer/active/', ViewActiveCustomers.as_view(), name='activecustomers'),
    path('customer/create/', AddCustomer.as_view(), name='addcustomer'),
    path('customer/details/<slug:slug>/', CustomerDetails.as_view(), name='customerdetails'),

    # path('customer/external/details/<uuid:external_uuid>/', CustomerExternalDetails.as_view(), name='customerexternaldetails'),
    # path('customer/external/details/<uuid:external_uuid>/print/', CustomerExternalDetailsPrint.as_view(), name='customerexternaldetailsprint')
]
