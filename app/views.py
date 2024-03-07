from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProductCrud(ViewSet):
    def list(self, request):
        LPO= Product.objects.all()
        JPO= ProductSerializer(LPO,many=True)
        return Response(JPO.data)
    
    def retrive(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JPO=ProductSerializer(PO)
        return Response(PO.data)
        
    def create(self,request):
        JD=request.data
        PDO= ProductSerializer(data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'Created':'Data is inserted'})
    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductSerializer(PO,data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'Error':'Not Able To update'})

    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductSerializer(PO,data=JD,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'Error':'Not Able To Update'})

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Deleted':'Data is Deleted'})
