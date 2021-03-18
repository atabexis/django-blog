from django.shortcuts import render
from .models import Post, Author
#GET
#POST 
def login(request):
    if request.method == 'GET':
        return render(request, 'blog/login.html')
    else:
        
        pass 

def post_list(request):
    # ORM - object relational mapper 
    posts = Post.objects.filter() #ORM - select * from posts       
    return render(request, 'blog/post_list.html', {"posts": posts})
    
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors.html', {"authors": authors})


