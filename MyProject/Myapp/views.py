from django.shortcuts import render,redirect
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from .models import ProductInformation,MobileVerificationNumber,SellerInformation,SellerBuinsessInformation,UserInformation,ProductOrder
import re
from . send_sms import OtpVerificationClass
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import random
        

def index(request):
    print(request.user)
    Seller_Info=SellerInformation.objects.filter(Primary_key=request.user).values()
    print(Seller_Info)
    UserInfo=UserInformation.objects.filter(EmailId=request.user).values()
    print(UserInfo)
    if UserInfo.__len__()==0:
        return redirect('SellerProfile')
    else:
        userInfo2=UserInformation.objects.filter(EmailId=request.user).values()
        print(userInfo2[0]['VendorImage'])
    productOrder=ProductOrder.objects.all().values()
    return render(request,"index.html",{"Seller":Seller_Info,"userinfo":userInfo2,"orders":productOrder})

def Product(request):
    product_list=ProductInformation.objects.filter(Primary_key=request.user).values()
    
    return render(request,"pages/forms/Product.html",{"list":product_list})

def AddProduct(request):
    if request.method=="POST":
        pName=request.POST['productName']
        pPrice=request.POST['productPrice']
        pDescription=request.POST['productDescription']
        pImage=request.FILES['images']
        PnameSection=pName[0].upper()+pName[1].upper()+pPrice                
        productid="P{}".format(PnameSection)
        print(productid)
        pInformation=ProductInformation(ProductId=productid,ProductName=pName,ProductDesc=pDescription,ProductImage=pImage,ProductPrice=pPrice,Primary_key=request.user)
        pInformation.save()
        return redirect('Product_Section')
    return render(request,"pages/forms/AddProduct.html")


def LogInPage(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user_auth=authenticate(username=email,password=password)
        print(user_auth)
        if user_auth is not None:
            login(request,user_auth)
            return redirect('VendorHome')
        else:
            messages.warning(request,'Incorrect Username or Password !!')
        
    return render(request,"pages/samples/login.html")

def MobileVerificationPage(request): 
    if request.method=="POST":
       mobile=request.POST["email"]
    #    mobile2=int(mobile)
       if mobile:
           lst=[]
           Mobile_verification=MobileVerificationNumber.objects.all().values()
           for i in Mobile_verification:
               lst.append(i['MobileNumber'])
        #    true_Check=MobileVerificationNumber.objects.filter('MobileNumber').values()
        #    print(true_Check)
           if mobile not in lst:
                Temp_Mobile_Save=MobileVerificationNumber(MobileNumber=mobile,verified=False)
                Temp_Mobile_Save.save()        
                # mobile3=str(mobile2)
                obj=OtpVerificationClass()
                obj.Email_verification(mobile)
                return redirect('MobileVerificationSection')
           else:
               messages.warning(request,"You Already have Account Please Sign In")
       else:
           messages.warning(request,"Please Enter Correct Mobile Number !!")
    return render(request,"pages/samples/Mobile.html")

def MobileOtpVerification(request):
    MobileOtpData=MobileVerificationNumber.objects.filter(verified=False).values()
    if request.method=="POST":
        I1=request.POST['I1']
        I2=request.POST['I2']
        I3=request.POST['I3']
        I4=request.POST['I4']
        I5=request.POST['I5']
        I6=I1+I2+I3+I4+I5
        obj2=OtpVerificationClass()
        if I6==str(obj2.otp):
            sanve_test=MobileVerificationNumber(MobileNumber=MobileOtpData[0]['MobileNumber'],verified=True)
            sanve_test.save()
            save_test2=MobileVerificationNumber.objects.filter(MobileNumber=MobileOtpData[0]['MobileNumber'],verified=False).delete()
            dataFetching=MobileVerificationNumber.objects.filter(verified=True).values()
            # Need to change the logic, it is not appropriate for huge cutomer    
            encMessage=(dataFetching[0]['MobileNumber'])
            url='Vendor-Information/{}'.format(encMessage)
            return HttpResponseRedirect(url)
        else:
            messages.error(request,"Incorrect Otp Entered !!")       
    return render(request,'pages/samples/Otp.html',{'Mobile':MobileOtpData})


def VendorOtherDetail(request,id):
    Main_section=MobileVerificationNumber.objects.filter(MobileNumber=id).values()
    if request.method=="POST":
        name=request.POST['Fname']
        Date=request.POST['Date']
        date1=Date[0:4]+Date[5:7]+Date[8:10]
        date2=int(date1)
        Current_Date=date.today()
        typeConversion=str(Current_Date)
        data=typeConversion[0:4]+typeConversion[5:7]+typeConversion[8:10]
        Current_date=int(data)

        if not re.findall('\d',name):
            if date2<Current_date:
                print(Main_section)
                Seller_Info=SellerInformation(SellerName=name,DOB=Date,Primary_key=Main_section[0]['MobileNumber'])
                Seller_Info.save()
                url='{}/Business-Information/'.format(Main_section[0]['MobileNumber'])
                return HttpResponseRedirect(url)
            else:
                messages.warning(request,f"Your Date Of Birth can't be {date.today()}")
        else:
            messages.warning(request,"Name can not Contain number or Special Character, Please Enter the Correct Name !!") 
    return render(request,'pages/samples/OtherDetail.html')

def FinalRegistration(request,id):
    print(id)
    if request.method=="POST":
        name=request.POST['Fname']
        Gst=request.POST['Date']
        password=request.POST['Password']
        
        if not re.findall('\d',name):
            if not (re.findall('\d',password) and len(password)>=10):
                messages.warning(request,'Password should Contain At least One Digit and length should be at least 10 character')
            else:
                Seller_Info2=SellerBuinsessInformation(BusinessName=name,GstNumber=Gst,Password=password,Primary_key=id)
                Seller_Info2.save()
                User_Registration=User.objects.create_user(username=id,password=password)
                User_Registration.save()
                obj=OtpVerificationClass()
                obj.Email_verification2(id)
                messages.success(request,"Registered Successfully !! Please Login !!")
                return redirect('LoginSection')      
        
    return render(request,"pages/samples/FinalRegistration.html")


def logOutSection(request):
    logout(request)
    return redirect('LoginSection')

def Profile(request):
    if request.method=="POST":
        VName=request.POST['VName']
        VAddress=request.POST['VAddress']
        BName=request.POST['BName']
        BAddress=request.POST['BAddress']
        BImage=request.FILES['Bimages']
        BMobile=request.POST['BMobile']
        BEmail=request.POST['BEmail']
        BGst=request.POST['BGst']
        userProfile=UserInformation(VendorName=VName,VendorAddress=VAddress,VendorImage=BImage,BusinessName=BName,BusinessAddress=BAddress,GstNumber=BGst,EmailId=BEmail,MobileNumber=BMobile)
        userProfile.save()
        return redirect('VendorHome')
    print(request.user)
    UserInfo=SellerInformation.objects.filter(Primary_key=request.user).values()
    print(UserInfo)
    print(request.user)
    BusinessInfo=SellerBuinsessInformation.objects.filter(Primary_key=request.user).values()
    print(BusinessInfo)
    user=UserInformation.objects.filter(EmailId=request.user).values()
    print(user)
    return render(request,"pages/forms/profile.html",{"user":UserInfo,"seller":BusinessInfo,"other":user})