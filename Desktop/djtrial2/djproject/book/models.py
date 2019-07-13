from django.db import models


class owner(models.Model):
    ownername=models.CharField('ownername',max_length=20,null=True)
    book_name=models.CharField('bookname',max_length=20,null=True)
    original_price=models.IntegerField('originalprice',null=True)
    selling_price=models.IntegerField('sellingprice',null=True)
    address=models.CharField('address',max_length=150,null=True)
    ph_num=models.IntegerField('phonenumber')
    bookpassword=models.CharField('bookpassword',max_length=20,null=True)
    verified=models.BooleanField(default=False)
# Create your models here.
