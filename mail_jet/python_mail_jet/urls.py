from django.urls import path,include
from . import views

app_name = 'python_mail_jet'

urlpatterns = [
    path('',views.home,name='home'),
    path('mail-success',views.mail_success,name='mail_success'),
]

