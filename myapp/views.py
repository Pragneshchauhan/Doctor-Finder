from django.shortcuts import render, HttpResponse
from .models import *
from random import randint
from django.urls import reverse
from datetime import datetime, timedelta, date
from django.http import HttpResponseRedirect
from django.db.models import Q
from . import utils
from django.core.mail import send_mail
from django.utils.html import strip_tags
           



# Create your views here.

def visitpage(request):
    doctor=Doctor.objects.all()
    return render(request,"app/visitpage.html",{'doctor':doctor})
def searchresult(request):
    query = request.GET['query']
    all_doctor  = Doctor.objects.filter(Q(DoctorFullName__icontains=query) |
                                        Q(ClinicName__icontains=query) |
                                        Q(speciality__icontains=query)|
                                        Q(city=query))
    return render(request,"app/searchresult.html",{'all_doctor':all_doctor})
# def patientdashboard(request):
#     if 'email' in request.session and "role" in request.session:
#         if request.session['role'] == "patient":
#             query = request.GET['query']
#             patient = Patient.objects.get(user_id=request.session['id'])

#             all_doctor  = Doctor.objects.filter(Q(DoctorFullName__icontains=query) |
#                                                 Q(ClinicName__icontains=query) |
#                                                 Q(speciality__icontains=query)|
#                                                 Q(city=query))
            
#             return render(request,"app/patientdashboard.html",{'all_doctor':all_doctor, 'patientss':patient})
#         else:
#             all_patients = Patient.objects.filter()
#             all_doctors = Doctor.objects.all()
#             return render(request, 'app/patientdashboard.html', {'all_patients': all_patients,'patientss':patient, 'all_doctors': all_doctors})
#     else:
#         return HttpResponseRedirect(reverse('login')) 


    
    
   
  

def loginpage(request):
    return render(request,"app/login.html")
def regpage(request):
    return render(request,"app/register.html")
def patientdashboard(request):
    return render(request,"app/patientdashboard.html")
def favourites(request):
    return render(request,"app/favourites.html")
def doctorprofile(request,pk):
    doctor=Doctor.objects.get(pk=pk)
    reviews = allreviews.objects.filter(Doctor_id=doctor)
    comments=comment.objects.filter(Doctor_id=doctor)
    return render(request,"app/doctor-profile.html",{'doctor1':doctor,'reviews':reviews,'comments':comments})

def chat(request):
    return render(request,"app/chat.html")
def profilesetting(request):
    return render(request,"app/profilesettings.html")
def changepassword(request):
    return render(request,"app/changepassword.html")
def doctorregister(request):
    return render(request,"app/doctor-register.html")
def Pharmaregistration(request):
    return render(request,"app/Pharmacy-registration.html")
def showdata(request):
    all_details = User.objects.all()
    return render(request,"app/showdata.html",{'details':all_details})
def search(request):
    return render(request,"app/search.html")
def calendar(request):
    return render(request,'app/calendar.html')
def patientbookhistory(request):
    patients = Patient.objects.get(user_id=request.session['id'])

    return render(request,'app/patient-bookhistory.html',{'patients':patients})


def speciality(request):
    speciality=Doctor.objects.filter(speciality='Cardiologist')
    return render(request,'app/speciality.html',{'speciality':speciality})

def Surgeon(request):
    Surgeon=Doctor.objects.filter(speciality='Surgeon')
    return render(request,'app/speciality.html',{'Surgeon':Surgeon})

def Radiologist(request):
    Radiologist=Doctor.objects.filter(speciality='Radiologist')
    return render(request,'app/speciality.html',{'Radiologist':Radiologist})

def Cardiologist1(request):
    Cardiologist=Doctor.objects.filter(speciality='Cardiologist')
    return render(request,'app/speciality1.html',{'Cardiologist':Cardiologist})
def Surgeon1(request):
    Surgeon=Doctor.objects.filter(speciality='Surgeon')
    return render(request,'app/speciality1.html',{'Surgeon':Surgeon})
def Radiologist1(request):
    Radiologist=Doctor.objects.filter(speciality='Radiologist')
    return render(request,'app/speciality1.html',{'Radiologist':Radiologist})
def Email(request,pk):
    user = User.objects.get(pk=pk)
    user.is_verfied = True
    user.save()
    return HttpResponseRedirect(reverse('varificationpage'))
def emailpatient(request,pk):
    user = User.objects.get(pk=pk)
    user.is_verfied = True
    user.save()
    return HttpResponseRedirect(reverse('varificationpage'))
def varificationpage(request,pk):
    return render(request,'app/varification.html',{'pk':pk})
def varification(request,pk):
    
    if request.method == "POST":
        print("\n\n===",request.POST.get('OTP'))
        otp = request.POST['OTP']
        user = User.objects.get(pk=pk)
        print(user,type(user.otp),type(otp))
        if user.otp == int(otp):
            print("=====1=====")
            user.is_verfied = True
            user.save()
            return HttpResponseRedirect(reverse('login'))
    return render(request,'app/varification.html',{'pk':pk})

def registeruser(request):
    try:
        if request.POST['role'] == 'doctor':
            role = request.POST['role']
            doctorFullName = request.POST['DoctorFullName']
            clinicName = request.POST['ClinicName']
            password = request.POST['password']
            confirmpassword = request.POST['conformpassword']
            gender = request.POST['gender']
            email = request.POST['email']
            speciality = request.POST['speciality']
            experience = request.POST['experience']
            qualification = request.POST['qualification']
            address = request.POST['address']
            dateofbirth = request.POST['birthdate']
            city = request.POST['city']
            Countrycode = request.POST['countrycode']
            mobile = str(request.POST['mobile'])
            image=request.FILES['image']
            

            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request,'app/doctor-register.html', {'message': message})
            else:
                if password == confirmpassword:
                    print('===========3==========')
                    otp = randint(10000,999999)
                    newuser = User.objects.create(email=email, password=password, role=role, otp=otp)
                    newdoctor = Doctor.objects.create(user_id=newuser, DoctorFullName=doctorFullName, ClinicName=clinicName, gender=gender, speciality=speciality,Experience=experience,qualification=qualification,address=address, birthdate=dateofbirth, city=city, mobile=mobile,profile_pic=image,)
                    print('===========4==========')
                    utils.Email(doctorFullName,password,otp,email,newuser.pk)
                    print(otp)
                    return render(request,'app/varification.html' , {'pk':newuser.pk})
                else:
                    print("========= 5 ========")
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app/doctor-register.html', {'message': message})
                # if password == confirmpassword:
                #     otp = randint(10000,999999)
                #     newuser = User.objects.create(email=email, password=password, role=role, otp=otp)
                #     newdoctor = Doctor.objects.create(user_id=newuser, DoctorFullName=doctorFullName, ClinicName=clinicName, gender=gender, speciality=speciality,Experience=experience,qualification=qualification,address=address, birthdate=dateofbirth, city=city, mobile=mobile,Countrycode=Countrycode,profile_pic=image,)
                #     return render(request,'app/login.html')
                # else:
                #     message = "Password and confirm password doesn't match"
                #     return render(request, 'app/doctor-register.html', {'message': message})
        else:
            if request.POST['role'] == 'patient':
                role = request.POST['role']
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                password = request.POST['password']
                confirmpassword = request.POST['confirmpassword']
                bloodgroup=request.POST['bloodgroup']
                gender = request.POST['gender']
                email = request.POST['email']
                address=request.POST['address']
                dateofbirth = request.POST['birthdate']
                city = request.POST['city']
                countrycode=request.POST['countrycode']
                mobile = str(request.POST['phone'])
                image=request.FILES['image']
                
                user = User.objects.filter(email=email)
                if user:
                    message = 'This email already exists'
                    return render(request, 'app/register.html', {'message': message})
                else:
                    if password == confirmpassword:
                        otp = randint(100000, 9999999)
                        newuser = User.objects.create(email=email, password=password, role=role, otp=otp)
                        newpatient = Patient.objects.create(user_id=newuser, firstname=firstname, lastname=lastname, gender=gender,BloodGroup=bloodgroup, city=city,address=address, mobile=mobile, Countrycode=countrycode,birthdate=dateofbirth,profile_pic=image)
                        utils.emailpatient(firstname,lastname,password,otp,email,newuser.pk)
                        print(otp)
                        return render(request,'app/varification.html' , {'pk':newuser.pk})
                    else:
                        message = "Password and confirm password doesn't match"
                        return render(request,'app/register.html', {'message': message})
    
                # if request.POST['role'] == 'pharma':
                #     role = request.POST['role']
                #     pharmaname = request.POST['pharmaname']
                #     fullname = request.POST['fullname']
                #     password = request.POST['password']
                #     confirmpassword = request.POST['confirmpassword']
                #     speciality = request.POST['speciality']
                #     institution = request.POST['institution']
                #     qualification = request.POST['qualification']
                #     gender = request.POST['gender']
                #     email = request.POST['email']
                #     address=request.POST['address']
                #     dateofbirth = request.POST['birthdate']
                #     city = request.POST['city']
                #     countrycode=request.POST['countrycode']
                #     mobile = str(request.POST['phone'])
                #     image=request.FILES['image']

                #     user = User.objects.filter(email=email)
                #     if user:
                #         message = 'This email already exists'
                #         return render(request, 'app/register.html', {'message': message})
                #     else:
                #         if password == confirmpassword:
                #             otp = randint(100000, 9999999)
                #             newuser = User.objects.create(email=email, password=password, role=role, otp=otp)
                #             newPharma = Pharma.objects.create(user_id=newuser, PharmaName=pharmaname, FullName=fullname, gender=gender,qualification=qualification,InstitutionTrainning=institution, city=city,address=address, mobile=mobile, Countrycode=countrycode,birthdate=dateofbirth,profile_pic=image)
                #             return render(request,'app/login.html')
                #         else:
                #             message = "Password and confirm password doesn't match"
                #             return render(request,'app/register.html', {'message': message})

    except User.DoesNotExist:
        return render(request, 'app/register.html', {'message': message})
def loginuser(request):

    if request.POST['role'] == 'doctor':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print(user)
        print("role")
        if user[0]:
            if user[0].password == password and user[0].role == 'doctor':
                doctor = Doctor.objects.filter(user_id=user[0])
                request.session['email'] = user[0].email
                request.session['DoctorFullName'] = doctor[0].DoctorFullName
                request.session['role'] = user[0].role
                request.session['id'] = user[0].id

               # request.session['profile_pic']=doctor[0].profile_pic
                print("----------> Profile pic-->", doctor[0].profile_pic.url)
                

                return HttpResponseRedirect(reverse('doctordashboard'))
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "app/login.html", {'message': message})
    
    if request.POST['role'] == 'patient':
        
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print("User------------------------------->",user)
        if user[0]:
            if user[0].password == password and user[0].role == 'patient':
                patient = Patient.objects.filter(user_id=user[0])
                request.session['email'] = user[0].email
                request.session['firstname'] = patient[0].firstname
                request.session['role'] = user[0].role
                request.session['id'] = user[0].id
                return HttpResponseRedirect(reverse('patienthomepage'))
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "app/login.html", {'message': message})

    if request.POST['role'] == 'pharma':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        print(user)
        print("role")
        if user:
            if user.password == password and user.role == 'pharma':
                pharma = Pharma.objects.get(user_id=user)
                request.session['email'] = user.email
                request.session['PharmaName'] = pharma.PharmaName
                request.session['role'] = user.role
                request.session['id'] = user.id

               # request.session['profile_pic']=doctor[0].profile_pic
                print("----------> Profile pic-->", pharma.profile_pic.url)
                

                return HttpResponseRedirect(reverse('ShowDoctor'))
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "app/login.html", {'message': message})
def patienthomepage(request):
    if 'email' in request.session and "role" in request.session:
        if request.session['role'] == "patient":
            all_doctor  = Doctor.objects.all()
            patient = Patient.objects.get(user_id=request.session['id'])
            return render(request,"app/patient-homepage.html",{'all_doctor':all_doctor,'patientss':patient})
        else:
            all_patients = Patient.objects.all()
            all_doctors = Doctor.objects.all()
            patient = Patient.objects.get(user_id=request.session['id'])
            return render(request, 'app/patient-homepage.html', {'all_patients': all_patients, 'patientss':patient,'all_doctors': all_doctors})
    else:
        return HttpResponseRedirect(reverse('login'))
def appointmentlist(request):
    patient = Patient.objects.get(user_id=request.session['id'])
    appointment=book_appointment.objects.filter(Patient_id=patient)
    return render(request,'app/appointmentlist.html',{'appointment':appointment,'patient':patient})            

def patientdashboard(request):
    if 'email' in request.session and "role" in request.session:
        if request.session['role'] == "patient":
            query = request.GET['query']
            patient = Patient.objects.get(user_id=request.session['id'])

            all_doctor  = Doctor.objects.filter(Q(DoctorFullName__icontains=query) |
                                                Q(ClinicName__icontains=query) |
                                                Q(speciality__icontains=query)|
                                                Q(city=query))
            
            return render(request,"app/patientdashboard.html",{'all_doctor':all_doctor, 'patientss':patient})
        else:
            all_patients = Patient.objects.filter()
            all_doctors = Doctor.objects.all()
            return render(request, 'app/patientdashboard.html', {'all_patients': all_patients,'patientss':patient, 'all_doctors': all_doctors})
    else:
        return HttpResponseRedirect(reverse('login'))  

def bookingpage(request,pk):
    
    doctor = Doctor.objects.get(pk=pk)
    Sun_slot = scheduletime.objects.filter(Day='Sunday',Doctor_id=doctor )
    Mon_slot = scheduletime.objects.filter(Day='Monday',Doctor_id=doctor)
    Tue_slot = scheduletime.objects.filter(Day='Tuesday',Doctor_id=doctor)
    Wed_slot = scheduletime.objects.filter(Day='Wednesday',Doctor_id=doctor)
    Thur_slot = scheduletime.objects.filter(Day='Thursday',Doctor_id=doctor)
    Fri_slot = scheduletime.objects.filter(Day='Friday',Doctor_id=doctor)
    Sat_slot = scheduletime.objects.filter(Day='Saturday',Doctor_id=doctor)
    
    # return HttpResponse(sundate[0].Date)

    sun=[]
    if Sun_slot:
        for t in range(len(Sun_slot)): 
            for i in range(Sun_slot[t].Opentime,Sun_slot[t].Closetime+1):
                sun.append(i)
    mon=[]
    if Mon_slot:
        for t in range(len(Mon_slot)):
            for i in range(Mon_slot[t].Opentime,Mon_slot[t].Closetime+1):
                mon.append(i)
            
    tue=[]
    if Tue_slot:
        for t in range(len(Tue_slot)):
            for i in range(Tue_slot[t].Opentime,Tue_slot[t].Closetime+1):
                tue.append(i)
    wed=[]
    if Wed_slot:
        for t in range(len(Wed_slot)):
            for i in range(Wed_slot[t].Opentime,Wed_slot[t].Closetime+1):
                wed.append(i)
    th=[]
    if Thur_slot:
        for t in range(len(Thur_slot)):
            for i in range(Thur_slot[t].Opentime,Thur_slot[t].Closetime+1):
                th.append(i)
    fri=[]
    if Fri_slot:
        for t in range(len(Fri_slot)):
            for i in range(Fri_slot[t].Opentime,Fri_slot[t].Closetime+1):
                fri.append(i)
    sat=[]
    if Sat_slot:
        for t in range(len(Sat_slot)):
            for i in range(Sat_slot[t].Opentime,Sat_slot[t].Closetime+1):
                sat.append(i)
    return render(request,"app/booking1.html",{'doctors':doctor,'sun':sun,'mon':mon,'tue':tue,'wed':wed,'th':th,'fri':fri,'sat':sat,'Sun_slot':Sun_slot[0] if Sun_slot else None,'Mon_slot':Mon_slot[0] if Mon_slot else None,'Tue_slot':Tue_slot[0] if Tue_slot else None,'Wed_slot':Wed_slot[0] if Wed_slot else None,'Thur_slot':Thur_slot[0] if Thur_slot else None,'Fri_slot':Fri_slot[0] if Fri_slot else None,'Sat_slot':Sat_slot[0] if Sat_slot else None})
def bookappoint(request,pk):
    doctor = Doctor.objects.get(pk=pk)
    patient = Patient.objects.get(user_id=request.session['id'])
    day = request.POST['day']
    time = request.POST['time']
    date = request.POST['date']
  
    newbook = book_appointment.objects.create(
        Day = day,
        Time = time ,
        Doctor_id = doctor,
        Patient_id = patient,
        Date = date
    )
    booking = book_appointment.objects.filter(Patient_id=patient)
    return render(request,"app/patient-bookhistory.html",{'booking_appo':booking,'patient':patient})
    

# def booking_appointment(request,pk):
#     sunday=request.POST['sn']
#     email=request.POST['em']
#     patient = Patient.objects.get(user_id=request.session['id'])
#     doctor = Doctor.objects.get(pk=pk)
#     newbooking =book_appointment.objects.create(
#         Patient_id = patient,
#         Doctor_id = doctor,
#         Sunday = sunday
       
#     )
#     booking = book_appointment.objects.all()
    
#     return render(request,'app/patient-bookhistory.html')

def doctordashboard(request):
    doctor = Doctor.objects.get(user_id=request.session['id'])
    booking = book_appointment.objects.filter(Doctor_id=doctor)
    return render(request,"app/doctordashboard.html",{'booking':booking,'doct':doctor,'total_booking':len(booking)})

def appointment_stutusA(request,pk):
    print("\n\n================ Appointment Status=========")
    patient = book_appointment.objects.get(pk=pk)
    print(patient)
    patient.appointment_status = "Accept"
    # print(booking_id)
    patient.save()
    return HttpResponseRedirect(reverse('doctordashboard'))

def appointment_stutusR(request,pk):
    print("\n\n================ Appointment Status=========")
    patient = book_appointment.objects.get(pk=pk)
    print(patient)
    patient.appointment_status = "Rejected"
    # print(booking_id)
    patient.save()
    return HttpResponseRedirect(reverse('doctordashboard'))

def appointments(request):
    return render(request,'app/booking1.html')
def schedule(request):
    doctor = Doctor.objects.get(user_id=request.session['id'])
    Sun_slot = scheduletime.objects.filter(Day='Sunday',Doctor_id=doctor )
    Mon_slot = scheduletime.objects.filter(Day='Monday',Doctor_id=doctor)
    Tue_slot = scheduletime.objects.filter(Day='Tuesday',Doctor_id=doctor)
    Wed_slot = scheduletime.objects.filter(Day='Wednesday',Doctor_id=doctor)
    Thur_slot = scheduletime.objects.filter(Day='Thursday',Doctor_id=doctor)
    Fri_slot = scheduletime.objects.filter(Day='Friday',Doctor_id=doctor)
    Sat_slot = scheduletime.objects.filter(Day='Saturday',Doctor_id=doctor)
    return render(request,"app/schedule-timings.html",{'Sun_slot':Sun_slot,'Mon_slot':Mon_slot,'Tue_slot':Tue_slot,'Wed_slot':Wed_slot,'Thur_slot':Thur_slot,'Fri_slot':Fri_slot,'Sat_slot':Sat_slot,'docto':doctor})
def schedule_timing(request):
    doctor_id = Doctor.objects.get(user_id=request.session['id'])
    openat = request.POST['openat']
    closeat = request.POST['closeat']
    day = request.POST['day']
    date = request.POST['date']
    
    new_slot = scheduletime.objects.create(
        Doctor_id=doctor_id,
        Opentime = openat,
        Closetime = closeat,
        Day = day,
        Date = date
        
    )
    
    return HttpResponseRedirect(reverse(schedule))

def mypatient(request):
    doctor = Doctor.objects.get(user_id=request.session['id'])
    mypatients = book_appointment.objects.filter(Doctor_id = doctor)
    return render(request,'app/my-patients.html',{'mypatient':mypatients})
# def booksuccess(request,pk):
#     return render(request,'app/booking-success.html')





def patientprofilesettings(request):
    patientprofile = Patient.objects.get(user_id = request.session['id'])
    return render(request,'app/patientprofile-settings.html',{'patientprofile':patientprofile})

def edit_user(request):
    existuser=Patient.objects.get(user_id = request.session['id'])
    existuser.firstname=request.POST['fname']
    existuser.lastname=request.POST['lname']
    existuser.birthdate=request.POST['dob']
    existuser.BloodGroup=request.POST['bloodgroup']
    existuser.mobile=request.POST['mobile']
    existuser.address=request.POST['address']
    existuser.city=request.POST['city']
    existuser.state=request.POST['state']
    existuser.postalcode=request.POST['zipcode']
    existuser.country=request.POST['country']
    existuser.save()
    return HttpResponseRedirect(reverse('patientprofilesettings'))



def doctorprofilesettings(request):
    doctorprofile = Doctor.objects.get(user_id = request.session['id'])
    return render(request,'app/doctorprofile-settings.html',{'doctorprofile':doctorprofile})
    
def edit_doctorprofile(request):
    existuser=Doctor.objects.get(user_id =request.session['id'])
    existuser.DoctorFullName=request.POST['dname']
    existuser.mobile=request.POST['mobile']
    existuser.gender=request.POST['gender']
    existuser.ClinicName=request.POST['ClinicName']
    existuser.address=request.POST['address']
    existuser.city=request.POST['city']
    existuser.Appointmentfees=request.POST['fees']
    existuser.Biography=request.POST['bio']
    existuser.state=request.POST['state']
    existuser.country=request.POST['contry']
    existuser.postalcode=request.POST['postalcode']
    existuser.qualification=request.POST['degree']
    existuser.college=request.POST['college']
    existuser.YearofCompletion=request.POST['year']
    existuser.birthdate=request.POST['dob']
    existuser.save()
    return HttpResponseRedirect(reverse('doctorprofilesettings'))
  
def ds_appointments(request):
    doctor = Doctor.objects.get(user_id=request.session['id'])
    appointment = book_appointment.objects.filter(Doctor_id=doctor)
    return render(request,'app/ds_appointments .html',{'docts':doctor,'appointmentsss':appointment})
def ds_mypatients(request):
    doctor = Doctor.objects.get(user_id=request.session['id'])
    mypatients=book_appointment.objects.filter(Doctor_id=doctor)
    return render(request,'app/ds_my-patients .html',{'doctmypa':doctor,'mypatients':mypatients})


def reviews(request):
    doctor = Doctor.objects.get(user_id=request.session['id'])
    myreview=allreviews.objects.filter(Doctor_id=doctor)
    return render(request,'app/reviews.html',{'doctor':doctor,'myreview':myreview})
def doctorchangepassword(request):
    doctor = Doctor.objects.get(user_id=request.session['id'])
    return render(request,'app/doctor-change-password.html',{'doctor':doctor})


def admin_appointment(request):
    all_appointments = book_appointment.objects.all()
    return render(request,"admin/admin_appointment-list.html",{'all_appointmentss':all_appointments})
def admin_specialities(request):
    doctor =Doctor.objects.all()
    return render(request,"admin/admin_specialities.html",{'doctor':doctor})
def admin_doctor(request):
    doctor=Doctor.objects.all()
    all_appointments=book_appointment.objects.all()
    return render(request,"admin/admin_doctor-list.html",{'doctor':doctor,'all_appointments':all_appointments})
def admin_patient(request):
    patient=Patient.objects.all()
    book=book_appointment.objects.all()
    return render(request,"admin/admin_patient-list.html",{'patient':patient,'book':book})
def admin_reviews(request):
    review=allreviews.objects.all()
    return render(request,"admin/admin_reviews.html",{'review':review})
def admin_transactions(request):
    return render(request,"admin/admin_transactions-list.html")
def admin_settings(request):
    return render(request,"admin/admin_settings.html")
def admin_invoice(request):
    return render(request,"admin/admin_invoice-report.html")
def reportgen(request):
    print("\n\n====",request.GET.get('startdate'),type(request.GET.get('startdate')))
    print("\n\n====",request.GET.get('enddate'),type(request.GET.get('enddate')))
    date_str=request.GET['startdate']
    date_string=request.GET['enddate']
    startdate = datetime.strptime(date_str,"%Y-%m-%d").date()
    enddate = datetime.strptime(date_string,"%Y-%m-%d").date()
    
    print(date)
    appointments  = book_appointment.objects.filter(Q(Date__range=[str(startdate),str(enddate)]))
    return render(request,"admin/admin_invoice-report.html",{'appointments':appointments})
def delete_report(request,pk):
    delete_u=book_appointment.objects.get(pk=pk)
    delete_u.delete()
    return HttpResponseRedirect(reverse('admin_invoice'))
def admin_login(request):
    return render(request,"admin/admin_login.html")
def admin_register(request):
    return render(request,"admin/admin_register.html")
def admin_forgotpassword(request):
    return render(request,"admin/admin_forgot-password.html")
def admin_dashboard(request):
    patient= Patient.objects.all()
    doctor= Doctor.objects.all()
    all_appointments = book_appointment.objects.all()
    review = allreviews.objects.all()
    print("\n\n========",doctor,"\n\n")
    print("\n\n========",patient,"\n\n")
    print("\n\n========",all_appointments,"\n\n")
    print("\n\n========",review,"\n\n")

    return render(request,"admin/admin_dashboard.html",{'patient':patient,'doctor':doctor,'review':review,'total_review':len(review),'total_doctors':len(doctor),'total_patients':len(patient),'all_appointments':all_appointments,'total_appointment':len(all_appointments)})
def admin_lockscreen(request):
    return render(request,"admin/admin_lock-screen.html")
def error404(request):
    return render(request,"admin/error-404.html")
def admin_error500(request):
    return render(request,"admin/admin_error-500.html")
def blankpage(request):
    return render(request,"admin/blank-page.html")
def components(request):
    return render(request,"admin/components.html")
def form_basicinput(request):
    return render(request,"admin/form-basic-inputs.html")
def form_inputgroup(request):
    return render(request,"admin/form-input-groups.html")
def form_horizontal(request):
    return render(request,"admin/form-horizontal.html")
def form_vertical(request):
    return render(request,"admin/form-vertical.html")
def adminlogin(request):
    if request.POST['email'] == 'doctorfinder7@gmail.com':
        if request.POST['password'] == 'doctorfinder77':
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.filter(email=email)
            print(user)
            print("role")

            return HttpResponseRedirect(reverse('admin_dashboard'))
        else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "admin/admin_login.html")
    else:
        message = "user doesn't exist"
        return render(request, "admin/admin_login.html")
def doctor_profile1(request,pk):
    doctor=Doctor.objects.get(pk=pk)
    return render(request,"app/doctor-profile1.html",{'docts':doctor})
def review(request,pk):
    review = request.POST['review']
    # print("\n\n====",review)
    title = request.POST['title']
    patient = Patient.objects.get(user_id=request.session['id'])
    doctor = Doctor.objects.get(pk=pk)
    
    add_review = allreviews.objects.create(
        Title = title,
        reviews = review,
        Doctor_id = doctor,
        Patient_id = patient,
        
        
    )
    all_review = allreviews.objects.all()
   
    return render(request,'app/doctor-profile1.html',{'all_review':all_review,'docts':doctor,'patient':patient})

def logout(request):
    del request.session['email']
    del request.session['role']
    # del request.session['firstname']
    return HttpResponseRedirect(reverse('login'))

def doctors(request):
    doctor=Doctor.objects.all()
    return render(request,"app/doctors.html",{'doctor':doctor})
def doctors1(request):
    doctors=Doctor.objects.all()
    return render(request,"app/doctors1.html",{'doctors':doctors})
def specia(request):
    doctor=Doctor.objects.all()
    return render(request,"app/specia.html",{'doctor':doctor})
def specia1(request):
    doctor=Doctor.objects.all()
    return render(request,"app/specia1.html",{'doctor':doctor})

#changepassword
def changepassword(request):
    id = request.session['id']
    user = User.objects.get(id=id)

    old_password = user.password

    current = request.POST['current']
    new_password = request.POST['new_password']
    confirm = request.POST['confirm']

    if old_password == current and new_password == confirm:
        user.password = confirm
        user.save()
        message = "Your Password have been changed successfully!"
        return render(request, "app/doctor-change-password.html",{'message':message})
    else:
        error_msg = "Incorrect Password , Try Again  !!"
        return render(request, "app/doctor-change-password.html", {'error_msg': error_msg})
# chnagepassword
def patientchngpwdpage(request):
    patientchangepas = Patient.objects.get(user_id = request.session['id'])

    return render(request,"app/patient-change-pass.html",{'patientchangepas':patientchangepas})
def patientchangepas(request):
    id = request.session['id']
    user = User.objects.get(id=id)

    old_password = user.password

    current = request.POST['current']
    new_password = request.POST['new_password']
    confirm = request.POST['confirm']

    if old_password == current and new_password == confirm:
        user.password = confirm
        user.save()
        message = "Your Password have been changed successfully!"
        return render(request, "app/patient-change-pass.html",{'message':message})
    else:
        error_msg = "Incorrect Password , Try Again  !!"
        return render(request, "app/patient-change-pass.html", {'error_msg': error_msg})
# changepassword
# forgotpassword
def forgotpass(request):
    return render(request,'app/forgot-password.html')
def forgotPassword(request):
    email = request.POST['email']
    try:
        user = User.objects.get(email=email)
        if user:
            if user.email == email:
                otp = randint(100000, 9999999)
                user.otp = otp
                utils.forgotPassword(otp,email,user.pk)
                user.save()
                email_subject = "This is your new OTP"
                print("\n== UTILS ===")
                return render(request, 'app/forgetpwdvarification.html', {'email': email,'pk':user.pk})
            else:
                message = 'This email does not match'
                print(message)
                return render(request, "app/forgot-password.html", {'message': message})
        else:
            message = 'This email is not available'
            print(message)
            return render(request, "app/forgot-password.html", {'message': message})
    except:
        message = 'This email is not available'
        return render(request, "app/forgot-password.html", {'message': message})
        # newuser = User.objects.create(email=email, password=password, role=role, otp=otp)
        #             newdoctor = Doctor.objects.create(user_id=newuser, DoctorFullName=doctorFullName, ClinicName=clinicName, gender=gender, speciality=speciality,Experience=experience,qualification=qualification,address=address, birthdate=dateofbirth, city=city, mobile=mobile,profile_pic=image,)
        #             print('===========4==========')
        #             utils.Email(doctorFullName,password,otp,email,newuser.pk)
        #             print(otp)
        #             return render(request,'app/varification.html' , {'pk':newuser.pk})
def forgetpwdvarification(request,pk):
    return render(request,'app/forgetpwdvarification.html',{'pk':pk})

def forgetvarification(request,pk):
    if request.method == "POST":
        print("\n\n===",request.POST.get('OTP'))
        otp = request.POST['OTP']
        user = User.objects.get(pk=pk)
        print(user,type(user.otp),type(otp))
        if user.otp == int(otp):
            print("=====1=====")
            user.save()
            return render(request,'app/forgot-changepwd.html',{'pk':pk})
    return render(request,'app/forgetpwdvarification.html',{'pk':pk})
def forgotchangepwdpage(request,pk):
    return render(request,'app/forgot-changepwd.html',{'pk':pk})
def forgotchangepwd(request,pk):
    
    user = User.objects.get(pk=pk)

    
    new_password = request.POST['new_password']
    confirm = request.POST['confirm']

    if  new_password == confirm:
        user.password = confirm
        user.save()
        message = "Your Password have been changed successfully!"
        return render(request, "app/login.html",{'message':message})
    else:
        error_msg = "Incorrect Password , Try Again  !!"
        return render(request, "app/forgot-changepwd.html", {'error_msg': error_msg})

def delete_details(request,pk):
    delete_user=allreviews.objects.get(pk=pk)
    delete_user.delete()
    return HttpResponseRedirect(reverse('admin_reviews'))
def delete_user(request,pk):
    delete_u=Doctor.objects.get(pk=pk)
    delete_u.delete()
    return HttpResponseRedirect(reverse('admin_doctor'))
def delete_patient(request,pk):
    delete_u=Patient.objects.get(pk=pk)
    delete_u.delete()
    return HttpResponseRedirect(reverse('admin_patient-list'))


def reportpage(request):
    return render(request,"admin/report.html")
# def reportgen(request):
#     print("\n\n====",request.GET.get('startdate'),type(request.GET.get('startdate')))
#     print("\n\n====",request.GET.get('enddate'),type(request.GET.get('enddate')))
#     date_str=request.GET['startdate']
#     date_string=request.GET['enddate']
#     startdate = datetime.strptime(date_str,"%Y-%m-%d").date()
#     enddate = datetime.strptime(date_string,"%Y-%m-%d").date()
    
#     print(date)
#     appointments  = book_appointment.objects.filter(Q(Date__range=[str(startdate),str(enddate)]))
#     return render(request,"admin/report.html",{'appointments':appointments})
# def reportgen(request):
#     print("\n\n====",request.GET.get('date'),type(request.GET.get('date')))
#     date_str=request.GET['date']
#     date = datetime.strptime(date_str,"%Y-%m-%d").date()
#     print(date)
#     appointments  = book_appointment.objects.filter(Q(Date__icontains=date))
#     return render(request,"admin/report.html",{'appointments':appointments})

def adminpro(request):
    return render(request,"admin/admin_profile.html")


def bloggrid(request):
    return render(request,'app/blog-grid.html')

# def doctor_profile1(request,pk):
#     doctor=Doctor.objects.get(pk=pk)
#     allreview=allreviews.objects.filter(Doctor_id=doctor)
#     comments=comment.objects.filter(Doctor_id=doctor)

#     print("\n\n======== Reviews ========")
#     # print("All Review >> ",allreview)
#     for r in allreview:
#         print("\nTitle===",r.reviews)
#         for c in comments:
#             if r == c.review_id:
#                 print("\tCommnet : ",c.content)
#     # print("Comments >>",comments)
#     print("================\n\n")
    # return render(request,"app/doctor-profile1.html",{'allreview':allreview,'comments':comments,'docts':doctor})
def review(request,pk):
    review = request.POST['review']
    print("\n\n====",review)
    patient = Patient.objects.get(user_id=request.session['id'])
    doctor = Doctor.objects.get(pk=pk)
    add_review = allreviews.objects.create(
        
        reviews = review,
        Doctor_id = doctor,
        Patient_id = patient,
        
    )
    allreview=allreviews.objects.filter(Doctor_id=doctor)
    comments=comment.objects.filter(Doctor_id=doctor)

    print("\n\n======== Reviews ========")
    # print("All Review >> ",allreview)
    for r in allreview:
        print("\nTitle===",r.reviews)
        for c in comments:
            if r == c.review_id:
                print("\tCommnet : ",c.content)
    # print("Comments >>",comments)
    print("================\n\n")
   
    return render(request,'app/doctor-profile1.html',{'allreview':allreview,'comments':comments,'docts':doctor})
def reply(request,pk):
    review_id=allreviews.objects.get(pk=pk)
    doctor = review_id.Doctor_id
    patient = Patient.objects.get(user_id=request.session['id'])
    print("\n\n======",doctor)
    content=request.POST['content']
    newpost=comment.objects.create(content=content,review_id=review_id,Doctor_id = doctor,Patient_id = patient)
    allreview=allreviews.objects.filter(Doctor_id=doctor)
    # comments=comment.objects.filter(review_id=review_id)
    comments=comment.objects.filter(Doctor_id=doctor)
    # {% if allreview.id == comments.review_id  %}
    print("\n\n======== Reviews ========")
    # print("All Review >> ",allreview)
    for r in allreview:
        print("\nTitle===",r.reviews)
        for c in comments:
            if r == c.review_id:
                print("\tCommnet : ",c.content)
    # print("Comments >>",comments)
    print("================\n\n")
    return render(request,'app/doctor-profile1.html',{'allreview':allreview,'comments':comments,'docts':doctor})

def reviews(request):
    doctor = Doctor.objects.get(user_id=request.session['id'])
    allreview=allreviews.objects.filter(Doctor_id=doctor)
    comments=comment.objects.filter(Doctor_id=doctor)

    print("\n\n======== Reviews ========")
    # print("All Review >> ",allreview)
    for r in allreview:
        print("\nTitle===",r.reviews)
        for c in comments:
            if r == c.review_id:
                print("\tCommnet : ",c.content)
    # print("Comments >>",comments)
    print("================\n\n")
    return render(request,'app/reviews.html',{'doctor':doctor,'allreview':allreview,'comments':comments})
    
def docreply(request,pk):
    review_id=allreviews.objects.get(pk=pk)
    patient = review_id.Patient_id
    print("\n\n======",patient)
    doctor = Doctor.objects.get(user_id=request.session['id'])
    print("\n\n======",doctor)
    content=request.POST['content']
    newpost=comment.objects.create(content=content,review_id=review_id,Doctor_id = doctor,Patient_id = patient)
    allreview=allreviews.objects.filter(Doctor_id=doctor)
    # comments=comment.objects.filter(review_id=review_id)
    comments=comment.objects.filter(Doctor_id=doctor)
    # {% if allreview.id == comments.review_id  %}
    print("\n\n======== Reviews ========")
    # print("All Review >> ",allreview)
    for r in allreview:
        print("\nTitle===",r.reviews)
        for c in comments:
            if r == c.review_id:
                print("\tCommnet : ",c.content)
    # print("Comments >>",comments)
    print("================\n\n")
    return render(request,'app/reviews.html',{'allreview':allreview,'comments':comments,'doctor':doctor})




