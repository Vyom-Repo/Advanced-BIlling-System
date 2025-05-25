from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import OrganisationDetails,CustomerDetails,Invoice_Details,Product
from .forms import OrganisationForm,CustomerForm,Invoice_Details_Form,Product_Form
from django.urls import reverse_lazy
from django.http import HttpResponse

def OrganisationView(request):
    forms = OrganisationForm(request.POST or None)
    return render(request,'signup.html',{'org':forms})

def LoginView(request):
    
    return render(request,'registration/login.html')

def index(request):  
    
    return render(request,'index.html')

    
# Customer Data ---------------
   
def CustomerView(request):
        return render(request,'customer.html')

def CustomerFormView(request):
    return render(request,'customerform.html')


    
def CustomerUpdate(request):  
    return render(request,'customerform.html')

# Invoice Data ---------------

def Total_Invoice_Page(request):
    return render(request,'Total_Invoice_Page.html')


def InvoiceView(request):
    return render(request,'temp_invoice.html')
   
def InvoicePage(request):
    return render(request,'invoice_list.html')
    
    
    
def DetailPage(request):
    return render(request,'DetailPage.html')


def InvoiceForm(request):
        return render(request,'invoiceform.html')

    
def InvoiceUpdate(request):
        return render(request,'invoiceform.html')


def ProductView(request):
    return render(request,'temp_product.html')


def ProductForm(request):
        return render(request,'productform.html')
    
def ProductUpdate(request):
    return render(request,'productform.html')

def logout(request):
    return redirect('login')

