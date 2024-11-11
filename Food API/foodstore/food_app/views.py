from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Food
from .serializers import FoodSerializers
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status

# Create your views here.

class FoodViewset(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers

    def get_serializer_class(self):
        return self.serializer_class
    
    #get all details
    def list(self,request):
        try:
            sample_objs = Food.objects.all()
            serializer = self.get_serializer(sample_objs, many = True)

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
                })
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
        
        #   add details
    def create(self,request):
        try:
            serializer = self.get_serializer(data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_201_CREATED,
                    'data':serializer.error,
                    'message':'Invalid Data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':'Food added Succesfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
        #get single detail
    def retrieve(self, request, pk=None):
        try:
            id = pk
            if id is not None:
                sample_obj = self.get_object()   
                serializer = self.get_serializer(sample_obj)
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
        
        # update all the fields of details
    def update(self,request,pk=None):
        try:
            Food_objs = self.get_object()
            serializer = self.get_serializer(Food_objs, data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Invalid Data'
                })
            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'Book updated Succesfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
        # Update specific fields
    def partial_update(self, request,pk = None):
        try:
            Food_objs = self.get_object()
            serializer = self.get_serializer(Food_objs, data= request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'sataus':status.HTTP_400_BAD_REQUEST,
                    'data':serializer.error,
                    'message':'Invalid Data'
                })
            serializer.save()
            return Response({
                    'sataus':status.HTTP_200_OK,
                    'data':serializer.data,
                    'message':'Book updated Succesfully'
                })
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
        # delete an sample 
    def destroy(self,request, pk):
        try:
            id = pk
            Food_objs = self.get_object()
            Food_objs.delete()
            return Response({
                'sataus':status.HTTP_400_BAD_REQUEST,
                'message':'Invalid Data'
                })
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })