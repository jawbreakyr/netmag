from django.shortcuts import render, get_object_or_404

from blog.models import Post


def index(request):
	# get the blog post that are published
	posts = Post.objects.filter(published=True)
	# now return the render template
	return render(request,'blog/index.html',{'posts':posts})


def post(request, slug):
	# get the Post object
	post = get_object_or_404(Post, slug=slug)
	# now return the render request template
	return render(request, 'blog/post.html',{'post':post})

# Create your views here.
