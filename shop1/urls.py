from django.contrib import admin
from django.urls import path, include
from shop1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path("showprod/<int:pid>", views.showprod, name="showprod"),
    path("order/<int:pid>", views.order, name="order"),
    path("order/upload", views.upload),
    path("test2/<int:pid>", views.test2, name="test2"),
    path("order/successpro", views.successpro, name="successpro"),
    path("track", views.track, name="track"),
    path("tracked", views.tracked, name="tracked"),
    path("search", views.search, name="search"),
    path("showprod/search", views.search, name="search"),
    path("order/search", views.search, name="search"),
    
    # filter
    
    path("category/<str:cname>", views.category, name="category"),
    
    path("products/<str:cname>", views.products, name="products"),
    

    # product pages


    path("arg", views.arg, name="arg")




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
