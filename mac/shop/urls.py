from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path('checkout/handlerequest',views.handlerequest,name='HandleRequest'),
    path("signup", views.handleSignUp, name="Checkout"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    
]
