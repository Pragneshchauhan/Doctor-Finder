from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect

def Email(doctorFullName,password,otp,email,id):
    print("\n== UTILS ===")
    html_message='''
    <html>
    <body>
    <p>Welcome %s and pass is %s and %d</p>
    <p>http://127.0.0.1:8000/varificationpage/%d<p>
    </body>
    </html>
    '''%(doctorFullName,password,otp,id)
    plain_message =strip_tags(html_message)
    send_mail("my subjects",plain_message,'pragneshchauhan00798@gmail.com',[email],html_message=html_message)
def emailpatient(firstname,lastname,password,otp,email,id):
    print("\n== UTILS ===")
    html_message='''
    <html>
    <body>
    <p>Welcome %s %s and pass is %s and otp is %d</p>
    <p>http://127.0.0.1:8000/varificationpage/%d<p>
    </body>
    </html>
    '''%(firstname,lastname,password,otp,id)
    plain_message =strip_tags(html_message)
    send_mail("my subjects",plain_message,'pragneshchauhan00798@gmail.com',[email],html_message=html_message)

    
def forgotPassword(otp,email,id):
    email_subject = "This is your new OTP"
    print("\n== UTILS ===")
    html_message='''
    <html>
    <body>
    <p>Welcome %s Your Otp is %d </p>
    <p>http://127.0.0.1:8000/forgetpwdvarification/%d<p>
    </body>
    </html>
    '''%(email,otp,id)
    print(otp)
    plain_message =strip_tags(html_message)
    send_mail("my subjects",plain_message,'pragneshchauhan00798@gmail.com',[email],html_message=html_message)
    # return HttpResponseRedirect(reverse(login))
    # link = "https://localhost:8000/example?email="+email+"&otp="+otp+"&random="+random
    # send_mail(email_subject, 'mail_template','pragneshchauhan00798@gmail.com', [email], {'otp': otp})