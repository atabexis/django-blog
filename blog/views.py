from django.shortcuts import render
from .models import Post, Author

def post_list(request):
    posts = Post.objects.all() #ORM - select * from posts   
    return render(request, 'blog/post_list.html', {"posts": posts})
    
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors.html', {"authors": authors})