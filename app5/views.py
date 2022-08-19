from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from app5.models import UserData
from app5.serializers import UserSerializer

# Create your views here.

def signup(request):
    if request.method == "POST":
        name = request.POST['uname']
        phone = request.POST['phn']
        date = request.POST['dob']
        em = request.POST['email']
        pw = request.POST['passwd']
        #print(name)
        #print(phone)
        #print(date)
        #print(em)
        #print(pw)

        data = UserData(username=name, phone_no=phone, dob=date, email=em, pswd=pw)
        data.save()


    return render(request, 'signup.html')



def login(request) :
    return render(request, 'login.html' )

def redirect1(request) :
    return render(request, 'su.html' )

def redirect2(request) :
    return render(request, 'fail.html' )
 
def index(request) :
    return HttpResponse("Successfully created a web application")

@api_view(['GET'])
def firstApi(request) :
    message = "Created an API"
    return Response(message)



# Create your views here.
@csrf_exempt
def u_det(request, id = 0):

    if request.method == 'POST' :  # api post method
        u_det = JSONParser().parse(request)
        user_serial = UserSerializer(data = u_det)
        if user_serial.is_valid():
            user_serial.save()
            return JsonResponse({"status" : "success" , "data" : user_serial.data})
        else :
            return JsonResponse({"status" : "failed" , "data" : user_serial.errors})

    elif request.method == 'GET' :    # api get method
        products = UserData.objects.all()  

        user_serial = UserSerializer(products, many = True)
        return JsonResponse({"data": user_serial.data})
    
    elif request.method == 'PUT' :   # api put method
        products = JSONParser().parse(request)
        productsData = UserData.objects.get(id = products['id'])
        cu_sel = UserSerializer(productsData, products  )
        if cu_sel.is_valid():
            cu_sel.save()
            return JsonResponse({"status" : "data updated " , "data" : cu_sel.data})
        else :
            return JsonResponse({"status" : "couldnt update data" , "data" : cu_sel.errors})


    elif request.method == 'DELETE' :     # api delete method
        products = JSONParser().parse(request)
        productsData = UserData.objects.filter(id = products['id'])
        productsData.delete()
        
        return JsonResponse({"status" : "data deleted " })