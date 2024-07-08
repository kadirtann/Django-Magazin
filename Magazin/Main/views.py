from django.shortcuts import render

def index(request):
    return render(request, 'Main/base.html')

def blog(request):
    return render(request, 'Main/blog.html')

def blog_category(request):
    return render(request, 'Main/blog-category.html')

def fashion(request):
    return render(request, 'Main/fashion.html')

def lifestyle(request):
    return render(request, 'Main/lifestyle.html')

def travel(request):
    return render(request, 'Main/travel.html')

def post_single(request):
    return render(request, 'Main/post-single.html')
