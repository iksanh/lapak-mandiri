from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import LoginForm

# Create your views here.

def custom_login(request):
  if request.user.is_authenticated:
    return redirect('/')
  
  next_url = request.GET.get('next', '/')
  
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']

      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)

        if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
          return redirect(next_url)
        return redirect('/')
      
      else:
        form.add_error(None, 'User dan Password Salah') 

  return render(request, 'auth/login.html', {'form': form, 'next': next_url})

def logout_view(request):
  logout(request)
  
  return redirect('login')

