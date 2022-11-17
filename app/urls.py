from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', HomeViews.HomeView.as_view(), name='home'),
    path('api/load-customer-locations/', views.load_locations, name='api-load-customer-locations'),

    path('jobs/', HomeViews.JobsHome.as_view(), name='jobshome'),
    path('jobs/create/', Jobs.AddJob.as_view(), name='addjob'),
    path('jobs/<pk>/update/', Jobs.UpdateJob.as_view(), name='updatejob'),
    path('jobs/search/', search_jobs, name='searchjob'),

    path('customer/', HomeViews.CustomerHome.as_view(), name='customerhome'),
    path('customer/active/', Customers.ViewActiveCustomers.as_view(), name='activecustomers'),
    path('customer/create/', Customers.AddCustomer.as_view(), name='addcustomer'),
    path('customer/details/<slug:slug>/', Customers.CustomerDetails.as_view(), name='customerdetails'),
    path('customer/external/details/<uuid:external_uuid>/', Customers.CustomerExternalDetails.as_view(),
         name='customerexternaldetails'),
    path('customer/external/details/<uuid:external_uuid>/print/', Customers.CustomerExternalDetailsPrintPDF.as_view(),
         name='customerexternaldetailsprint')

]
