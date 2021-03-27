from django.shortcuts import render, HttpResponseRedirect
from .models import Post, Author
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
from django.conf import settings

def user_login(request):
    if request.method == 'GET':
        form = LoginForm()        
    else:                
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #{'username': 'aidai', ;}
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None: 
                if user.is_active: 
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, 'Ваш аккаунт заблокирован')
            else:     
                messages.error(request, 'Неправильный ввод данных') 

    return render(request, 'blog/login.html', {'login_form': form})

def user_register(request):
    if request.method == 'GET':
        form = RegistrationForm()
    else:        
        form = RegistrationForm(request.POST)
        #cd = form.cleaned_data 
        user_exists = User.objects.filter(email=request.POST['email']).exists()
        if not user_exists: 
            if form.is_valid(): 
                new_user = form.save(commit=False)
                new_user.username = request.POST['email']
                new_user.set_password(form.cleaned_data['password1'])
                new_user.save()
                Author.objects.create(user=new_user, first_name='', last_name='')
                return HttpResponseRedirect('/login/')
            else:
               messages.error(request, 'Неправильные данные') 
        else:
            messages.error(request, 'Такой пользователь уже есть')

    return render(request, 'blog/register.html', {'register_form': form})

@login_required 
def post_list(request):
    posts = Post.objects.filter() #ORM - select * from posts       
    return render(request, 'blog/post_list.html', {"posts": posts})

@login_required     
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors.html', {"authors": authors})

def contact(request): 
    if request.method == 'POST':
        print(request.POST)
        sender_email = request.POST['sender-email']
        msg = request.POST['msg-text']
        receiver = 'aidai.beishekeeva@gmail.com'
        subject = 'Hello'
        send_mail(subject, msg, sender_email, [receiver])
        messages.info(request, 'Ваш email отправлен')

    return render(request, 'blog/contact.html')
