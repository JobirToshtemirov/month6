from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.



app_name= 'user'

def register_view(request,):
    if request.method == 'POST'
        form = UserForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.set_password(raw_password = form.cleaned_data['password'])
            user.save()

            return redirect('user:login')
        else:
            errors =




def login_view(request):
    return HttpResponse("Login")


def logout_view(request):
    return HttpResponse("Logout")