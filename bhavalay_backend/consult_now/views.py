# views.py

from rest_framework import status
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import randint
from .models import Consultation
from .serializers import ConsultationSerializer

def send_otp(mobile, otp):
    url = f"https://control.msg91.com/api/v5/otp?template_id=64e46c81d6fc056a09428b84&mobile={mobile}&otp={otp}"

    payload = {}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authkey": "402924A9xeKSEJ3U64e46d64P1"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

@api_view(['POST'])
def create_consultation(request):
    if request.method == 'POST':
        serializer = ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            otp = str(randint(1000, 9999))  # Generate a 4-digit OTP
            serializer.validated_data['otp'] = otp  # Add OTP to the serialized data
            serializer.save()

            # Send OTP to the mobile number
            send_otp(serializer.validated_data['mobile_number'], otp)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verify_otp(request):
    if request.method == 'POST':
        mobile_number = request.data.get('mobile_number')
        otp = request.data.get('otp')

        try:
            consultation = Consultation.objects.get(mobile_number=mobile_number, otp=otp)
            consultation.otp = None  # Clear the OTP as it has been verified
            consultation.save()

            return Response({"status": "OTP verified"}, status=status.HTTP_200_OK)
        except Consultation.DoesNotExist:
            return Response({"status": "Invalid OTP or mobile number"}, status=status.HTTP_400_BAD_REQUEST)