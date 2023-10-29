from . import views;
from django.urls import path

urlpatterns = [
    path('Vendor-Transaction-Section/',views.index,name="VendorHome"),
    path('Product-catogory/',views.Product,name="Product_Section"),
    path('Add-Product/',views.AddProduct,name="ProudctAdd"),
    path('Vendor-Login/',views.LogInPage,name="LoginSection"),
    path('Mobile-Verification/',views.MobileVerificationPage,name="MobilePageSection"),
    path('Mobile-Verification/Mobile-Otp/',views.MobileOtpVerification,name="MobileVerificationSection"),
    path('Mobile-Verification/Mobile-Otp/Vendor-Information/<str:id>',views.VendorOtherDetail,name="VendorDetail"),
    path('Mobile-Verification/Mobile-Otp/Vendor-Information/<str:id>/Business-Information/',views.FinalRegistration,name="VendorBusinessDetail"),
    path("Vendor-logout/",views.logOutSection,name="logoutpage"),
    path("Seller-Profile/",views.Profile,name="SellerProfile")
    
]