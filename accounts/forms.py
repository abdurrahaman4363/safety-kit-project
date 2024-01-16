from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount
from django.contrib.auth.forms import PasswordChangeForm

class UserAccountCreationForm(UserCreationForm):
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    role = forms.ChoiceField(choices=UserAccount.ROLE_CHOICES)
    gender = forms.ChoiceField(choices=UserAccount.GENDER_CHOICES, required=False)
    street_address = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    postal_code = forms.CharField(max_length=20, required=False)
    country = forms.CharField(max_length=100, required=False)
    nid = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields =['username','first_name','last_name','password1','password2','email','nid', 'birth_date', 'role', 'gender', 'street_address', 'city', 'postal_code', 'country']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            UserAccount.objects.create(
            user=user,
            nid=self.cleaned_data['nid'],
            birth_date=self.cleaned_data['birth_date'],
            role=self.cleaned_data['role'],
            gender=self.cleaned_data['gender'],
            street_address=self.cleaned_data['street_address'],
            city=self.cleaned_data['city'],
            postal_code=self.cleaned_data['postal_code'],
            country=self.cleaned_data['country']
        )
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-white '
                    'text-black border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })




class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=UserAccount.GENDER_CHOICES, required=False)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    role = forms.ChoiceField(choices=UserAccount.ROLE_CHOICES)
    nid = forms.CharField(max_length=20)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

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
        if self.instance:
            try:
                user_account = self.instance.account
            except UserAccount.DoesNotExist:
                user_account = None

            if user_account:
                self.fields['gender'].initial = user_account.gender
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['street_address'].initial = user_account.street_address
                self.fields['city'].initial = user_account.city
                self.fields['postal_code'].initial = user_account.postal_code
                self.fields['country'].initial = user_account.country

                self.fields['role'].initial = user_account.role
                self.fields['nid'].initial = user_account.nid

    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = UserAccount.objects.get_or_create(user=user)
            user_account.gender = self.cleaned_data['gender']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.street_address = self.cleaned_data['street_address']
            user_account.city = self.cleaned_data['city']
            user_account.postal_code = self.cleaned_data['postal_code']
            user_account.country = self.cleaned_data['country']

            user_account.role = self.cleaned_data['role']
            user_account.nid = self.cleaned_data['nid']
            user_account.save()

        return user
    


class StyledPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": (
                        "appearance-none block w-full bg-white "
                        "text-black border border-gray-200 rounded "
                        "py-3 px-4 leading-tight focus:outline-none "
                        "focus:bg-white focus:border-gray-500"
                    )
                }
            )
            