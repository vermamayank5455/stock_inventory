from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.db.models.signals import pre_delete
from PIL import Image


# Create your models here.
class Stock(models.Model):
    pno=models.AutoField(primary_key=True)
    product=models.CharField(max_length=200)
    quantity=models.IntegerField(blank=True,null=True)
    hsn=models.IntegerField(blank=True,null=True)
  



class Purchase(models.Model):
    purchase_no=models.AutoField(primary_key=True)
    product_id=models.ForeignKey('Stock',on_delete=models.CASCADE,blank=True,null=True)
    product=models.CharField(max_length=200,blank=True,null=True)
    image=models.FileField(upload_to="images",blank=True,null=True)
    vendor=models.CharField(max_length=200)
    quantity=models.IntegerField()
    price=models.IntegerField()
    date=models.DateField(default=timezone.now)
    invoice_no=models.CharField(max_length=200,blank=True,null=True)
    gst=models.IntegerField(max_length=200,blank=True,null=True)


def create_Purchase(sender,instance,created,** kwargs):
    if created:
        print("purchase product_id is ",instance.product_id.pno)
        g=instance.product_id.pno
        l=instance.product_id.quantity
        q=Stock.objects.get(pno=g)
        print("new quantity is ",q.quantity)
        print("old quantity is ",l)
        q.quantity = q.quantity + l
        q.save()
        
        # instance.stock.save(update_fields['quantity'])
        print("stock created")

# def update_Purchase(sender,instance,created,** kwargs):
#     q=Stock.objects.get(pno=instance.product_id.pno)
#     q.quantity=instance.quantity
#     q.save()
#     print("stock updated")


# post_save.connect(update_Purchase,sender=Purchase)
post_save.connect(create_Purchase,sender=Purchase)


class Sales(models.Model):
    sales_no=models.AutoField(primary_key=True)
    product_id=models.ForeignKey('Stock',on_delete=models.CASCADE,blank=True,null=True)
    product=models.CharField(max_length=200,blank=True,null=True)
    vendor=models.CharField(max_length=200)
    quantity=models.IntegerField()
    price=models.IntegerField()
    date=models.DateField(default=timezone.now)
    gst_no=models.CharField(max_length=200,blank=True,null=True)
    gst_rate=models.IntegerField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    hsn=models.IntegerField(blank=True,null=True)

def create_Sales(sender,instance,** kwargs):
    g=instance.product_id.quantity
    print("new quantity is",g)
    q=Stock.objects.get(pno=instance.product_id.pno)
    print("old quantity is ",instance.quantity)
    print("stock quantity is ",q.quantity)
    q.quantity = q.quantity - instance.quantity
    q.save()


post_save.connect(create_Sales, sender=Sales)
