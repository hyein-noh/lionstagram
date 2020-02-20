from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post' :post})

def new(request):
    #글 작성 submit 버튼을 눌렀을 때
    if request.method == 'POST':
        post = Post()
        post.author = request.user
        post.title = request.POST['title']
        post.content= request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.save()

        return redirect('/detail/'+str(post.id))
    else: 

        return render(request, 'new.html')