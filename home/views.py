from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from blog1.models import Post
from home.models import Contact


# Create your views here.

def homepage(request):
    return render(request,'home/index.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['confpass']

        if firstname == "":
            messages.error(request,"First Name should not be empty")
            return redirect('/register')
        elif lastname == "":
            messages.error(request,"Last Name should not be empty")
            return redirect('/register')
        elif username == "":
            messages.error(request,"Username should not be empty")
            return redirect('/register')
        elif email == "":
            messages.error(request,"Email should not be empty")
            return redirect('/register')
        elif password == "":
            messages.error(request,"Password should not be empty")
            return redirect('/register')
        elif cpassword == "":
            messages.error(request,"Confim Password should not be empty")
            return redirect('/register')
        elif password == cpassword:
            messages.error(request,"Password and Confim Password should be same")
            return redirect('/register')
        elif len(username) > 7:
            messages.error(request,"Username should not be more than 7 characters")
            return redirect('/register') 
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username not available')
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect("/register")
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()
                messages.info(request,'Registered Successfully')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/')
    else:
        return render(request,'home/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'Login Successfully')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            messages.error(request,'Check Username or Password')
            return redirect('/login')
    else:
        return render(request,'home/login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('/')

def search(request):
    query = request.GET['query']
    if(len(query)>60):
        posts = Post.objects.none()
    else:
        posttitles = Post.objects.filter(title__icontains = query)
        postcontents = Post.objects.filter(desc__icontains = query)
        posts=posttitles.union(postcontents)

    if posts.count()==0:
        messages.warning(request,"No search result found")
    context = {'posts':posts,'query':query} 

    return render(request,'home/search.html',context)

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        username='dddd'
        email=request.POST['email']
        contact=request.POST['contact']
        msg=request.POST['msg']
        print(username)
        # if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<3 :
        #     messages.error(request,"Please fill the form corectly")
        # else:
        contact=Contact(name=name,username=username,email=email,contactno=contact,msg=msg)
        contact.save()
        messages.success(request,"Thank you for contacting us")
        return redirect("/contact")
    else:
        return render(request,'home/contact.html')
    
    return render(request,'home/conatct.html')
