from django.shortcuts import render, redirect
from django.views.generic import View
from services_app.forms import SignUpUserForm

from django.contrib.auth import login, authenticate


# class TestView(View):

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        authenticate(request)
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return False


class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request):
        form = SignUpUserForm(request.GET)
        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = SignUpUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            login(request, user)
            return redirect('home')


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
