import string
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from BreakdownAssist.models import Petrol_pump, Service_center, Tow_service, Mechanic, Feedback, Login, User, Request, \
    Chat, Rating


def login(request):
    return render(request,'logintemplate.html')
def loginpost(request):
    uname=request.POST["textfield"]
    pwd=request.POST["textfield2"]

    al=Login.objects.filter(Username=uname,Password=pwd)
    if al.exists():
        fs=Login.objects.get(Username=uname,Password=pwd)
        request.session['lid']=fs.id
        if fs.Type=='admin':
            return  HttpResponse("<script>alert('Welcome');window.location='/myapp/admin_home/'</script>")
        if fs.Type=='mechanic':
            return  HttpResponse("<script>alert('Welcome');window.location='/myapp/mechanic_home/'</script>")
        if fs.Type=='User':
            return  HttpResponse("<script>alert('Welcome');window.location='/myapp/user_home/'</script>")
    else:
        return HttpResponse("<script>alert('Invalid credentials');window.location='/myapp/login/'</script>")


def logout(request):

    request.session['lid'] = ""
    return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")


def admin_addpump(request):

    if request.session['lid']=='':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'admin/managepetrolpump/addpump.html')

def addpumppost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    pname=request.POST["textfield"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    district=request.POST["textfield4"]
    place=request.POST["textfield5"]
    post=request.POST["textfield6"]
    pin=request.POST["textfield7"]

    pp = Petrol_pump()
    pp.pump_name=pname
    pp.phone=phone
    pp.email=email
    pp.district=district
    pp.place=place
    pp.post=post
    pp.pin=pin
    pp.save()

    return HttpResponse("<script>alert('Added');window.location='/myapp/admin_addpump/'</script>")


def admin_editpump(request,id):
    ps=Petrol_pump.objects.get(id=id)

    return render(request,'admin/managepetrolpump/editpump.html',{'id':ps})

def editpumppost(request):
    id=request.POST['id']
    pname=request.POST["textfield"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    district=request.POST["textfield4"]
    place=request.POST["textfield5"]
    post=request.POST["textfield6"]
    pin=request.POST["textfield7"]

    pp = Petrol_pump.objects.get(id=id)
    pp.pump_name = pname
    pp.phone = phone
    pp.email = email
    pp.district = district
    pp.place = place
    pp.post = post
    pp.pin = pin
    pp.save()

    return HttpResponse("<script>alert('Updated');window.location='/myapp/admin_viewpump/'</script>")


def delete_pump(request,id):
    ps=Petrol_pump.objects.get(id=id)
    ps.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/myapp/admin_viewpump/'</script>")



def admin_viewpump(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp=Petrol_pump.objects.all()
    return render(request,'admin/managepetrolpump/viewpump.html',{'data':vp})

def adminviewpumppost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Petrol_pump.objects.filter(pump_name__icontains=search)
    return render(request, 'admin/managepetrolpump/viewpump.html', {'data': vp})


def admin_addservice(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'admin/manageservicecenter/addservicecenter.html')
def addservicepost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    name=request.POST["textfield"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    details=request.POST["textfield4"]
    district=request.POST["textfield5"]
    place=request.POST["textfield6"]
    post=request.POST["textfield7"]
    pin=request.POST["textfield8"]

    ss = Service_center()
    ss.center_name=name
    ss.phone=phone
    ss.email=email
    ss.details=details
    ss.district=district
    ss.place=place
    ss.post=post
    ss.pin=pin
    ss.save()

    return HttpResponse("<script>alert('Added');window.location='/myapp/admin_addservice/'</script>")



def admin_editservice(request,id):
    sv=Service_center.objects.get(id=id)
    return render(request,'admin/manageservicecenter/editservicecenter.html',{'id':sv})
def editservicepost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    id=request.POST['id']
    name=request.POST["textfield"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    details=request.POST["textfield4"]
    district=request.POST["textfield5"]
    place=request.POST["textfield6"]
    post=request.POST["textfield7"]
    pin=request.POST["textfield8"]

    ss = Service_center.objects.get(id=id)
    ss.center_name = name
    ss.phone = phone
    ss.email = email
    ss.details = details
    ss.district = district
    ss.place = place
    ss.post = post
    ss.pin = pin
    ss.save()

    return HttpResponse("<script>alert('Updated');window.location='/myapp/admin_viewservice/'</script>")

def delete_service(request,id):
    sv=Service_center.objects.get(id=id)
    sv.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/myapp/admin_viewservice/'</script>")


def admin_viewservice(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Service_center.objects.all()
    return render(request,'admin/manageservicecenter/viewservicecenter.html',{'data':vp})
def adminviewservicepost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Service_center.objects.filter(center_name__icontains=search)
    return render(request, 'admin/manageservicecenter/viewservicecenter.html', {'data': vp})


def admin_addtow(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'admin/managetowservice/addtow.html')
def addtowpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    name=request.POST["textfield"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    district=request.POST["textfield4"]
    place=request.POST["textfield5"]
    post=request.POST["textfield6"]
    pin=request.POST["textfield7"]

    tw = Tow_service()
    tw.tow_name=name
    tw.phone=phone
    tw.email=email
    tw.district=district
    tw.place=place
    tw.post=post
    tw.pin=pin
    tw.save()

    return HttpResponse("<script>alert('Added');window.location='/myapp/admin_addtow/'</script>")



def admin_edittow(request,id):
    ts=Tow_service.objects.get(id=id)
    return render(request,'admin/managetowservice/edittow.html',{'id':ts})
def edittowpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    id=request.POST['id']
    name=request.POST["textfield"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    district=request.POST["textfield4"]
    place=request.POST["textfield5"]
    post=request.POST["textfield6"]
    pin=request.POST["textfield7"]

    tw = Tow_service.objects.get(id=id)
    tw.tow_name = name
    tw.phone = phone
    tw.email = email
    tw.district = district
    tw.place = place
    tw.post = post
    tw.pin = pin
    tw.save()

    return HttpResponse("<script>alert('Updated');window.location='/myapp/admin_viewtow/'</script>")

def delete_towservice(request,id):
    sv=Tow_service.objects.get(id=id)
    sv.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/myapp/admin_viewtow/'</script>")


def admin_viewtow(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Tow_service.objects.all()
    return render(request,'admin/managetowservice/viewtow.html',{'data':vp})
def adminviewtowpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Tow_service.objects.filter(tow_name__icontains=search)
    return render(request, 'admin/managetowservice/viewtow.html', {'data': vp})


def admin_home(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'adminhimeindex.html')



def admin_changepwd(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'admin/changepassword.html')
def adminchangepassword(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    currentpwd=request.POST["textfield"]
    newpwd=request.POST["textfield2"]
    confirmpwd=request.POST["textfield3"]

    if newpwd==confirmpwd:
        al = Login.objects.filter(id=request.session['lid'], Password=currentpwd)
        if newpwd == currentpwd:
            return HttpResponse("<script>alert('Use different password');history.back()</script>")
        else:
            if al.exists():
                fs = Login.objects.filter(id=request.session['lid'], Password=currentpwd).update(Password=newpwd)
                return HttpResponse("<script>alert('Password successfully changed');window.location='/myapp/login/'</script>")

            else:
                return HttpResponse("<script>alert('Wrong password');history.back()</script>")
    else:
        return HttpResponse("<script>alert('Passwords doesnt match');history.back()</script>")





def admin_viewfeedback(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Feedback.objects.all()
    return render(request,'admin/viewfeedback.html',{'data':vp})
def viewfeedpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    fromdate=request.POST["textfield"]
    todate=request.POST["textfield2"]
    vp = Feedback.objects.filter(date__range=[fromdate,todate])
    return render(request, 'admin/viewfeedback.html', {'data': vp})


def admin_viewmech(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Mechanic.objects.filter(status='pending')
    return render(request,'admin/viewmechanic.html',{'data':vp})
def viewmechpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Mechanic.objects.filter(mechanic_name__icontains=search,status='pending')
    return render(request, 'admin/viewmechanic.html', {'data': vp})

def admin_aprvmech(request,id):
    mc=Mechanic.objects.filter(LOGIN=id).update(status="Approved")
    vv=Login.objects.filter(id=id).update(Type='mechanic')
    return HttpResponse("<script>alert(' Aproved ');window.location='/myapp/admin_viewapprovedmech/'</script>")

def admin_rejctmech(request,id):
    mc=Mechanic.objects.filter(id=id).update(status="Rejected")
    return HttpResponse("<script>alert(' Rejected ');window.location='/myapp/admin_viewrejectedmech/'</script>")

def admin_viewapprovedmech(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Mechanic.objects.filter(status="Approved")
    return render(request,'admin/viewapprovedmechanics.html',{'data':vp})
def viewaprvdmechpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Mechanic.objects.filter(mechanic_name__icontains=search,status='Approved')
    return render(request, 'admin/viewapprovedmechanics.html', {'data': vp})

def admin_viewrejectedmech(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Mechanic.objects.filter(status="Rejected")
    return render(request,'admin/viewrejectedmechanics.html',{'data':vp})
def viewrejmechpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Mechanic.objects.filter(mechanic_name__icontains=search,status='Rejected')
    return render(request, 'admin/viewrejectedmechanics.html', {'data': vp})

def admin_viewworkstatus(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Request.objects.all()
    return render(request,'admin/viewworkststus.html',{'data':vp})
def viewstatuspost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Request.objects.filter(date=search)
    return render(request, 'admin/viewworkststus.html', {'data': vp})










def mechanic_home(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'mechhomeindex.html')


def mechanic_viewprofile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    lid=request.session['lid']
    mp=Mechanic.objects.get(LOGIN_id=lid)
    return render(request,'mechanic/viewprofile.html',{'data':mp})

def mechanic_editprofile(request):
    me=Mechanic.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'mechanic/editprofile.html',{'data':me})
def editprofpost(request):
    id=request.POST['id']
    name=request.POST["textfield"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    specialization=request.POST["textfield4"]
    gender=request.POST["RadioGroup1"]
    district=request.POST["textfield6"]
    place=request.POST["textfield7"]
    post=request.POST["textfield8"]
    pin=request.POST["textfield9"]
    status=request.POST["textfield10"]

    pf = Mechanic.objects.get(id=id)
    pf.mechanic_name=name
    pf.phone=phone
    pf.email=email
    pf.specialization=specialization
    pf.gender=gender
    pf.district=district
    pf.place=place
    pf.post=post
    pf.pin=pin
    pf.availability=status
    pf.save()

    return HttpResponse("<script>alert('Updated');window.location='/myapp/mechanic_viewprofile/'</script>")

def mechanic_viewpump(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp=Petrol_pump.objects.all()
    return render(request,'mechanic/viewpump.html',{'data':vp})
def viewpumppost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Petrol_pump.objects.filter(pump_name__icontains=search)
    return render(request, 'mechanic/viewpump.html',{'data': vp})


def mechanic_viewreq(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Request.objects.filter(status='Pending',MECHANIC__LOGIN_id=request.session['lid'])
    return render(request,'mechanic/viewreqandconfirm.html',{'data':vp})

def aprvuser(request,id):
    res=Request.objects.filter(id=id).update(status="approved")
    return HttpResponse("<script>alert(' Aproved ');window.location='/myapp/viewaprvdusers/'</script>")

def rejuser(request,id):
    res=Request.objects.filter(id=id).update(status="rejected")
    return HttpResponse("<script>alert(' Rejected ');window.location='/myapp/rejectedusers/'</script>")




def viewreqpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Request.objects.filter(date=search,status='pending',MECHANIC__LOGIN_id=request.session['lid'])
    return render(request, 'mechanic/viewreqandconfirm.html', {'data': vp})

def mechanic_chat(request):
    return render(request,'mechanic/chat.html')

def viewaprvdusers(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Request.objects.filter(status='approved',MECHANIC__LOGIN_id=request.session['lid'])
    return render(request,'mechanic/viewapprovedusers.html', {'data': vp})

def viewaprvduserspost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Request.objects.filter(USER__user_name__icontains=search,status='approved')
    return render(request, 'mechanic/viewapprovedusers.html', {'data': vp})


def rejectedusers(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Request.objects.filter(status='rejected',MECHANIC__LOGIN_id=request.session['lid'])
    return render(request,'mechanic/viewrejectedusers.html', {'data': vp})
def viewrejuserpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Request.objects.filter(USER__user_name__icontains=search,status='rejected')
    return render(request, 'mechanic/viewrejectedusers.html', {'data': vp})


def mechanic_changepassword(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'mechanic/changepassword.html')
def mechchangepwd(request):
    currentpwd=request.POST["textfield"]
    newpwd=request.POST["textfield2"]
    confirmpwd=request.POST["textfield3"]
    if newpwd==confirmpwd:
        al = Login.objects.filter(id=request.session['lid'], Password=currentpwd)
        if newpwd==currentpwd:
            return HttpResponse("<script>alert('Use different password');history.back()</script>")
        else:

            if al.exists():
                fs = Login.objects.filter(id=request.session['lid'], Password=currentpwd).update(Password=newpwd)
                return HttpResponse("<script>alert('Password successfully changed');window.location='/myapp/login/'</script>")

            else:
                return HttpResponse("<script>alert('Wrong password');history.back()</script>")
    else:
        return HttpResponse("<script>alert('Passwords doesnt match');history.back()</script>")



def user_addfeedback(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'user/addfeedback.html')
def addfeedpost(request):
    feedback=request.POST["textarea"]

    fb = Feedback()
    fb.feedback=feedback
    import datetime
    date=datetime.datetime.now().date()
    fb.date=date
    fb.USER_id=User.objects.get(LOGIN=request.session['lid']).id
    fb.save()

    return HttpResponse("<script>alert(' Feedback sent ');window.location='/myapp/user_home/'</script>")

def user_changepassword(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'user/changepassword.html')
def userchangepwd(request):
    currentpwd=request.POST["textfield"]
    newpwd=request.POST["textfield2"]
    confirmpwd=request.POST["textfield3"]
    if newpwd==confirmpwd:
        al = Login.objects.filter(id=request.session['lid'], Password=currentpwd)
        if newpwd == currentpwd:
            return HttpResponse("<script>alert('Use different password');history.back()</script>")
        else:
            if al.exists():
                fs = Login.objects.filter(id=request.session['lid'], Password=currentpwd).update(Password=newpwd)
                return HttpResponse("<script>alert('Password successfully changed');window.location='/myapp/login/'</script>")

            else:
                return HttpResponse("<script>alert('Wrong password');history.back()</script>")
    else:
        return HttpResponse("<script>alert('Passwords doesnt match');history.back()</script>")






def user_home(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    return render(request,'userhomeindex.html')


def user_viewnearestmech(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    # vp = Rating.objects.filter(MECHANIC__status="Approved")
    vp = Mechanic.objects.filter(status="Approved")

    return render(request,'user/viewnearestmechanics.html',{'data':vp})
def viewnearestmechpost(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    search=request.POST["textfield"]
    vp = Mechanic.objects.filter(Q(place__icontains=search)  |  Q(district__icontains=search)  |  Q(post__icontains=search),status="Approved")
    return render(request, 'user/viewnearestmechanics.html', {'data': vp})


def reqmechanic(request,id):
    rs = Request()
    rs.date=datetime.now()
    rs.status="pending"
    rs.MECHANIC=Mechanic.objects.get(id=id)
    rs.USER=User.objects.get(LOGIN__id=request.session['lid'])
    rs.save()
    return HttpResponse("<script>alert(' Requested ');window.location='/myapp/userviewreqstatus/'</script>")


def user_viewservicecenter(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Service_center.objects.all()
    return render(request,'user/viewservicecenter.html',{'data':vp})
def userviewservicepost(request):
    search=request.POST["textfield"]
    # vp = Service_center.objects.filter(place__icontains=search)
    vp = Service_center.objects.filter(Q(place__icontains=search) | Q(district__icontains=search)  |  Q(post__icontains=search))

    return render(request, 'user/viewservicecenter.html', {'data': vp})


def user_viewpump(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Petrol_pump.objects.all()
    return render(request,'user/viewpump.html',{'data':vp})


def userviewpumppost(request):
    search=request.POST["textfield"]
    print(search)
    vp = Petrol_pump.objects.filter(Q(place__icontains=search) | Q(district__icontains=search)  |  Q(post__icontains=search))
    return render(request, 'user/viewpump.html', {'data': vp})


def mechanicsignup(request):
    return render(request,'mechsignupindex.html')
def mechsignuppost(request):
    name=request.POST["textfield"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    specialization=request.POST["textfield4"]
    gender=request.POST["RadioGroup1"]
    district=request.POST["textfield5"]
    place=request.POST["textfield6"]
    post=request.POST["textfield7"]
    pin=request.POST["textfield8"]
    pwd=request.POST["textfield9"]
    confirmpwd=request.POST["textfield10"]

    res=Login.objects.filter(Username=email)
    if res.exists():
        return HttpResponse("<script>alert(' Email already exist');window.location='/myapp/mechanicsignup/'</script>")

    if pwd==confirmpwd:
        lg = Login()
        lg.Username = email
        lg.Password = confirmpwd
        lg.Type = 'pending'
        lg.save()

        ms = Mechanic()
        ms.mechanic_name = name
        ms.phone = phone
        ms.email = email
        ms.specialization = specialization
        ms.gender = gender
        ms.district = district
        ms.place = place
        ms.post = post
        ms.pin = pin
        ms.LOGIN = lg
        ms.status = 'pending'
        ms.availability = 'Available'
        ms.save()

        return HttpResponse("<script>alert(' Successfully requested ');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert(' Invalid password ');window.location='/myapp/login/'</script>")



def usersignup(request):
    return render(request,'usersignupindex.html')
def usersignuppost(request):
    name=request.POST["textfield"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    gender=request.POST["RadioGroup1"]
    district=request.POST["textfield4"]
    place=request.POST["textfield5"]
    post=request.POST["textfield6"]
    pin=request.POST["textfield7"]
    pwd=request.POST["textfield8"]
    confirmpwd=request.POST["textfield9"]

    res = Login.objects.filter(Username=email)
    if res.exists():
        return HttpResponse("<script>alert(' Email already exist');window.location='/myapp/usersignup/'</script>")

    if pwd==confirmpwd:
        ulg = Login()
        ulg.Username = email
        ulg.Password = confirmpwd
        ulg.Type = "User"
        ulg.save()

        us = User()
        us.user_name = name
        us.phone = phone
        us.email = email
        us.gender = gender
        us.district = district
        us.place = place
        us.post = post
        us.pin = pin
        us.LOGIN = ulg
        us.save()

        return HttpResponse("<script>alert(' Successfully registered ');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert(' Incorrect password ');window.location='/myapp/usersignup/'</script>")


def user_viewtow(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Tow_service.objects.all()
    return render(request,'user/viewtow.html',{'data':vp})
def userviewtowpost(request):
    search=request.POST["textfield"]
    vp = Tow_service.objects.filter(Q(place__icontains=search) | Q(district__icontains=search)  |  Q(post__icontains=search))
    return render(request, 'user/viewtow.html', {'data': vp})

def user_chat(request):
    return render(request,'user/chat.html')

def userviewreqstatus(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Successfully loggedout');window.location='/myapp/login/'</script>")

    vp = Request.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'user/viewreqstatus.html',{'data':vp})


from django.core.mail import send_mail
from django.conf import settings

def forget_password(request):
    return render(request,'forgotpassword.html')

def forget_password_post(request):

    em = request.POST['em_add']
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(random.choice(characters) for i in range(8))
    log = Login.objects.filter(Username=em)
    if log.exists():
        logg = Login.objects.get(Username=em)
        message = 'temporary password is ' + str(strong_password)
        send_mail(
            'temp password',
            message,
            settings.EMAIL_HOST_USER,
            [em, ],
            fail_silently=False
        )
        logg.Password = strong_password
        logg.save()
        return HttpResponse('<script>alert("success");window.location="/myapp/login/"</script>')
    else:
        return HttpResponse('<script>alert("invalid email");window.location="/myapp/login/"</script>')



def rating(request,id):
    return render(request,"User/rating.html",{'id':id})

def rating_post(request):
    ratings=request.POST['rating']
    mech=request.POST['mid']

    obj=Rating()
    obj.rating=ratings
    from datetime import datetime
    obj.date=datetime.now().strftime('%Y-%m-%d')
    obj.USER=User.objects.get(LOGIN=request.session['lid'])
    obj.MECHANIC_id=mech
    obj.save()
    return HttpResponse('<script>alert("Success");window.location="/myapp/user_viewnearestmech/"</script>')




def user_view_rating(request,id):
    res=Rating.objects.filter(MECHANIC_id=id)
    return render(request,"User/viewrating.html",{'data':res, 'id':id})




############chat

# mechanic view

def chat1(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = User.objects.get(LOGIN=cid)

    return render(request, "Mechanic/Chat.html", {'name': qry.user_name, 'toid': cid})


def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = User.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM=fromid, TO=toid) | Q(FROM=toid, TO=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO.id, "date": i.date, "from": i.FROM.id,'photo':'/static/chat_style/images/user.png'})

    return JsonResponse({ "data": l, 'name': qry.user_name, 'toid': request.session["userid"]})


def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})

# chat in mechanice

def chat_with_user(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = Mechanic.objects.get(LOGIN=cid)

    return render(request, "User/Chat.html", {'name': qry.mechanic_name, 'toid': cid})


def chat_view_user(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = User.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM=fromid, TO=toid) | Q(FROM=toid, TO=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO.id, "date": i.date, "from": i.FROM.id,'photo':'/static/chat_style/images/mechanic.png/'})

    return JsonResponse({ "data": l, 'name': qry.user_name, 'toid': request.session["userid"]})


def chat_send_mech(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})






###############





# userview

def chat2(request,id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = Mechanic.objects.get(LOGIN=cid)

    return render(request, "User/Chat.html", {'name': qry.mechanic_name, 'toid': cid})


def chat_view2(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = Mechanic.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM=fromid, TO=toid) | Q(FROM=toid, TO=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO.id, "date": i.date, "from": i.FROM.id})

    return JsonResponse({ "data": l, 'name': qry.mechanic_name, 'toid': request.session["userid"]})


def chat_send2(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})

# chat in mechanice

def chat_with_user2(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = User.objects.get(LOGIN=cid)

    return render(request, "Mechanic/Chat.html", {'name': qry.user_name,'toid': cid})


def chat_view_user2(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = Mechanic.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM=fromid, TO=toid) | Q(FROM=toid, TO=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO.id, "date": i.date, "from": i.FROM.id})

    return JsonResponse({ "data": l, 'name': qry.mechanic_name, 'toid': request.session["userid"]})


def chat_send_mech2(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})

