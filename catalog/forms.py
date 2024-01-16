from django import forms

from catalog.models import Product, Category, Version

LIST_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


# class StyleFormMixin:
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in LIST_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с названием продукта')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in LIST_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с описанием продукта')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('__all__')
     