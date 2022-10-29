from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView, UserView, UserChangeView, UserPasswordChangeView



urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('account/<int:pk>', UserView.as_view(), name='account'),
    path('account/<int:pk>/update', UserChangeView.as_view(), name='user_update'),
    path('account/<int:pk>/password-change', UserPasswordChangeView.as_view(), name='password_change')
]