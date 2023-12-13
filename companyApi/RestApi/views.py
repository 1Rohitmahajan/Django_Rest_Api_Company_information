from django.shortcuts import render
from rest_framework import viewsets
from RestApi.models import Company,Employee
from rest_framework.response import Response
from RestApi.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    #companies/{companyId}/employees get this 
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emp=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emp,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company does not exit'
            })
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer