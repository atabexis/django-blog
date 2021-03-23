from django.shortcuts import render, HttpResponseRedirect
from .models import Post, Author
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'GET':
        form = LoginForm()        
    else:        
        print(request.POST)
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

def post_list(request):
    # ORM - object relational mapper 
    posts = Post.objects.filter() #ORM - select * from posts       
    return render(request, 'blog/post_list.html', {"posts": posts})
    
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors.html', {"authors": authors})


