from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Comment

# Formulario de registro
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
        return user


# Formulario de login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))  # Captura el username
    password = forms.CharField(widget=forms.PasswordInput)  # Captura la password

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )

# Formulario para comentarios
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
