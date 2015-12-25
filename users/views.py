<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth import *
from django.core.context_processors import csrf
=======
from django.shortcuts import render,render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.template import RequestContext

from django.core.context_processors import csrf
from django.contrib.auth import *

# Create your views here.
def user_login(request):
    '''
    login
    '''
    print('login users')

    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username %s password %s' % (username, password))
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')
    ctx = {}
    ctx.update(csrf(request))
    return render(request, 'login.html', ctx)

def user_logout(request):
    '''
    logout
    URL: /users/logout
    '''

    logout(request)
    return redirect('/')


# Create your views here.
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             return HttpResponseRedirect("/books/")
#     else:
#         form = UserCreationForm()
#     return render_to_response("registration/register.html", {
#         'form': form,
#     })

# <html>
# <body>

# {% block title %}Create an account{% endblock %}

# {% block content %}
#   <h1>Create an account</h1>
# <form action="" method="post">{% csrf_token %}
#   <form action="" method="post">{% csrf_token %}
#       {{ form.as_p }}
#       <input type="submit" value="Create the account">
#   </form>
# {% endblock %}
# </body>
# </html>


# def register(request):
# if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#         new_user = form.save()
#         return HttpResponseRedirect("/books/")
# else:
#     form = UserCreationForm()
# c = {'form': form}
# return render_to_response("registration/register.html", c, context_instance=RequestContext(request) # 

