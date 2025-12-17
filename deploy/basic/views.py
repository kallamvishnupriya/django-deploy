from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math

# Create your views here.
def home(request):
    return render(request,'home.html')
def sample(request):
    return HttpResponse("hello")
def sample1(request):
    return HttpResponse("welcome")
def sample2(request):
    info= {"data":["vishnu","priya","kallam","reddy"]}
    return JsonResponse(info)

def pagination(request):
    data=['a','b','c','d','e','f','g','h','i','j','k']
    page=int(request.GET.get("page",1))
    limit=int(request.GET.get("limit",3))

    start=(page-1)*limit
    end=page*limit
    total_pages=math.ceil(len(data)/limit)
    result=data[start:end]
    res={"status":"success","page":page,"total_pages":total_pages,"data":result}
    return JsonResponse(res)