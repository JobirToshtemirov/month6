from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from auth_fur.form import RegisterForm
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from auth_fur.token import TokenGenerator
from django.utils.http import urlsafe_base64_encode
from conf.settings import EMAIL_HOST_USER



def home(request):
    if request.method == 'POST':
        form = RegisterForm(request.Post)

    return render(request, 'index.html')  # 'index.html' — это файл в папке templates


def send_email(request, user):
    # Send email to user
    token = TokenGenerator.make_token(user)
    uid = urlsafe_base64_encode(user.pk)
    current = get_current_site(request)
    verification_url = reverse('auth_fur:verify_email', kwargs={'uidb64': uid, 'token': token})
    full_url = f"http://{current.site.domain}{verification_url}"

    text_content = render_to_string(
        'register/verify_email.html',
        {'user': user, 'full_url': full_url},

    )

    message = EmailMultiAlternatives(
        subject="Verify your email address",
        body=text_content,
        to=[user.email],
        from_email=[EMAIL_HOST_USER]
    )

    message.attach_alternative(text_content, 'text/html')
    message.send()


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(row_password=form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            send_email(request, user)
            return redirect(reverse_lazy('auth_fur:login'))
        else:
            errors = form.errors
            return render(request, 'login.html', {"errors": errors})
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')
