from django.shortcuts import render
from django.views import View  # 
from django.views.generic import TemplateView


     # views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import RegistrationLog, LoginAttempt


##from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import authenticate, login
#from django.http import HttpRespons


# Create your views here.
class HomePage(TemplateView):
    template_name = 'turningtide/home.html'  # Make sure the template exists

#class HomePage(View):  # 'self' is not part of the class definition
  #  def get(self, request):  # Add 'self' and 'request' as parameters
 #       return render(request, "turningtide/home.html")

class NgoPage(View):  
    def get(self, request):  
        return render(request, "turningtide/ngos.html")
    
class BlogPage(View):  
    def get(self, request):  
        return render(request, "turningtide/blogs.html")    
    
    
    
class LoginPage(View):  
    def get(self, request):  
        return render(request, "turningtide/login.html")    


class LogReg(View):  
    def get(self, request):  
        return render(request, "turningtide/log-reg.html") 
    
class MapsPage(View):  
    def get(self, request):  
        return render(request, "turningtide/map.html")    



    
class Donation(View):  
    def get(self, request):  
        return render(request, "turningtide/donation.html")    

    
class EcoShopsPage(View):  
    def get(self, request):  
        return render(request, "turningtide/ecoshops.html")  
    


class ContributionPage(View):  
    def get(self, request):  
        return render(request, "turningtide/yourcontribution.html")      
    
class After(View):  
    def get(self, request):  
        return render(request, "turningtide/afterparty.html")          
    


class CleanupPage(View):  
    def get(self, request):  
        return render(request, "turningtide/cleanup.html")  


class leaderBoardPage(View):  
    def get(self, request):  
        return render(request, "turningtide/leaderboard.html")  
    
class PrizesPage(View):  
    def get(self, request):  
        return render(request, "turningtide/prizes.html") 
    
    
class AboutPage(View):  
    def get(self, request):  
        return render(request, "turningtide/about.html")  
    
class Participate(View):  
    def get(self, request):  
        return render(request, "turningtide/participation.html")    
    

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the registration
            RegistrationLog.objects.create(user=user, success=True, ip_address=request.META.get('REMOTE_ADDR'))
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'turningtide/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Log successful login
                LoginAttempt.objects.create(user=user, success=True, ip_address=request.META.get('REMOTE_ADDR'))
                return redirect('home')  # Redirect to a home page or dashboard
            else:
                # Log failed login attempt
                LoginAttempt.objects.create(success=False, ip_address=request.META.get('REMOTE_ADDR'))
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'turningtide/login.html', {'form': form})