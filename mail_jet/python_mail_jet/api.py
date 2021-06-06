import requests
from django.conf import settings
import json

def send_email(request, **kwargs):
    result = False
    from_email = kwargs.get("from_email", None)
    options = kwargs.get("options", None)
    to_emails = kwargs.get("to_emails", None)
    template_id = kwargs.get("template_id", None)
    subject = kwargs.get("subject", "General Mail")
    to_name = kwargs.get("to_name", None)
    

    data = {
    "Messages":[
            {
            "From": {
                    "Email": str(from_email),
                    "Name": "Your Name"
            },
            "To": [
                {
                    "Email": str(to_emails),
                    "Name": str(to_name)
                }
            ],
            "Variables": options,
            "TemplateID": template_id,
            "TemplateLanguage": True,
            "TemplateErrorReporting": {
            "Email": str(from_email),
            "Name": "Your Name"
            },
            "Subject": str(subject)
            }
            ]
        }
    data = json.dumps(data)

    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post('https://api.mailjet.com/v3.1/send', headers=headers, data=data, auth=(settings.MJ_APIKEY, settings.MJ_APISECRET))     
    result = True
    return result
    

