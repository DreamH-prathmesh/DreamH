from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect

from django.templatetags.static import static

# Create your views here.
from .models import slide, product
from .models import soffer,catgory,brand
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

    # # SHOW MORE
    # prma = product.objects.filter(
    #     Q(chat__icontains="men") | Q(subchat="men")).order_by('-pid')[6:36]

    # prla = product.objects.filter(
    #     Q(chat__icontains="ladies") | Q(subchat="ladies")).order_by('-pid')[6:36]

    # prfa = product.objects.filter(
    #     Q(chat__icontains="footwear") | Q(subchat="footwear")).order_by('-pid')[6:36]

    # prfsa = product.objects.filter(
    #     Q(chat__icontains="fashion") | Q(subchat="fashion")).order_by('-pid')[6:36]

    # # /SHOW MORE

    # arg = product.objects.filter(is_available="yes")
    
    bprice = product.objects.filter(Q(chat__icontains="best-price") | Q(subchat__icontains="best-price")).order_by('-pid')[:12]

    from .models import soffer,catgory,brand
    
    soffer = soffer.objects.all()
    
    catgory = catgory.objects.all()
    
    brand = brand.objects.all()
    
    data = {
        'im': im, 
        'im2': im2, 
        'im3': im3, 
        'pr': pr, 
        'prl': prl, 
        'prm': prm, 
        'prf': prf, 
        'prfs': prfs, 
        'bprice':bprice,
        
        'soffer':soffer,
        'catgory':catgory,
        'brand':brand,
    
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

# filter



def category(request,cname):
    

    products = product.objects.filter(
        Q(chat__icontains=cname) | Q(subchat__icontains=cname)).order_by('-pid')
    
    data = {
        'products':products,
    }
    
    return render(request, "filter/products.html", data)    
    
 

def products(request,cname):
    

    products = product.objects.filter(
        Q(chat__icontains=cname) | Q(subchat__icontains=cname)).order_by('-pid')
    
    data = {
        'products':products,
    }
    
    return render(request, "filter/products.html", data)    
    



def arg(request):
    
    os.system('python statics/ImageAugmentation.py')
    
    return HttpResponse("wait")
