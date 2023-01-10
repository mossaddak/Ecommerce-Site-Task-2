from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('AllProducts/',views.AllProducts, name='AllProducts'),
    path('ProductDetails/<int:pk>/', views.ProductDetails, name="ProductDetails"),
    path('MyProducts/', views.MyProducts, name="MyProducts"),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('UpdateProduct/<int:pk>/', views.UpdateProduct, name="UpdateProduct"),
    path('DeleteProduct/<int:pk>/', views.DeleteProduct, name="DeleteProduct"),
    path('UserProductsForAdmin/', views.UserProductsForAdmin, name="UserProductsForAdmin"),
    path('AllUsers/', views.AllUsers, name="AllUsers"),
    path('UserProfile/<int:pk>/', views.SellerProfile, name="UserProfile"),
    path('ProfilePictureChngeForAdmin/<int:pk>/', views.ProfilePictureChngeForAdmin, name="ProfilePictureChngeForAdmin"),
    path('SpecificUsersProductForAdmin/<int:pk>/', views.SpecificUsersProductForAdmin, name="SpecificUsersProductForAdmin"),
    path('CategoryBasedProduct/<int:pk>/', views.CategoryBasedProduct, name="CategoryBasedProduct"),
    path('SearchProduct/', views.SearchProducts, name="SearchProduct"),

    #product order
    path('OrderProduct/<int:pk>/', views.productOrder, name="OrderProduct"),

    #product feedback
    path('ProductFeedBack/<int:pk>/', views.ProductFeedBack, name="ProductFeedBack"),
    path('UpdateFeedback/<int:pk>/', views.UpdateFeedback, name="UpdateFeedback"),
    path('DeleteFeedback/<int:pk>/', views.DeleteFeedback, name="DeleteFeedback"),

    #shopping cart
    path('ShoppingCart/<int:pk>/', views.ShoppingCart, name="ShoppingCart"),

    #my buy
    path("MyOrder/", views.MyOrder, name="MyOrder"),
    path("CustomerOrder/", views.CustomerOrder, name="CustomerOrder"),

    #order tracking
    path("OrderTracking/", views.OrderTracking, name="OrderTracking")

]
