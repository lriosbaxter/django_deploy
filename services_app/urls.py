from django.contrib import admin
from django.urls import path

from services_app.views import HomeView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name="login"),
    path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name="logout"),
]