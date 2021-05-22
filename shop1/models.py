from django.db import models


# Create your models here.


class slide(models.Model):
    title = models.CharField('title', max_length=100)
    stitle = models.CharField('stitle', max_length=120)
    simg = models.ImageField(upload_to="shop1/images", default="")

    def __str__(self):
        return self.title


class order(models.Model):
    proid = models.CharField("proid", max_length=50, default="")
    oid = models.AutoField(primary_key=True)
    fname = models.CharField("fname",  max_length=100)
    mobile_no = models.CharField("mobile_no", max_length=50)
    address = models.CharField("address", max_length=200)
    pin = models.IntegerField("pin", default="")
    hno = models.CharField("hno", max_length=50)
    city = models.CharField("city", max_length=50)
    ostat = models.CharField("ostat", max_length=50, default="processing")
    alt_no = models.CharField("alt_no", max_length=50)
    qnt = models.CharField("qnt", max_length=50, default="")

    color = models.CharField("color", max_length=50, null=True, blank=True)
    size = models.CharField("size", max_length=50, null=True, blank=True)

    def __str__(self):
        return self.ostat


class product(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField("pname", max_length=70)
    price = models.IntegerField("price")
    dicount = models.CharField("dicount", max_length=50)
    sdesc = models.CharField("sdesc", max_length=300)
    desc = models.CharField("desc", max_length=1000)
    chat = models.CharField("chat", max_length=50)
    subchat = models.CharField("subchat", max_length=50)
    pimg = models.ImageField(upload_to="shop1/images", default="")
    pimg2 = models.ImageField(upload_to="shop1/images", default=1)
    pimg3 = models.ImageField(upload_to="shop1/images", default=1)

    color = models.CharField("color", max_length=50, null=True, blank=True)
    size = models.CharField("size", max_length=50, null=True, blank=True)

    is_argumented = models.CharField("is_argumented", max_length=3, default="no")

    def __str__(self):
        return self.pname

