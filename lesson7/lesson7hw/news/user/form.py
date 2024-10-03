
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

