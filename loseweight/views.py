from django.shortcuts import render, redirect, get_object_or_404
from models.models import Foods, About, Blog
from accounts.models import APPUser


# Create your views here.
def dashboard(request):
    context = {
        'user_count': APPUser.objects.count(),
        'blog_count': Blog.objects.count(),
    }
    return render(request, 'base.html', context)


def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['message']
        About.objects.create(name=name, email=email, text=text)
        return redirect('about')
    return render(request, 'about.html')


def calc(request):
    context = {
        't': False,
    }
    if request.method == 'POST':
        age = request.POST['age']
        height = request.POST['height']
        weight = request.POST['weight']
        bmi = int(weight) / ((int(height) / 100) ** 2)
        context = {
            't': True,
            'bmi': ('%.2f' % bmi),
            'age': age,
            'height': height,
            'weight': weight,
            'foods': Foods.objects.filter(bmi_start__lte=bmi, bmi_end__gte=bmi),
        }
        return render(request, 'BMICalc.html', context)
    return render(request, 'BMICalc.html', context)


def blog(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'blog.html', context)


def blog_detail(request, id):
    context = {
        'blog': get_object_or_404(Blog, id=id),
    }
    return render(request, 'blog_detail.html', context)
