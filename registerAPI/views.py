import jdatetime
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from .serializers import Phone_serializer
from rest_framework.response import Response
from rest_framework import status
from .models import RegisterModel
from .utils import is_mobile, revalidate_phone, send_sms, check_time
from .common import (
    REGISTER_FAILD,
    REGISTER_ACCEPT_MOBILE,
    REGISTER_ACCEPT_LANDLINE,
    REGISTER_FAILD_CHAR_COUNT,
    REGISTER_FAILD_WRONG_NUMBER,
    SHOW_REGISTERED_PHONE_NOT_FOUND
)
class RegisterView(APIView):
    @swagger_auto_schema(request_body=Phone_serializer)
    def post(self, request):
        try:
            phone_recieved = Phone_serializer(data=request.data)
            phone_recieved.is_valid(raise_exception=True)
            phone_obj = phone_recieved.validated_data
        except:
            return Response(REGISTER_FAILD, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        result_validate = revalidate_phone(phone_obj=phone_obj)
        if result_validate == "CHAR_COUNT":
            return Response(REGISTER_FAILD_CHAR_COUNT, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        elif result_validate == "WRONG_NUMBER":
            return Response(REGISTER_FAILD_WRONG_NUMBER, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        # Check if record exists and if sent_sms_at is within the past day
        existing = RegisterModel.objects.filter(phone_number=result_validate).order_by('-sent_sms_at').first()
        if existing and existing.sent_sms_at > jdatetime.datetime.now() - jdatetime.timedelta(days=1):
            print(f"TOO MANY REQUEST BY {result_validate}")
            return Response(REGISTER_FAILD, status=status.HTTP_429_TOO_MANY_REQUESTS)  # Too many requests

        is_mobile_flag = is_mobile(phone_number=result_validate)
        obj = RegisterModel(
            phone_number=result_validate,
            sent_sms_at=jdatetime.datetime.now(),
            is_mobile=is_mobile_flag
        )
        obj.save()

        if is_mobile_flag:
            if check_time():  # Assuming this checks whether SMS should be sent now
                send_sms(phone_number=result_validate)
                print(f"SMS SENT TO NUMBER: {result_validate}")
            return Response(REGISTER_ACCEPT_MOBILE, status=status.HTTP_200_OK)
        else:
            print(f"PHONE NUMBER NOT RECOGNIZED: {result_validate}\nOR TIME IS NOT APPOPRIATE FOR SENDING SMS")
            return Response(REGISTER_ACCEPT_LANDLINE, status=status.HTTP_200_OK)

class ShowRegisteration(APIView):
    include = openapi.Parameter(
        'include',
        openapi.IN_QUERY,
        description="Show phone numbers that include this substring",
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[include])
    def get(self, request):
        phone_substring = request.query_params.get("include")

        try:
            if phone_substring:
                query_object = RegisterModel.objects.filter(phone_number__contains=phone_substring)
            else:
                query_object = RegisterModel.objects.all()

            result = [obj.phone_number for obj in query_object]

        except Exception as ex:
            result = SHOW_REGISTERED_PHONE_NOT_FOUND

        return Response(result, status.HTTP_200_OK)
