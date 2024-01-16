from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView,LogoutView
from .models import UserAccount
from django.contrib.auth import login,logout
from django.views import View
from django.contrib import messages
from .forms import UserAccountCreationForm, UserUpdateForm, StyledPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

class UserAccountCreateView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserAccountCreationForm
    success_url = reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.success(self.request, 'Information incorrect')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Successfully Created Your Account.')
        print(form.cleaned_data)
        user = form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "accounts/user_login.html"

    def form_valid(self, form):
        messages.success(self.request, 'Successfully Login.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Login Information Incorrect.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("home")
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy("login")


class UserAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def form_valid(self, form):
        messages.success(self.request, 'Successfully Upadate Information.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Information Incorrect.')
        return super().form_invalid(form)

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  
        return render(request, self.template_name, {'form': form})    
    




class PasswordChangeView(LoginRequiredMixin, FormView):
    template_name = "accounts/password_change.html"
    form_class = StyledPasswordChangeForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, 'Successfully Changed Password.')
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Information Incorrect')
        return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user

        return kwargs