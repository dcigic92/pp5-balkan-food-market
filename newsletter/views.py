from django.shortcuts import render
from django.contrib import messages

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import json


# Mailchimp Settings
API_KEY = settings.MAILCHIMP_API_KEY
SERVER = settings.MAILCHIMP_DATA_CENTER
LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID


def newsletter(request):
    """ A view to allow users to subscribe to 
    email newsletter using Mailchimp. """

    if request.method == "POST":
        email = request.POST['email']
        mailchimp = Client()
        mailchimp.set_config({
            "api_key": API_KEY,
            "server": SERVER,
        })

        member_info = {
            "email_address": email,
            "status": "subscribed",
        }

        try:
            mailchimp.lists.add_list_member(LIST_ID, member_info)
            messages.success(request, 'Thank you for subscribing!')
        except ApiClientError as error:
            error_message = json.loads(error.text)['detail']
            messages.error(request, f'{error_message}')

    context = {
        'on_newsletter_page': True
    }

    return render(request, "newsletter/newsletter.html", context)