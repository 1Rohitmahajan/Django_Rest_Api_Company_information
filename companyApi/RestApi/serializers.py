from rest_framework import serializers
from RestApi.models import Company,Employee
#create serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField() #upgrate not allowed
    class Meta: 
        model=Company
        fields="__all__"#all field get
        

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"