from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from accounts.forms import RegisterForm, LoginForm


'''def register_view(request):

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            return redirect('login')
    else:   
        user_form = UserCreationForm()

    return render(request, 'register.html', {'user_form': user_form})

'''

class SignUpView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class SignInView(View):
    template_name = 'login.html'
    form_class = AuthenticationForm


    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cars_list')
        return render(request, self.template_name, {'form': form})
        

class LogoutView(View):
    

    def get(self, request):
        logout(request)
        return redirect('cars_list')


def logout_view(request):
    logout(request)

    return redirect('cars_list')
    
    
