# Design Patterns in Django

## Class-Based Views (CBV)

### Problem
The original `signupAccount` view used a function-based view (FBV). While FBVs are simple and intuitive, they can become difficult to manage and extend as the application grows. In contrast, **Class-Based Views (CBV)** allow for better reuse of code, by dividing the logic into methods (e.g., `get`, `post`).

### Solution
We refactored the `signupAccount` view into a class-based view called `SignUpView`. This new view inherits from Django's `View` class and separates the logic for handling GET and POST requests.

#### Refactored Code:
```python
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from .models import CustomUser

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            user = CustomUser()
            user.save_user(user_data)
            login(request, user)
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})
