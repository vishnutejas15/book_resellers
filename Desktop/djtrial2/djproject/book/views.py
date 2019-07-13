from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,logout,login
from .forms import UserRegisterForm,adminform,sellbookform,booksearchForm
from .models import owner
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request,'home1.html')


def send_email():
    send_mail(
    'verify notification',
    'book is added to library verify it.',
    'chandanhs.19mar1999@gmail.com',
    ['prabhutp2@gmail.com'],
    fail_silently=False,
)

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserRegisterForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
            return render(request,'rthanks.html')
        else:
            print(user_form.errors)
    else:
        user_form=UserRegisterForm()
        return render(request,'auth/register.html',{'form':user_form,'registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'userchoice.html')
            else:
                return HttpResponse("your account is in active")
        else:
                print("someone tried to login and field")
                print("They used username:{} and password: {}".format(username,password))
                return HttpResponse("invalid login")
    else:
        return render(request,'auth/login.html',{})




def user_logout(request):
    logout(request)
    return redirect('/')

def adminlogin(request):
    if request.method=='POST':
                username=request.POST.get('un')
                password=request.POST.get('pw')
                if username=="acnpv" and password=="acnpv":
                    return render(request,"adminchoice.html")
                else:
                    return render(request,'error.html')
    else:
        form=adminform()
        return render(request,'adminlogin.html',{'form':form})



def delete(request):
    if request.method=="POST":
        print(request.POST)
        result=owner.objects.all()
        for i in request.POST.keys():
            print(i)
            for r in result:
                if str(r.id)==i:
                    id=i
                    print(id)
            # return redirect('/delete-book/<id>')
                    result1=owner.objects.get(id=id)
                    result1.delete()
        return redirect('/')
    else:
        result=owner.objects.all()
        return render(request,"delete.html",{'result':result})


def verify(request):
    if request.method=="POST":
        result=owner.objects.all()
        print(request.POST)
        for i in request.POST.keys():
            print(i)
            for r in result:
                if r.verified==False and str(r.id) in request.POST:
                    #print(r.verified) 
                    r.verified=True
                    #print(r.verified)  
                    r.save()  
        return redirect('/')
    else:
        result=owner.objects.all()
        return render(request,"verify.html",{'result':result})


def sellbook(request):
    if request.method=='POST':
        form=sellbookform(request.POST)
        if form.is_valid():
            form.save()
            send_email()
            return render(request,"thanks.html")
    else:
        form=sellbookform()
        return render(request,'bookinfo.html',{'form':form})


def buybook(request):
    if request.method=='POST':
        search=booksearchForm(request.POST)
        print(search)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            print(value)
            result=owner.objects.filter(book_name__contains=value)
            return render(request,'buybook1.html',{'result':result})
    else:
        form=booksearchForm()
        result=owner.objects.all()
        return render(request,"buybook1.html",{'form':form,'result':result})

def buy(request,id):
    result=owner.objects.get(id=id)
    if request.method=="POST":
        pw=request.POST.get('password')
        if pw== result.bookpassword:
            result1=owner.objects.get(id=id)
            result1.delete()
            return render(request,"bthanks.html")
        else:
            return render(request,"error.html")

    else:
        return render(request,"confirmation1.html",{'result':result})

def userchoice(request):
    return render(request,"userchoice.html")

def dash_board(request):
    ow=owner.objects.all()
    c=0
    for i in ow:
        if i.verified==True:
            c+=1
    u_count=len(User.objects.all())
    count=len(owner.objects.all())
    return render(request,"dashboard.html",{'nu':u_count,'nv':c,'nb':count})







# def deletebook(request):
#     result=owner.objects.get(id=id)
#     result.delete()
#     return redirect('/')










# count= len(owner.objects.all())
#for o in o:
#u_count= len(User.objects.all())
# #






# Create your views here.
