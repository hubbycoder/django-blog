from django.shortcuts import render

posts = [
    {
        'author': 'RedJay',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'December 1, 2019'
    },
    {
        'author': 'BlueJay',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'December 2, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
