from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .forms import RegisterUserForm
from django.contrib.auth import  login
from django.contrib.auth.decorators import login_required
from .models import UserList
# Create your views here.

class Login(LoginView):
    template_name = "users/accounts/login.html"

class Logout(LogoutView):
    next_page = "/"    


class RegisterUser(FormView):
    template_name = "users/accounts/register.html"
    form_class = RegisterUserForm
    success_url = "/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

@login_required    
def profile(request):
    user = request.user   
    user_lists = UserList.objects.filter(user=user)
    return render(request, "users/accounts/profile.html",{"user":user,
                                                          "user_lists":user_lists}) 