from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView

from app.forms import CreateCustomerForm, CreateJobForm
from app.models import Customer, Job, CustomerLocation
from proj import settings
from django_weasyprint import WeasyTemplateResponseMixin, WeasyTemplateResponse


class HomeView(TemplateView):
    template_name = 'app/home.html'


class CustomerHome(TemplateView):
    template_name = 'app/customer/customerhome.html'


class JobsHome(TemplateView):
    template_name = 'app/job/jobshome.html'


def load_locations(request):
    customer_id = request.GET.get('locations')
    locations = CustomerLocation.objects.filter(customer_id=customer_id).order_by('address')
    return render(request, 'app/job/locationdropdown.html', {'locations': locations})


class AddCustomer(CreateView):
    model = Customer
    form_class = CreateCustomerForm
    template_name = 'app/customer/newcustomer.html'

    def get_success_url(self):
        return reverse('customerdetails', args=(self.object.slug,))


class CustomerDetails(DetailView):
    model = Customer
    template_name = 'app/customer/customer_detail.html'


class CustomerExternalDetails(DetailView):
    model = Customer
    template_name = 'app/customer/customer_external_detail.html'

    def get_object(self, queryset=None):
        return Customer.objects.get(external_uuid=self.kwargs.get('external_uuid'))


class ViewActiveCustomers(ListView):
    model = Customer
    template_name = 'app/customer/activecustomers.html'
    queryset = Customer.objects.filter(active=True)
    paginate_by = 10


class AddJob(CreateView):
    model = Job
    form_class = CreateJobForm
    template_name = 'app/job/createjob.html'

    def get_success_url(self):
        return reverse('customerdetails', args=(self.object.customer.slug,))


class UpdateJob(UpdateView):
    model = Job
    fields = [
        'active',
        'status',
        'customer',
        'customer_location',
        'scope_of_work',
        'request_from',
        'PO_number',
        'SC_work_order',
        'notes',
    ]
    template_name = 'app/job/editjob.html'

    def get_success_url(self):
        return reverse('customerdetails', args=(self.object.customer.slug,))


class CustomerExternalDetailsPrint(DetailView):
    model = Customer
    template_name = 'app/customer/customer_external_detail_print.html'

    def get_object(self, queryset=None):
        return Customer.objects.get(external_uuid=self.kwargs.get('external_uuid'))


class CustomerExternalDetailsPrintPDF(WeasyTemplateResponseMixin, CustomerExternalDetailsPrint):
    response_class = WeasyTemplateResponse
    pdf_attachment = False
    pdf_filename = 'printout.pdf'
    pdf_stylesheets = [
        str(settings.STATIC_ROOT) + '\\app\\bootstrap.css',
    ]
