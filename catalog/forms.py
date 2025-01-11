from django.forms import ModelForm
from django.core.exceptions import ValidationError
from catalog.models import Product
from config.settings import forbidden_words


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter',)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название продукта'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Характеристика продукта'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите цену'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control'})

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in forbidden_words:
            if word in name or word in description:
                self.add_error('name', 'В названии и описании не должны присутсвтовать слова из списка запрещенных слов')