from django.shortcuts import render

from apps.base import models
# Create your views here.
def index(request):
    settings = models.Settings.objects.latest('id')
    about = models.About.objects.latest('id')
    catigoty = models.Catigory.objects.all()
    projects = models.Products.objects.all()
    skills = models.Skills.objects.latest('id')
    video = models.Video.objects.latest('id')
    partners = models.Partners.objects.all()
    review = models.Reviews.objects.all()
    news = models.News.objects.all()

    return render(request, 'index.html', locals())