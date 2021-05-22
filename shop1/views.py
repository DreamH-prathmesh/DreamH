from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect

from django.templatetags.static import static

# Create your views here.
from .models import slide, product
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import os

def home(request):
    # SLIDER
    im = slide.objects.all()[0]
    im2 = slide.objects.all()[1]
    im3 = slide.objects.all()[2]

    # 6 PRODUCTS

    pr = product.objects.filter(
        Q(chat__icontains="top-product") | Q(subchat="top-product")).order_by('pid')[:6]

    prm = product.objects.filter(
        Q(chat__icontains="men") | Q(subchat="men")).order_by('-pid')[:6]

    prl = product.objects.filter(
        Q(chat__icontains="ladies") | Q(subchat="ladies")).order_by('-pid')[:6]

    prf = product.objects.filter(
        Q(chat__icontains="foot") | Q(subchat="foot")).order_by('-pid')[:6]

    prfs = product.objects.filter(
        Q(chat__icontains="fashion") | Q(subchat="fashion")).order_by('-pid')[:6]

    # SHOW MORE
    prma = product.objects.filter(
        Q(chat__icontains="men") | Q(subchat="men")).order_by('-pid')[6:36]

    prla = product.objects.filter(
        Q(chat__icontains="ladies") | Q(subchat="ladies")).order_by('-pid')[6:36]

    prfa = product.objects.filter(
        Q(chat__icontains="footwear") | Q(subchat="footwear")).order_by('-pid')[6:36]

    prfsa = product.objects.filter(
        Q(chat__icontains="fashion") | Q(subchat="fashion")).order_by('-pid')[6:36]

    # /SHOW MORE

    arg = product.objects.filter(is_argumented="yes")

    data = {
        'im': im, 
        'im2': im2, 
        'im3': im3, 
        'pr': pr, 
        'prl': prl, 
        'prm': prm, 
        'prf': prf, 
        'prfs': prfs, 
        'prma': prma, 
        'prla': prla, 
        "prfa": prfa, 
        "prfsa": prfsa,
        'arg':arg
        }

    return render(request, "home.html", data)


def search(request):
    if request.method == "POST":
        search = request.POST['search']
        if search:
            pr = product.objects.filter(
                Q(pname__icontains=search) | Q(desc__icontains=search))

            if pr:
                return render(request, "searchr.html", {'pr': pr})
            else:
                return render(request, "snothing.html")

        # sk = request.POST.get('search')
        else:
            return HttpResponseRedirect('search')

            # return render(request, "snothing.html")
    return HttpResponseRedirect('search')


def showprod(request, pid):
    # fetch prod using id
    prod = product.objects.filter(pid=pid)

    return render(request, "showprod.html", {'prod': prod[0]})


def test2(request, pid):
    prod = product.objects.filter(pid=pid)
    return render(request, "test2.html", {'prod': prod[0]})


def order(request, pid):
    # prod.product.objects.filter(pid=pid)
    prod = product.objects.filter(pid=pid)

    return render(request, "order.html", {'prod': prod[0]})


def upload(request):
    if request.method == "POST":
        name = request.POST.get('fname')
        no = request.POST.get('mobile_no')
        add = request.POST.get('address')
        pinc = request.POST.get('pin')
        cit = request.POST.get('city')
        hno = request.POST.get('hno')
        ano = request.POST.get('alt_no')
        quentity = request.POST.get('quentity')
        color = request.POST.get('color')
        size = request.POST.get('size')
        id = request.POST.get('pid')

        from .models import order

        ord = order(fname=name, mobile_no=no, address=add, pin=pinc,
                    hno=hno, city=cit, alt_no=ano, qnt=quentity, proid=id, color=color, size=size)
        ord.save()


        return HttpResponseRedirect('successpro')

    else:
        return render(request, "error.html")

    return HttpResponseRedirect('successpro')


def successpro(request):
    from .models import order

    prod = order.objects.last()

    return render(request, "successpro.html", {'prod': prod})


def track(request):
    '''  if request.method == "POST":
          tid = request.POST.get('tid')
          from .models import order
          tr = order.objects.filter(oid=tid)
          print(tr)

          return render(request, "track.html", {'tr': tr})
      '''
    return render(request, "track.html")


def tracked(request):
    if request.method == "POST":
        try:
            tid = request.POST.get('tid')
            tphone = request.POST.get('tphone')
            from .models import order
            prod = order.objects.filter(oid=tid, mobile_no=tphone)

            return render(request, "tracked.html", {'prod': prod[0]})
        except:
            return render(request, "error.html")
    else:
        return render(request, "error.html")

    return render(request, "tracked.html")

    '''pr=product.objects.all()[0:20]

    print(pr)

    if request.method=="POST":
        name=request.POST.get('tname')
        price=request.POST.get('tprice')
        from .models import test
        print(name)
        ord=test(tname=name,tprice=price)
        ord.save() '''
   # pro = Variation.objects.last()

    return render(request, "test.html")


# ladies wear

def saree(request):
    prm = product.objects.filter(
        Q(chat__icontains="saree") | Q(subchat="saree")).order_by('-pid')

    return render(request, "ladies/lsari.html", {'prm': prm})


def kurti(request):
    prm = product.objects.filter(
        Q(chat__icontains="kurti") | Q(subchat="kurti")).order_by('-pid')

    return render(request, "ladies/lkurti.html", {'prm': prm})


def top(request):
    prm = product.objects.filter(
        Q(chat__icontains="top") | Q(subchat="top")).order_by('-pid')

    return render(request, "ladies/ltop.html", {'prm': prm})


def lpant_shirt(request):
    prm = product.objects.filter(
        Q(chat__icontains="ladies-pantshirt") | Q(subchat="ladies-pantshirt")).order_by('-pid')

    return render(request, "ladies/lpantshirt.html", {'prm': prm})


def ljeans(request):
    prm = product.objects.filter(
        Q(chat__icontains="ladies-jeans") | Q(subchat="ladies-jeans")).order_by('-pid')

    return render(request, "ladies/ljens.html", {'prm': prm})


def ltshirt(request):
    prm = product.objects.filter(
        Q(chat__icontains="ladies-tshirt") | Q(subchat="ladies-tshirt")).order_by('-pid')

    return render(request, "ladies/lt-shirt.html", {'prm': prm})


def lworkout(request):
    prm = product.objects.filter(
        Q(chat__icontains="ladies-workout") | Q(subchat="ladies-workout")).order_by('-pid')

    return render(request, "ladies/lworkout.html", {'prm': prm})


def lother(request):
    prm = product.objects.filter(
        Q(chat__icontains="ladies-other") | Q(subchat="ladies-other")).order_by('-pid')

    return render(request, "ladies/lother.html", {'prm': prm})

# means wear


def mshirt(request):
    prm = product.objects.filter(
        Q(chat__icontains="mens-shirt") | Q(subchat="mens-shirt")).order_by('-pid')

    return render(request, "mens/mshirt.html", {'prm': prm})


def mtshirt(request):
    prm = product.objects.filter(
        Q(chat__icontains="mens-tshirt") | Q(subchat="mens-tshirt")).order_by('-pid')

    return render(request, "mens/mtshirt.html", {'prm': prm})


def mpant(request):
    prm = product.objects.filter(
        Q(chat__icontains="mens-pant") | Q(subchat="mens-pant")).order_by('-pid')

    return render(request, "mens/mpant.html", {'prm': prm})


def minnerwear(request):
    prm = product.objects.filter(
        Q(chat__icontains="mens-innerwear") | Q(subchat="mens-innerwear")).order_by('-pid')

    return render(request, "mens/minnerwear.html", {'prm': prm})


def mother(request):
    prm = product.objects.filter(
        Q(chat__icontains="mens-other") | Q(subchat="mens-other")).order_by('-pid')

    return render(request, "mens/mother.html", {'prm': prm})


def mworkout(request):
    prm = product.objects.filter(
        Q(chat__icontains="mens-workout") | Q(subchat="mens-workout")).order_by('-pid')

    return render(request, "mens/mworkout.html", {'prm': prm})

# foot wear


def mens_footwear(request):
    prm = product.objects.filter(
        Q(chat__icontains="mens-footwear") | Q(subchat="mens-footwear")).order_by('-pid')

    return render(request, "footwear/mens_footwear.html", {'prm': prm})


def ladies_footwear(request):
    prm = product.objects.filter(
        Q(chat__icontains="ladies-footwear") | Q(subchat="ladies-footwear")).order_by('-pid')

    return render(request, "footwear/ladies_footwear.html", {'prm': prm})


def m_other_footwear(request):
    prm = product.objects.filter(
        Q(chat__icontains="m-other-footwear") | Q(subchat="m-other-footwear")).order_by('-pid')

    return render(request, "footwear/m_other_footwear.html", {'prm': prm})

# fashion


def mens_fashion(request):
    prm = product.objects.filter(
        Q(chat__icontains="mens-fashion") | Q(subchat="mens-fashion")).order_by('-pid')

    return render(request, "fashion/men_fashion.html", {'prm': prm})


def ladies_fashion(request):
    prm = product.objects.filter(
        Q(chat__icontains="ladies-fashion") | Q(subchat="ladies-fashion")).order_by('-pid')

    return render(request, "fashion/ladies_fashion.html", {'prm': prm})


def other_fashion(request):
    prm = product.objects.filter(
        Q(chat__icontains="other-fashion") | Q(subchat="other-fashion")).order_by('-pid')

    return render(request, "fashion/other_fashion.html", {'prm': prm})


def arg(request):
    
    os.system('python statics/ImageAugmentation.py')
    
    return HttpResponse("wait")
