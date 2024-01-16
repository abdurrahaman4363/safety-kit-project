
from django import forms
from .models import Vaccine,DoseBooking,Review,STAR_CHOICES
from accounts.models import UserAccount

class VaccineForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Vaccine
        fields = ['name', 'description', 'date', 'age', 'dose_number','user_account','campaign']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user_account'].queryset = UserAccount.objects.filter(role='Doctor')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-white '
                    'text-black border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })


class DoseBookingForm(forms.ModelForm):
    class Meta:
        model = DoseBooking
        fields = ['first_dose', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-white '
                    'text-black border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })

class CampaignReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=STAR_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "shadow appearance-none border border-gray-500 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            }
        ),
    )

    class Meta:
        model = Review
        fields = ["comment", "rating"]