from django.urls import path
from . import views
from django.conf.urls.static import static 
from .views import *
from django.contrib import admin 
from django.conf import settings 

urlpatterns = [
     path('login/', views.login),
     path('loginform/', views.loginform),
     path('index/', views.index),
     path('blank/', views.blank),
     path('edit_stock/<int:pno>/', views.edit_stock,name='update_stock'),
     path('edit_stockForm/', views.edit_stockForm),
     path('edit_purchase/<int:purchase_no>', views.edit_purchase,name="pur"),
     path('purchase/', views.purchase),
     path('edit_purchaseForm/', views.edit_purchaseForm),
     path('sales/', views.sales),
     path('edit_sales/<int:sales_no>', views.edit_sales,name="sal"),
     path('edit_salesForm/', views.edit_salesForm),
     path('bill_purchase/', views.bill_purchase),
     path('bill_sales/', views.bill_sales),
     path('stock_form/', views.stock_form),
     path('purchase_form/', views.purchase_form),
     path('sales_form/', views.sales_form),
     path('bill_purchase_form/', views.bill_purchase_form),
     path('bill_sales_form/', views.bill_sales_form),
     path('vendor_purchase/<str:vendor>/<str:date>', views.vendor_purchase,name = 'ven_purchase'),
     path('vendor_sales/<str:vendor>/<str:date>', views.vendor_sales,name = 'ven_sales'),
     path('billing_sales/', views.billing_sales),
     path('billing_purchase/', views.billing_purchase),
     path('history/', views.history),
     path('history_show/', views.history_show,name='hist_show'),
     path('summary/', views.summary),
     path('download_sales/', views.download_sales),
     path('download_purchase/', views.download_purchase),
     path('purchase_records/', views.purchase_records),
     path('sales_records/', views.sales_records),
     path('logout_view/', views.logout_view),
     path('file/<str:pno>', views.image,name="fil"),

     
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 