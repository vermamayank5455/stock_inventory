from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import stockform
from .forms import purchaseform
from .forms import salesform
from .forms import *
from store.models import Stock
from store.models import Purchase
from store.models import Sales
from django.contrib.auth.models import User,auth
from django.contrib import messages
import datetime
from django.contrib.auth import logout
from .decoraters import authorized_user
from django.db.models.functions import Lower
import csv





# Create your views here.

invoice_no=999

def login(request):
    if request.method =="POST":
        Username=request.POST['username']
        Password=request.POST['password']
        user=auth.authenticate(username=Username,password=Password)

        if user is not None:
            auth.login(request,user)
            response=redirect('/admin-se/index/')
            response.set_cookie('username',Username)
            return response
        
        else:
            messages.info(request,'invalid credentials')
            return redirect('/admin-se/loginform/')

        
    else:
        return render(request,'login.html')
        

def loginform(request):
    return render(request,'store/login.html')


@authorized_user
def index(request):
    all_entries=Stock.objects.all()
    all_purchase=Purchase.objects.all().order_by('-date')
    all_sales=Sales.objects.all().order_by('-date')
    stock=Stock.objects.all().values('product').distinct()
    var=[]
    for row in stock:
        temp=dict()
        add=0
        prod=row.get("product")
        all_products=Stock.objects.filter(product=prod)
        temp['product']=prod
        temp['pno']=all_products[0].pno
        for r in all_products:
            add=add+r.quantity
        temp['add']=add
        var.append(temp)
    return render(request,'store/index.html',{"msg":all_entries,"msg1":all_purchase,"msg2":all_sales,"msg4":var})

@authorized_user
def purchase_records(request):
    all_purchase=Purchase.objects.all().order_by('-date')
    return render(request,'store/purchase_records.html',{"msg1":all_purchase})

@authorized_user
def sales_records(request):
    all_sales=Sales.objects.all().order_by('-date')
    return render(request,'store/sales_records.html',{"msg2":all_sales})

@authorized_user
def blank(request):
    return render(request,'store/blank.html')

@authorized_user
def edit_stock(request,pno):
    form=Stock.objects.get(pno=pno)
    return render(request,'store/edit_stock.html',{'msg4':form})

@authorized_user
def edit_stockForm(request):
    if request.method == "POST" and 'edit' in request.POST:
        Pno = request.POST['pno']
        Product = request.POST['product']
        Hsn = request.POST['hsn']
        Quantity = request.POST['quantity']
        del_stock = Stock.objects.get(pno=Pno)
        form = stockform(request.POST,instance=del_stock)
        if form.is_valid():
            form.save()
            a="your form is saved"
        else:
            p=form.errors
            return render(request,'store/edit_stock.html',{"a":p})
    if request.method == "POST" and 'delete' in request.POST:
        Pno = request.POST['pno']
        Product = request.POST['product']
        Hsn = request.POST['hsn']
        Quantity = request.POST['quantity']
        form = stockform(request.POST)
        del_stock = Stock.objects.get(pno=Pno)
        del_stock.delete()
        a="your form is deleted"
    return render(request,'store/edit_stock.html',{"p":a})

@authorized_user
def purchase(request):
    products=Stock.objects.all().order_by(Lower('product'))
    return render(request,'store/purchase.html',{"products":products})

@authorized_user
def edit_purchase(request,purchase_no):
    form=Purchase.objects.get(purchase_no=purchase_no)
    return render(request,'store/edit_purchase.html',{'msg4':form})

@authorized_user
def edit_purchaseForm(request):
    if request.method == "POST" and 'edit' in request.POST:
        Purchase_no = request.POST['purchase_no']
        Product_id = request.POST['product_id']
        Product = request.POST['product']
        Vendor = request.POST['vendor']
        Quantity = request.POST['quantity']
        Price = request.POST['price']
        Date = request.POST['date']
        Invoice_no = request.POST['invoice_no']
        Gst = request.POST['gst']
        del_stock = Purchase.objects.get(purchase_no=Purchase_no)
        form = purchaseform(request.POST,instance=del_stock)
        if form.is_valid():
            form.save()
            p="your form is saved"
        else:
            p=form.errors
            return render(request,'store/edit_purchase.html',{"a":p})
    if request.method == "POST" and 'delete' in request.POST:
        Purchase_no = request.POST['purchase_no']
        Product_id = request.POST['product_id']
        Product = request.POST['product']
        Vendor = request.POST['vendor']
        Quantity = request.POST['quantity']
        Price = request.POST['price']
        Date = request.POST['date']
        form = purchaseform(request.POST)
        del_stock = Purchase.objects.get(purchase_no=Purchase_no)
        del_stock.delete()
        p="your form is deleted"
    return render(request,'store/edit_purchase.html',{"p":p})

@authorized_user
def sales(request):
    products=Stock.objects.all().order_by(Lower('product'))
    return render(request,'store/sales.html',{"products":products})

@authorized_user
def edit_sales(request,sales_no):
    form=Sales.objects.get(sales_no=sales_no)
    return render(request,'store/edit_sales.html',{'msg4':form})

@authorized_user
def edit_salesForm(request):
    if request.method == "POST" and 'edit' in request.POST:
        Sales_no = request.POST['sales_no']
        Product_id = request.POST['product_id']
        Product = request.POST['product']
        Vendor = request.POST['vendor']
        Quantity = request.POST['quantity']
        Price = request.POST['price']
        Date = request.POST['date']
        Gst_no = request.POST['gst_no']
        Gst_rate = request.POST['gst_rate']
        Address = request.POST['address']
        Phone = request.POST['phone']
        del_stock = Sales.objects.get(sales_no=Sales_no)
        form = salesform(request.POST,instance=del_stock)
        if form.is_valid():
            new_five = form.save(commit=False)
            new_five.product = Stock.objects.get(pno=Product_id).product
            new_five.save()
            p="your form is saved"
        else:
            p=form.errors
            return render(request,'store/edit_sales.html',{"a":p})
    if request.method == "POST" and 'delete' in request.POST:
        Sales_no = request.POST['sales_no']
        Product_id = request.POST['product_id']
        Product = request.POST['product']
        Vendor = request.POST['vendor']
        Quantity = request.POST['quantity']
        Price = request.POST['price']
        Date = request.POST['date']
        Address = request.POST['address']
        form = salesform(request.POST)
        del_stock = Sales.objects.get(sales_no=Sales_no)
        del_stock.delete()
        p="your row is deleted"
    return render(request,'store/edit_sales.html',{"p":p})

@authorized_user
def bill_sales(request):
    return render(request,'store/bill_sales.html')


def bill_purchase(request):
    return render(request,'store/bill_purchase.html')


@authorized_user
def stock_form(request):
    if request.method == "POST":
        Product = request.POST['product']
        Vendor = request.POST['vendor']
        Quantity = request.POST['quantity']
        Size = request.POST['size']
        form = stockform(request.POST)
        if form.is_valid():
            new_five = form.save(commit=False)
            new_five.product = Product[:3] +"-"+ Vendor[:3] +"-"+ Size
            form.save()
            p="your form is saved"
            return render(request,'store/blank.html',{"p":p})
        else:
            p=form.errors
            return render(request,'store/blank.html',{"a":p})
    return render(request,'store/blank.html')

@authorized_user
def purchase_form(request):
    if request.method == "POST":
        Invoice_no = request.POST['invoice_no']
        Product_id = request.POST['product_id']
        Vendor = request.POST['vendor']
        Quantity = request.POST['quantity']
        Price = request.POST['price']
        Date = request.POST['date']
        Gst = request.POST['gst']
        form = purchaseform(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            new_five = form.save(commit=False)
            new_five.product = Stock.objects.get(pno=Product_id).product
            new_five.save()
            a="your form is saved"
        else:
            p=form.errors
            return render(request,'store/purchase.html',{"a":p})
    all_entries=Purchase.objects.all()
    return render(request,'store/purchase.html',{"msg1":all_entries,"p":a})

@authorized_user
def sales_form(request):
    if request.method == "POST":
        Product_id = request.POST['product_id']
        Vendor = request.POST['vendor']
        Quantity = request.POST['quantity']
        Price = request.POST['price']
        Date = request.POST['date']
        Gst_no = request.POST['gst_no']
        Gst_rate = request.POST['gst_rate']
        Phone = request.POST['phone']
        Address = request.POST['address']
        form = salesform(request.POST)
        if int(Quantity) <= Stock.objects.get(pno=Product_id).quantity:
            pass
        else:
            g="you dont have enough stock"
            return render(request,'store/sales.html',{"a":g})

        if form.is_valid():
            new_five = form.save(commit=False)
            new_five.product = Stock.objects.get(pno=Product_id).product
            new_five.hsn = Stock.objects.get(pno=Product_id).hsn
            new_five.save()
            a="your form is saved"
            
        else:
            p=form.errors
            return render(request,'store/sales.html',{"a":p})
    all_entries=Sales.objects.all()
    return render(request,'store/sales.html',{"msg2":all_entries,"p":a})

@authorized_user
def bill_purchase_form(request):
    if request.method == "POST":
        Vendor = ""
        Date = ""
        Vendor = request.POST['vendor']
        Date = request.POST['date']
        entries = ""
        if Date=="":
            entries = Purchase.objects.filter(vendor=Vendor)
        elif Vendor=="":
            entries = Purchase.objects.filter(date=Date)
        else:
            entries = Purchase.objects.filter(vendor=Vendor).filter(date=Date)
    return render(request,'store/bill_purchase.html',{"msg1":entries})
    
@authorized_user
def bill_sales_form(request):
    if request.method == "POST":
        Vendor = ""
        Date = ""
        Vendor = request.POST['vendor']
        Date = request.POST['date']
        entries = ""
        if Date=="":
            entries = Sales.objects.filter(vendor=Vendor)
        elif Vendor=="":
            entries = Sales.objects.filter(date=Date)
        else:
            entries = Sales.objects.filter(vendor=Vendor).filter(date=Date)
        # print("entries are ", entries[0].id)
    return render(request,'store/bill_sales.html',{"msg1":entries})

@authorized_user
def vendor_purchase(request,vendor,date):
    entries = ""
    entries = Purchase.objects.filter(vendor=vendor).filter(date=date)
    var=[]
    add=0
    for record in entries:
        temp=dict()
        temp['product']=record.product
        temp['date']=record.date
        temp['price']=record.price
        temp['quantity']=record.quantity
        temp['total']=record.price*record.quantity
        var.append(temp)
        add=(record.price*record.quantity)+add
    details = entries[0]
    today=datetime.date.today()
    products=Stock.objects.all()
    return render(request,'store/billing_purchase.html',{"msg3":var,"details":details,"total":add,"today":today,"products":products,"date1":date,"vendor1":vendor})

@authorized_user
def billing_purchase(request):
    if request.method == "POST":
        Product_id = request.POST['product_id']
        Vendor = request.POST['vendor']
        Quantity = request.POST['quantity']
        Price = request.POST['price']
        Date = request.POST['date']
        
        print("Data in Request is ", request.POST)

        form = purchaseform(request.POST)
        if form.is_valid():
            new_five = form.save(commit=False)
            new_five.product = Stock.objects.get(pno=Product_id).product
            new_five.save()
            a="your form is saved"
            print("Form has been saved")
        else:
            p=form.errors
            print("errors are ", p)
            return render(request,'store/billing_purchase.html',{"a":p})

            
    print("date is",Date,Vendor)
    entries = ""
    entries = Purchase.objects.filter(vendor=Vendor).filter(date=Date)
    var=[]
    add=0
    details = entries[0]
    for record in entries:
        temp=dict()
        temp['product']=record.product
        temp['date']=record.date
        temp['price']=record.price
        temp['quantity']=record.quantity
        temp['total']=record.price*record.quantity
        var.append(temp)
        add=(record.price*record.quantity)+add
    print("vendor is",Vendor,Date)
    today=datetime.date.today()
    return render(request,'store/billing_purchase.html',{"msg3":var,"details":details,"total":add,"today":today})

@authorized_user
def vendor_sales(request,vendor,date):
    entries = ""
    entries = Sales.objects.filter(vendor=vendor).filter(date=date)
    details = entries[0]
    var=[]
    add=float()
    t=float()
    cgst=float()
    sgst=float()
    for record in entries:
        temp=dict()
        temp['product']=record.product
        temp['date']=record.date
        temp['price']=record.price
        temp['quantity']=record.quantity
        temp['hsn']=record.hsn
        temp['gst_no']=record.gst_no
        temp['gst_rate']=record.gst_rate
        temp['total']=round(record.price*record.quantity,2)
        var.append(temp)
        # cgst=(temp['total']*(temp['gst_rate']/2))/100+cgst
        cgst=(record.price*record.quantity)*((record.gst_rate)/2)/100+cgst
        add=(record.price*record.quantity)+add
        sgst=cgst
        t=add+cgst+sgst
        t=round(t,2)
    v1=[]
    v2=[]
    for r in entries:
        h=int(r.hsn)
        hsum=0
        if h not in v2:
            hsn_entries=Sales.objects.filter(vendor=vendor).filter(date=date).filter(hsn=h)
            for r1 in hsn_entries:
                hsum=hsum+(r1.price*r1.quantity)*((r1.gst_rate)/2)/100
            d=dict()
            d['hsn']=h
            d['hsum']=hsum
            v1.append(d)
        v2.append(h)
    # unique = [used.append(x) for x in v1 if x.get("hsn") not in used]
    # used = set( val for dic in v1 for val in dic.values())
    # used=[]
    # for i in v1:
    #     if i.get("hsn") not in i.values():
    #         used.append(i)
    print(v1)
    # print(used)
    today=datetime.date.today()
    products=Stock.objects.all()
    global invoice_no
    invoice_no=invoice_no+1
    return render(request,'store/billing_sales.html/',{"msg3":var,"Vendor":vendor,"Date":date,"total":add,"details":details,"today":today,"products":products,"invoice_no":invoice_no,"cgst":cgst,"t":t,"v1":v1})

@authorized_user
def billing_sales(request):
    if request.method == "POST":
        Product_id = request.POST['product_id']
        Vendor = request.POST['vendor']
        Quantity = request.POST['quantity']
        Price = request.POST['price']
        Date = request.POST['date']
        Gst_rate = request.POST['gst_rate']
        form = salesform(request.POST)
        if int(Quantity) <= Stock.objects.get(pno=Product_id).quantity:
            pass
        else:
            g="you dont have enough stock"
            entries = ""
            entries = Sales.objects.filter(vendor=Vendor).filter(date=Date)
            print("vendor is",Vendor,Date)
            var=[]
            add=float()
            t=float()
            cgst=float()
            sgst=float()
            details = entries[0]
            for record in entries:
                temp=dict()
                temp['product']=record.product
                temp['date']=record.date
                temp['price']=record.price
                temp['hsn']=record.hsn
                temp['gst_no']=record.gst_no
                temp['gst_rate']=record.gst_rate
                temp['quantity']=record.quantity
                temp['total']=record.price*record.quantity
                var.append(temp)
                cgst=(record.price*record.quantity)*((record.gst_rate)/2)/100+cgst
                add=(record.price*record.quantity)+add
                sgst=cgst
                t=add+cgst+sgst
                t=round(t,2)
                add=(record.price*record.quantity)+add
            v1=[]
            v2=[]
            for r in entries:
                h=int(r.hsn)
                hsum=0
                if h not in v2:
                    hsn_entries=Sales.objects.filter(vendor=vendor).filter(date=date).filter(hsn=h)
                    for r1 in hsn_entries:
                        hsum=hsum+(r1.price*r1.quantity)*((r1.gst_rate)/2)/100
                        d=dict()
                        d['hsn']=h
                        d['hsum']=hsum
                        v1.append(d)
                v2.append(h)
            # used = []
            # unique = [used.append(x) for x in v1 if x not in used]
            today=datetime.date.today()
            global invoice_no
            invoice_no=invoice_no+1
            return render(request,'store/billing_sales.html/',{"msg3":var,"total":add,"details":details,"today":today,"invoice_no":invoice_no,"g":g,"cgst":cgst,"t":t,"v1":v1})
        if form.is_valid():
            new_five = form.save(commit=False)
            new_five.product = Stock.objects.get(pno=Product_id).product
            new_five.hsn = Stock.objects.get(pno=Product_id).hsn
            new_five.save()
            a="your form is saved"
        else:
            p=form.errors
            return render(request,'store/billing_sales.html/',{"a":p})
    entries = ""
    entries = Sales.objects.filter(vendor=Vendor).filter(date=Date)
    print("vendor is",Vendor,Date)
    var=[]
    add=float()
    t=float()
    cgst=float()
    sgst=float()
    details = entries[0]
    for record in entries:
        temp=dict()
        temp['product']=record.product
        temp['date']=record.date
        temp['price']=record.price
        temp['hsn']=record.hsn
        temp['gst_no']=record.gst_no
        temp['gst_rate']=record.gst_rate
        temp['quantity']=record.quantity
        temp['total']=record.price*record.quantity
        var.append(temp)
        cgst=(record.price*record.quantity)*((record.gst_rate)/2)/100+cgst
        add=(record.price*record.quantity)+add
        sgst=cgst
        t=add+cgst+sgst
        t=round(t,2)
        add=(record.price*record.quantity)+add
    v1=[]
    v2=[]
    for r in entries:
        h=int(r.hsn)
        hsum=0
        if h not in v2:
            hsn_entries=Sales.objects.filter(vendor=vendor).filter(date=date).filter(hsn=h)
            for r1 in hsn_entries:
                hsum=hsum+(r1.price*r1.quantity)*((r1.gst_rate)/2)/100
                d=dict()
                d['hsn']=h
                d['hsum']=hsum
                v1.append(d)
        v2.append(h)
    # used = []
    # unique = [used.append(x) for x in v1 if x not in used]
    today=datetime.date.today()
    invoice_no=invoice_no+1
    return render(request,'store/billing_sales.html/',{"msg3":var,"total":add,"details":details,"today":today,"invoice_no":invoice_no,"cgst":cgst,"t":t,"v1":v1})

@authorized_user
def history(request):
    return render(request,'store/history.html')

@authorized_user
def summary(request):
    stock=Stock.objects.all().values('product').distinct()
    var=[]
    for row in stock:
        temp=dict()
        add=0
        prod=row.get("product")
        all_products=Stock.objects.filter(product=prod)
        temp['product']=prod
        temp['pno']=all_products[0].pno
        for r in all_products:
            add=add+r.quantity
        temp['add']=add
        var.append(temp)
    # stock1=Purchase.objects.all().values('product').distinct()
    # var1=[]
    # for row1 in stock1:
    #     temp1=dict()
    #     add1=0
    #     prod1=row1.get("product")
    #     all_products1=Purchase.objects.filter(product=prod1)
    #     temp1['product']=prod1
    #     temp1['purchase_no']=all_products1[0].purchase_no
    #     for r1 in all_products1:
    #         add1=add1 + r.quantity
    #     temp1['add']=add1
    #     var1.append(temp1)
    return render(request,'store/summary.html',{"msg":var})

@authorized_user
def history_show(request):
    # entry_sales=Sales.objects.filter(date=date)
    # entry_purchase=Purchase.objects.filter(date=date)
    if request.method =="POST":
        Start=request.POST['start']
        Last=request.POST['last']
    St=Start
    Lt=Last
    Start=Start.split("-")
    # Start=str(Start)
    Start="/".join(Start)
    Start=datetime.datetime.strptime(Start,'%Y/%m/%d')
    Last=Last.split("-")
    # Start=str(Start)
    Last="/".join(Last)
    Last=datetime.datetime.strptime(Last,'%Y/%m/%d')
    print(Last.strftime)
    entry_sales=Sales.objects.filter(date__range=[Start,Last]).order_by('-date')
    print(entry_sales)
    entry_purchase=Purchase.objects.filter(date__range=[Start,Last]).order_by('-date')
    return render(request,'store/history_show.html',{"msg1":entry_purchase,"msg2":entry_sales,"Start":St,"Last":Lt})

@authorized_user
def logout_view(request):
    response = HttpResponseRedirect('/admin-se/loginform/')
    response.delete_cookie('username')
    return response

@authorized_user
def image(request,pno):
    p=Purchase.objects.get(purchase_no=pno)
    return render(request,'store/image.html',{"r":p})

@authorized_user
def download_sales(request):
    response=HttpResponse(content_type='text/csv')
    
    if request.method =="POST":
        Start=request.POST['start']
        Last=request.POST['last']
    print("start date is",Start)
    print("start date is",Last)
    Start=Start.split("-")
    # Start=str(Start)
    Start="/".join(Start)
    Start=datetime.datetime.strptime(Start,'%Y/%m/%d')
    Last=Last.split("-")
    # Start=str(Start)
    Last="/".join(Last)
    Last=datetime.datetime.strptime(Last,'%Y/%m/%d')
    entry_sales=Sales.objects.filter(date__range=[Start,Last])
    entry_purchase=Purchase.objects.filter(date__range=[Start,Last])
    writer=csv.writer(response)
    writer.writerow(['sales_no','product','vendor','quantity','price','date','gst_no','gst_rate','address'])
    for row in entry_sales:
        writer.writerow([row.sales_no,row.product,row.vendor,row.quantity,row.price,row.date,row.gst_no,row.gst_rate,row.address])
    response['Content-Disposition']='attachment; filename= "member.csv"'
    print("sales is")
    return response

@authorized_user
def download_purchase(request):
    response=HttpResponse(content_type='text/csv')
    if request.method =="POST":
        Start=request.POST['start']
        Last=request.POST['last']
    print("start date is",Start)
    print("start date is",Last)
    Start=Start.split("-")
    # Start=str(Start)
    Start="/".join(Start)
    Start=datetime.datetime.strptime(Start,'%Y/%m/%d')
    Last=Last.split("-")
    # Start=str(Start)
    Last="/".join(Last)
    Last=datetime.datetime.strptime(Last,'%Y/%m/%d')
    entry_purchase=Purchase.objects.filter(date__range=[Start,Last])
    writer=csv.writer(response)
    writer.writerow(['purchase_no','product','vendor','quantity','price','date','gst'])
    for row in entry_purchase:
        writer.writerow([row.purchase_no,row.product,row.vendor,row.quantity,row.price,row.date,row.gst])
    response['Content-Disposition']='attachment; filename= "member.csv"'
    print("purchase is")
    return response