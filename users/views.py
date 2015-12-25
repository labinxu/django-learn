from django.shortcuts import render
from django.contrib.auth import *
from django.core.context_processors import csrf
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
    
def login(request):
    print('user_login')
    user_login(request)
