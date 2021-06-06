from django.shortcuts import render,redirect
from . import api
from django.conf import settings



def home(request):
    if request.method == "POST":
        from_email = settings.DEFAULT_FROM_EMAIL #Define DEFAULT_FROM_EMAIL,MJ_APIKEY,MJ_APISECRET in your settings file
        to_emails = request.POST["email"]
        to_name = "First Name"
        options = dict()
        # options['name'] = request.POST['first_name'] --> You can send dynamic content by specifying the variable name in your template as {{var.name}}
        result = api.send_email(request,from_email=from_email, to_name=to_name, to_emails=to_emails, options=options,subject='subject',template_id=2939796)
        if result:
            return redirect('/mail-success')
    return render(request,'python_mail_jet/home.html')


def mail_success(request):
    return render(request,'python_mail_jet/mail_success.html')