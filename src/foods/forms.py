from django import forms
from .models import Food


class FoodAddForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Voeg hier een title toe"
        }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Voeg hier een beschrijving toe"
        }))
    price = forms.DecimalField()

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00:
            raise forms.ValidationError("Prijs moet groter zijn dan 1")
        elif price >= 99.99:
            raise forms.ValidationError("Prijs moet klein zijn dan 100")
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 3:
            return title
        else:
            raise forms.ValidationError("Title moet minimaal 3 karakters bevatten")


class FoodModelForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            "title",
            "description",
            "price",
        ]
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Voeg hier een beschrijving toe"
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Voeg hier een title toe"
                }
            )
        }

        def clean_price(self):
            price = self.cleaned_data.get("price")
            if price <= 1.00:
                raise forms.ValidationError("Prijs moet groter zijn dan 1")
            elif price >= 100.00:
                raise forms.ValidationError("Prijs moet klein zijn dan 100")
            else:
                return price

        def clean_title(self):
            title = self.cleaned_data.get("title")
            if len(title) > 3:
                return title
            else:
                raise forms.ValidationError("Title moet minimaal 3 karakters bevatten")
