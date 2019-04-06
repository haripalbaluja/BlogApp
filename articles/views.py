from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Comment
# Create your views here.

def article_list(request):
	articles = Article.objects.all().order_by('date')
	return render(request,'articles/articles_list.html',{'articles':articles})


def article_detail(request, slug):
	#return HttpResponse(slug)
	article = Article.objects.get(slug =slug)
	comments = Comment.objects.filter(post=article).order_by('-created_date')
	print(comments)
	return render(request,'articles/article_detail.html',{'article':article,'comments':comments})

@login_required(login_url="/accounts/login")

def article_create(request):
	if request.method =='POST':
		form = forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			# save article to DB
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('articles:list')


	else:
		form = forms.CreateArticle()
	return render(request,'articles/article_create.html',{'form':form})	



def create_comment(request, pk):

	if request.method == 'POST':
		form = forms.CommentForm(request.POST)	
		
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.post_id = pk
			instance.save()
			article = Article.objects.get(pk = pk)
			
			
		#return render(request,'articles/create_comment.html', { 'article_id': pk })
		return redirect('/articles/'+str(article.slug))
	
	
	else:
		print("PK: ", pk)
		return render(request,'articles/create_comment.html', { 'article_id': pk })

	

