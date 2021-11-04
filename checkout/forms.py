from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # Create dictionary of placeholders to display in the form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Set autofocus on full_name field to True so cursor starts in
        # full-name field when user loads the page
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Iterate through form fields
        for field in self.fields:
            # Add a star to the placeholder if it's a required field
            # on the model
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # Set all the placeholder attributes to their values in the
            # dictionary above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add CSS class to fields: 'stripe-style-input'
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove form fields labels
            # (not needed as placehoilders are set above)
            self.fields[field].label = False
