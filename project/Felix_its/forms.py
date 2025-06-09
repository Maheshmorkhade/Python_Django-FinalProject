from django import forms
from .models import Felixclass

class FelixForm(forms.ModelForm):
    class Meta:
        model = Felixclass
        fields = ['name', 'image', 'type']

    def __init__(self, *args, **kwargs):
        super(FelixForm, self).__init__(*args, **kwargs)

        # Add empty choice for placeholder in select
        self.fields['type'].choices = [('', 'Select Course Type')] + list(self.fields['type'].choices)

        self.fields['name'].widget.attrs.update({
            'class': 'w-full px-4 py-2 text-black placeholder-black border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter course name'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'w-full px-4 py-2 text-black placeholder-black border border-gray-300 rounded bg-white focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Upload course image'
        })

        self.fields['type'].widget.attrs.update({
            'class': 'w-full px-4 py-2 text-black border border-gray-300 rounded bg-white focus:outline-none focus:ring-2 focus:ring-blue-500',
        })




