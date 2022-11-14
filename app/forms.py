from django import forms

from app.models import Customer, Job, CustomerLocation


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'acquired_date']
        widgets = {
            'acquired_date': DateInput(),
        }


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['created', 'updated', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_location'].queryset = CustomerLocation.objects.none()

        if 'customer' in self.fields:
            try:
                customer_id = int(self.data.get('customer'))
                self.fields['customer_location'].queryset = CustomerLocation.objects.filter(customer_id=customer_id).order_by('address')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Loc queryset
        elif self.instance.pk:
            self.fields['customer_location'].queryset = self.instance.customer.customerlocation_set_set.order_by('address')
