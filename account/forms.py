from django.contrib.auth.forms import UserCreationForm

from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email', 'name', "gender", "phone_number" , "country", 'password1', 'password2'
        ]