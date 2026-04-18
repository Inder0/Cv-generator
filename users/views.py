from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm,LoginForm
from django.contrib.auth.views import LoginView,PasswordResetView
# Create your views here.
def register(request):
    form=UserRegisterForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    context={
        'form':form
    }
    return render(request,"users/register.html",context)

def logout_view(request):
    logout(request)
    return render(request,"users/logout.html")


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm

class CustomPasswordResetView(PasswordResetView):
    def get_domain(self):
        return self.request.get_host()