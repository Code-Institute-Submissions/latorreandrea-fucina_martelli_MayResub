from django import forms


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ('user',)
        fields = (
            'full_name', 'email_address', 'phone_number', 'town_or_city',
            'street_address1', 'street_address2',
            'country', 'county', 'postcode')
    
    def __int__(self, *args, **kwargs):
        '''add placeholders, '''
        super(). __int__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name', 
            'email_address': 'email@email.example', 
            'phone_number': 'Phone Number', 
            'town_or_city': 'City', 
            'street_address1': 'main Street Adress', 
            'street_address2': 'secondary Street Adress',
            'country': 'Country', 
            'county': 'County/Region',
            'postcode': 'Postal Code',
        }