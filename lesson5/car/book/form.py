from django import forms


class BookForm(forms.Form):
    name = forms.CharField(max_length=64, required=True)
    author = forms.CharField(max_length=64)
    count = forms.CharField(max_length=5, required=True)
    price = forms.DecimalField(max_digits=7, decimal_places=2,  required=True)

    created_at = forms.DateTimeField(auto_now_add=True)
    updated_at = forms.DateTimeField(auto_now=True)
