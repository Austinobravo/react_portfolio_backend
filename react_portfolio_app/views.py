from smtplib import SMTPConnectError
import socket
from urllib.error import URLError
from .models import Projects,Technology,Experience,Services, Contact
from .serializers import ProjectsSerializer,TechnologySerializer,ExperienceSerializer,ServicesSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail, BadHeaderError
from rest_framework import  status
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class ProjectView(ListCreateAPIView):
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()

class ExperienceView(ListCreateAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

class TechnologyView(ListCreateAPIView):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all()

class ServicesView(ListCreateAPIView):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()

@api_view(['GET', 'POST'])
def contactView(request):
    if request.method == "POST":
        name = f'Message from: {request.data["name"]} and Email: {request.data["email"]}'
        email_message = request.data['message']
        CONTACT_EMAIL = 'austinobravo@gmail.com'
        ADMIN_EMAIL = ['support1@elitenessee.com', 'austinobravo@gmail.com']
        try:
            send_mail(name, email_message, CONTACT_EMAIL, ADMIN_EMAIL, fail_silently=True)
            contactMe = Contact(
                name= name,
                message = email_message,  
            )
            contactMe.save()
            return Response({'message': 'Your message have been sent.'},status=status.HTTP_200_OK)
        except BadHeaderError:
            return Response({'message':'An error occurred, Fill form again.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except socket.gaierror as dns_error:
            return Response({'message': 'No DNS network connection'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except URLError as e_error:
            return Response({'message': 'Poor or No network connection'}, status=status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED)
        except ObjectDoesNotExist:
            return Response({'message': 'Email not found'})
        except SMTPConnectError as smtp_connect_error:
            return Response({'message': 'Error connecting to the SMTP server'})
        except Exception as e:
            return Response({'message': "An error occured"})
    else:
        return Response({'message': 'No Emails Sent yet'})

