from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    email=models.EmailField(unique= True)
    password=models.CharField(max_length= 20)
    otp=models.IntegerField(default= 459)
    is_active=models.BooleanField(default= True)
    is_verfied=models.BooleanField(default= False)
    role=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add= True,blank= False)
    updated_at=models.DateTimeField(auto_now_add= True,blank= False)

class Doctor(models.Model):
    user_id=models.ForeignKey(User,on_delete= models.CASCADE)
    DoctorFullName=models.CharField(max_length=50)
    ClinicName=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100,blank= True)
    Experience=models.CharField(max_length=100,blank= True)
    speciality=models.CharField(max_length=100)
    Countrycode=models.CharField(max_length=30,blank= True)
    mobile=models.CharField(max_length=13)
    address=models.CharField(max_length=500,blank= True)
    city=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    birthdate=models.DateTimeField()
    profile_pic=models.ImageField(upload_to='image/',default='doc_male.png')
    Appointmentfees=models.CharField(max_length=50,blank= True)
    Biography=models.CharField(max_length=500,blank= True)
    state=models.CharField(max_length=50,blank= True)
    country=models.CharField(max_length=50,blank= True)
    postalcode=models.IntegerField(default= True)
    college=models.CharField(max_length=50,blank= True)
    YearofCompletion=models.CharField(max_length=50,blank= True)
   
    
class Patient(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    BloodGroup=models.CharField(max_length=10)
    Countrycode=models.CharField(max_length=30,blank= True)
    mobile = models.CharField(max_length = 13)
    address = models.CharField(max_length= 500, blank = True)
    city = models.CharField(max_length = 50)
    gender = models.CharField(max_length= 10)
    birthdate = models.DateField()
    profile_pic=models.ImageField(upload_to='image/',default='doc_male.png')
    state=models.CharField(max_length=50,blank= True)
    postalcode=models.IntegerField(default= True)
    country=models.CharField(max_length=50,blank= True)
  
class Pharma(models.Model):
    user_id=models.ForeignKey(User,on_delete= models.CASCADE)
    PharmaName=models.CharField(max_length=50)
    FullName=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100,blank= True)
    InstitutionTrainning=models.CharField(max_length=100,blank= True)
    speciality=models.CharField(max_length=100)
    Countrycode=models.CharField(max_length=30,blank= True)
    mobile=models.CharField(max_length=13)
    address=models.CharField(max_length=500,blank= True)
    city=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    birthdate=models.DateTimeField()
    profile_pic=models.ImageField(upload_to='image/',default='doc_male.png')
    
# class book_appointment(models.Model):
#     Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE,default=1)
#     Doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE,default=1)
#     Sunday = models.CharField(max_length=50)
#     Symtoms = models.CharField(max_length=50)
#     appointment_status = models.CharField(max_length=100,default = 'Pending')


class scheduletime(models.Model):
    Doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE,default=1)
    Opentime = models.IntegerField()
    Closetime = models.IntegerField()
    Day = models.CharField(max_length=50,blank=True)
    Openmeridiem = models.CharField(max_length=10,blank=True)
    Closemeridiem = models.CharField(max_length=10,blank=True)
    Date = models.CharField(max_length=50,blank=True)
class book_appointment(models.Model):
    Doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE,default=1)
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE,default=1)
    Day = models.CharField(max_length=50,blank= True)
    Time = models.CharField(max_length=50,blank= True)
    Symtoms = models.CharField(max_length=50,blank= True)
    appointment_status = models.CharField(max_length=100,default = 'Pending')
    Date = models.CharField(max_length=50,blank=True)

class allreviews(models.Model):
    Doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE,default=1)
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE,default=1)
    Title=models.CharField(max_length=500,blank=True)
    reviews=models.CharField(max_length=500,blank=True)
    
class comment(models.Model):
    Doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE,default=1)
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE,default=1)
    review_id =models.ForeignKey(allreviews,on_delete=models.CASCADE,default=1)
    content=models.CharField(max_length=50,blank= False)
    created_at=models.DateTimeField(auto_now_add= True,blank= False)
class blog(models.Model):
    Doctor_id =models.ForeignKey(Doctor,on_delete=models.CASCADE,default=1)
    Patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE,default=1)
    Blog=models.CharField(max_length=5000,blank=True)
    Title=models.CharField(max_length=500,blank=True)
    created_at=models.DateTimeField(auto_now_add= True,blank= False)



    





    