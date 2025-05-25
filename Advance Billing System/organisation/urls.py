from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',OrganisationView,name = 'signup'),
    path('',LoginView, name='login'),
    path('index/',index, name = 'index'),
    path('customer/',CustomerView,name = 'customer'),
    path('customerform/',CustomerFormView,name = 'customerform'),
    path('customerUpdate/',CustomerUpdate,name='CustUp'),
    path('invoiceview/',InvoiceView,name = 'invoiceview'),
    path('invoicepage/',InvoicePage,name='invopage'),
    path('invoiceform/',InvoiceForm,name='invoiceform'),
    path('invoiceUpdate/',InvoiceUpdate,name='InvoUp'),
    path('productview/',ProductView,name = 'productview'),
    path('productform/',ProductForm,name='productform'),
    path('productUpdate/',ProductUpdate,name='ProdUp'),
    path('detailpage/',DetailPage,name='detailpage'),
    path('logout/',logout,name = "logout"),
    path('all_invoices/',Total_Invoice_Page,name='total_invoice_page'),
]