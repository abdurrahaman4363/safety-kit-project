
from django.urls import path
from .views import UserAccountCreateView,UserLoginView,UserLogoutView,UserAccountUpdateView,PasswordChangeView
 
urlpatterns = [
    path('register/', UserAccountCreateView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserAccountUpdateView.as_view(), name='profile' ),
    path("profile/password_change/", PasswordChangeView.as_view(), name="password_change"),
    
]