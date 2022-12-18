from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from .models import Article,Comment
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request,"home.html")

def about(request):   
    return render(request,"about.html")

def articles(request):
    search = request.GET.get("search") 
    if search:
        articles = Article.objects.filter(title__contains = search) 
        return render(request, "articles.html", {"articles":articles})
    articles = Article.objects.all() 
    return render(request, "articles.html", {"articles": articles})

@login_required(login_url="user:login")  
def detail(request,id): 
    article = get_object_or_404(Article, id=id) 
    comments = article.comments.all()
    return render(request, "detail.html", {"article": article, "comments": comments})

@login_required(login_url="user:login")    
def dashboard(request):
    articles = Article.objects.filter(author = request.user) 
    context = {
        "articles": articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")   
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None) 
    if form.is_valid():
        article = form.save(commit= False) 
        if len(article.content)< 20000:
            article.author = request.user 
            article.save() 
            messages.success(request, "Article Successfully Created")
            return redirect("article:dashboard") 
        
        messages.error(request, "Content can not be more than 5000 characters and can not be blank")
        return render(request, "addarticle.html",{"form": form})

    if request.method == "POST":
        messages.error(request, "Content can not be blank")

    return render(request, "addarticle.html",{"form": form})
    
@login_required(login_url="user:login")    
def updateArticle(request,id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article)
    if form.is_valid(): 
        article = form.save(commit= False)                                                                                   
        article.author = request.user 
        article.save()
        messages.success(request, "Article Successfully Updated")
        return redirect("article:dashboard")
        
    return render(request,"update.html", {"form": form})

@login_required(login_url="user:login")    
def deleteArticle(request,id):
    article = get_object_or_404(Article, id = id)

    article.delete()
    messages.success(request, "Article Successfully Deleted")
    
    return redirect("article:dashboard") 


@login_required(login_url="user:login")
def addComment(request,id):
    
    article = get_object_or_404(Article, id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        if not comment_author or not comment_content:
            messages.error(request, "Name or Content can not be left blank")
            return redirect(reverse("article:detail", kwargs = {"id": id}))

        if len(comment_author)>25 or len(comment_content)>1000:
            messages.error(request, "Name can not be more than 50 characters or Content can not be more than 1000 characters")
            return redirect(reverse("article:detail", kwargs = {"id": id}))

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)

        newComment.article = article
        newComment.save()

    return redirect(reverse("article:detail", kwargs = {"id": id})) 
    


# Documentation --> https://docs.djangoproject.com/en/4.1/ref/urlresolvers/