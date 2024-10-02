from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, Passenger, Driver
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=20)
    homeAddress = forms.CharField(max_length=200)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'homeAddress')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.homeAddress = self.cleaned_data['homeAddress']
        if commit:
            user.save()
            '''# Create related Driver instance
            driver = Driver.objects.create(customuser_ptr=user, rate=0, driverLicense='')

            # Create related Passenger instance
            passenger = Passenger.objects.create(customuser_ptr=user, location='')'''

        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )
