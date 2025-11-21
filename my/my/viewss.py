from django.shortcuts import render
from django.http import HttpResponse,FileResponse
import os

def login(request):
    return render(request,'login.html')
def dashbord(request):
    return render(request,'dashbord.html')
def course(request):
    return render(request,'course.html')

#==============================math===============
def maths(request):
    return render(request,'subject.html')

#=================coa==============

def coa(request):
    return render(request,'coa.html')

def python(request):
    return render(request,'python.html')

def dsa(request):
    return render(request,'dsa.html')

def hv(request):
    return render(request,'humanvalues.html')

def dstl(request):
    return render(request,'dstl.html')

def de(request):
    return render(request,'subject.html')
#====================================questions==============================
def questions(request):
    return render(request,'subject.html')
#========================================dpp=============================
def dpp(request):
    return render(request,'subject.html')
#==========================================pyq==============================
def pyq(request):
    return render(request,'subject.html')
#------------------------------------------notes--------------------------
def notes(request):  
    id=request.GET.get('id')
    filepath = os.path.join("media", "document.pdf")
    from django.http import FileResponse, HttpResponse

def notes(request):
    element_id = request.GET.get('id')  # "123"
    if element_id == "123":
        return FileResponse(open(r"C:\Users\Shivam\OneDrive\Desktop\PROJECT\my\static\my\book-list.pdf", 'rb'),
                            content_type='application/pdf')


    

    


    if(id==3):  #----------------------dstl notes========================
     return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    

    if(id==1):   #===================python notes==================
     return FileResponse(open(r"C:\Users\Shivam\Downloads\book-list.pdf", 'rb'), content_type='application/pdf')
    
    
   

   
