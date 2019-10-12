from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if pass1 == pass2:
            if User.objects.filter(username = username).exists():
                print('user already exists')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                print('email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,email=email,password=pass1,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('/')
        else:
            return redirect('register')
        
    else:
        return render(request,'register.html')       

def login(request):
    
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('wrong credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')