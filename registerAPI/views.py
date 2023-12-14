import jdatetime
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from .serializers import Phone_serializer
from rest_framework.response import Response
from rest_framework import status
from .models import RegisterModel
from .utils import is_mobile,revalidate_phone
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
    def post(self,request):
        try:
            phone_recieved = Phone_serializer(data=request.data)
            phone_recieved.is_valid(raise_exception=True)
            phone_obj = phone_recieved.validated_data
        except:
            return Response(REGISTER_FAILD,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        result_validate = revalidate_phone(phone_obj=phone_obj)
        if result_validate == "CHAR_COUNT":
            return Response(REGISTER_FAILD_CHAR_COUNT, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        elif result_validate == "WRONG_NUMBER":
            return Response(REGISTER_FAILD_WRONG_NUMBER, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            if is_mobile(phone_number=result_validate) == True:
                object = RegisterModel(phone_number=result_validate, sent_sms_at=jdatetime.datetime.now(),is_mobile=True)
                object.save()
                return Response(REGISTER_ACCEPT_MOBILE,status.HTTP_200_OK)
            else:
                object = RegisterModel(phone_number=result_validate, sent_sms_at=jdatetime.datetime.now(),is_mobile=False)
                object.save()
                return Response(REGISTER_ACCEPT_LANDLINE,status.HTTP_200_OK)

class ShowRegisteration(APIView):
    include = openapi.Parameter('include', openapi.IN_QUERY,
                                 description="show phone number include this number",
                                 type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[include])
    def get(self,request):
        phone_substring = request.query_params.get("include")
        try:
            query_object = list(RegisterModel.objects.filter(phone_number__contains=phone_substring))
            result = []
            for obj in query_object:
                result.append(obj.phone_number)
        except Exception as ex:
            result = SHOW_REGISTERED_PHONE_NOT_FOUND
        return Response(result,status.HTTP_200_OK)