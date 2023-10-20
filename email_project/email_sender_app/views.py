import datetime

from django.http import JsonResponse
from django.conf import settings

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import loader

from rest_framework.views import APIView

class HandleEmail(APIView):
    def post(self, request, **kwargs):
        date = request.data.get("date", "")
        fullname = request.data.get("fullname", "")
        email = request.data.get("email", "")
        phone_number = request.data.get("phone_number", "")
        service = request.data.get("service", "")
        message = request.data.get("message", "")
        html_message = loader.render_to_string(
            'email_sender_app/message.html',
            {
                "date": date,
                "fullname":fullname,
                "email": email,
                "phone_number": phone_number,
                "service": service,
                "message": message
            })
        send_mail(
            'Appointment Booking',
            'Appointment Booking Scheduled.',
            settings.EMAIL_HOST_USER , 
            [settings.EMAIL_RECIPIENT], 
            html_message=html_message,
            fail_silently=False,
        )

        return JsonResponse(data={"message": "mail sent"})


    