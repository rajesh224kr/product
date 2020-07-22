from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from app.models import MyProductList


def showindex(request):
    return render(request,'index.html')


def addproduct(request):
    if request.method=='POST':
        idno=request.POST.get('t1')
        name=request.POST.get('t2')
        price=request.POST.get('t3')
        date=request.POST.get('t4')
        MyProductList(idno=idno,name=name,price=price,date=date).save()
        return redirect('/allproductview/')
    return render(request,'addproduct.html')


def allproductview(request,):
    data=MyProductList.objects.all()
    return render(request,'allproduct.html',{'data':data})


def udateproduct(request):
    data= MyProductList.objects.all()
    return render(request,'udateproduct.html',{'data':data})


def update(request,idno):
    data=MyProductList.objects.get(idno=idno)
    return render(request,'update.html',{'data':data})


def delete(request,idno):
    data=MyProductList.objects.get(idno=idno)
    data.delete()
    return redirect('/allproductview/')


def deletedata(request):
    data= MyProductList.objects.all()
    return render(request,'deletedata.html',{'data':data})


#####   nlp project

class Nlppro(APIView):
    def post(self,request,format=None):
        print('hi')
        data = {'name':'rajesh'}
        return Response(data=data)
