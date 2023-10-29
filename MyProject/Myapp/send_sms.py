from twilio.rest import Client
import random
import os
from twilio.rest import Client
from django.core.mail import send_mail
from django.conf import settings

class OtpVerificationClass:
    
    otp=random.randint(10000,99999)
        
            
    def Send_Otp_Function(self,mobile):
        account_sid = 'ACc38be9ab4ce7266de3b06142e9f135a0'
        auth_token = '159e710ff73b793b756b1a73b59c0d8c'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'Welcome to Sasta Bazzar\nHere is your OTP - {self.otp}',
        to=f'whatsapp:+91{mobile}'
        )

        print(message.sid)
    
    def Send_Mobile_Otp(self,mobile):
        # Download the helper library from https://www.twilio.com/docs/python/install
        
        # Set environment variables for your credentials
        # Read more at http://twil.io/secure
        account_sid = "ACf501fc8c6eb285443fccb0dd7b85c8cc"
        auth_token = os.environ["a151e3431ab4213217118bd1a8cf0278"]
        verify_sid = "VA378fdaf348434ba94024e5384068ff15"
        verified_number = "+918291660633"

        client = Client(account_sid, auth_token)

        verification = client.verify.v2.services(verify_sid) \
        .verifications \
        .create(to=verified_number, channel="sms")
        print(verification.status)

        otp_code = input("Please enter the OTP:")

        verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=otp_code)
        print(verification_check.status)
        
    def Email_verification(self,email):
        subject = 'Email OTP Verification Mail'
        message = f'Welcome Seller, thank you for registering as Vendor in Sasta Bazar.\nYour OTP-{self.otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        
    def Email_verification2(self,email):
        subject = 'Welcome To Sasta Bazzar Seller Service'
        message = 'Hello Seller,\nThis is our pleasure that you became part of Sasta Bazzar\nWe Welcome you from our gratitude.\nstart your Product with us and start Selling the Product\n\nThanks and Regards,\nSasta Bazzar\n\n\n\n***This is Auto-Generated mail please Do not reply***'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )