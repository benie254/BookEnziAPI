from django.shortcuts import render
from rest_framework.views import APIView
from enzi_app.serializers import BookingSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
import sendgrid
from decouple import config 
from sendgrid.helpers.mail import *
from rest_framework.response import Response
from rest_framework import status
import random 
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.utils.encoding import force_str
from django.shortcuts import redirect
from django.http import Http404

from enzi_app.models import ClientBooking




# Create your views here.
class ClientBookingView(APIView):
    def get(self,request):
        bookings = ClientBooking.objects.all().order_by('-checkin')
        serializer = BookingSerializer(data=request.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            name = request.data['name']
            email = request.data['email']
            checkin = request.data['checkin']
            checkout = request.data['checkout']
            user = serializer.save()
            user.refresh_from_db()
            id = random.randint(1,999999)
            current_site = get_current_site(request)
            msg = render_to_string('email/confirm-booking.html', {
                'name': name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(id)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(id),
                'email': email,
                'checkin': checkin,
                'checkout': checkout,
            })
            sg = sendgrid.SendGridAPIClient(api_key=config('SENDGRID_API_KEY'))
            message = Mail(
                from_email = Email("davinci.monalissa@gmail.com"),
                to_emails = email,
                subject = "Booking Confirmation",
                html_content='<p>Hello, ' + str(name) + ', <br><br>' + msg
            )
            print(message)
            try:
                sendgrid_client = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))
                response = sendgrid_client.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e)
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
# @permission_classes([AllowAny,])
def activate(request, uidb64, token):
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = uid
        return redirect('http://localhost:4200/booking/confirmed/' + uid)
        # if account_activation_token.check_token(uid,token):
        #     response = Response()
        #     successMsg = 'Confirmed! Activation link is valid.'
        #     response.data = {
        #         'success':successMsg,
        #     }
        #     # return response 
        #     return redirect('http://localhost:4200/booking/confirmed/' + uid)
        # else:
        #     Http404
        #     response = Response()
        #     errorMsg = 'Sorry, activation link is invalid.'
        #     response.data = {
        #         'error':errorMsg,
        #     }
        #     return response 
            # serializer = PasswordResetSerializer
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request,'index.html')