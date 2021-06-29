from django.urls import include, path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.CreateUserView.as_view()),
    path('email/change/', views.ChangeEmailView.as_view()),
    path('login/', views.LogInView.as_view()),
    path('password/', include([
        path('change/', views.ChangePasswordView.as_view()),
        path('forgot/', views.ForgotPasswordView.as_view()),
        path('reset/', views.ResetPasswordView.as_view()),
    ])),
    path('retrieve/', views.RetrieveUserView.as_view()),
    path('update/', views.UpdateUserView.as_view()),
    path('verify/', include([
        path('', views.VerifyUserView.as_view()),
        path('resend/', views.ResendVerificationEmailView.as_view()),
    ])),
]
