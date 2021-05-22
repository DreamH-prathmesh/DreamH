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


    # product pages

    # LADIES WEAR
    path("saree", views.saree, name="saree"),
    path("kurti", views.kurti, name="kurti"),
    path("top", views.top, name="top"),
    path("pant_shirt", views.lpant_shirt, name="pant_shirt"),
    path("jeans", views.ljeans, name="jeans"),
    path("tshirt", views.ltshirt, name="tshirt"),
    path("workout", views.lworkout, name="lworkout"),
    path("other", views.lother, name="other"),

    # means wear

    path("mshirt", views.mshirt, name="mshirt"),
    path("mtshirt", views.mtshirt, name="mtshirt"),
    path("mpant", views.mpant, name="mpant"),
    path("minnerwear", views.minnerwear, name="minnerwear"),
    path("mother", views.mother, name="mother"),
    path("mworkout", views.mworkout, name="mworkout"),

    # foot wears

    path("mens_footwear", views.mens_footwear, name="mens-footwear"),
    path("ladies_footwear", views.ladies_footwear, name="ladies-footwear"),
    path("m_other_footwear", views.m_other_footwear, name="mens-footwear"),

    # fashion

    path("mens_fashion", views.mens_fashion, name="mens-fashion"),
    path("ladies_fashion", views.ladies_fashion, name="ladies-fashion"),
    path("other_fashion", views.other_fashion, name="mens-fashion"),
    
    # Ai

    path("arg", views.arg, name="arg")




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
