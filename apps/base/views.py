from django.shortcuts import render
from apps.telegram_bot.views import get_text

from apps.base import models
# Create your views here.
def index(request):
    settings = models.Settings.objects.latest('id')
    about = models.About.objects.latest('id')
    categories = models.Catigory.objects.all()
    projects = models.Project.objects.all()
    skills = models.Skills.objects.latest('id')
    video = models.Video.objects.latest('id')
    partners = models.Partners.objects.all()
    review = models.Reviews.objects.all()
    news = models.News.objects.all()

    category_id = request.GET.get('data-filter')  # Получаем ID выбранной категории из запроса
    print
    if category_id:  # Если указана категория, фильтруем проекты
        projects = models.Project.objects.filter(catigory=category_id)

    if request.method == 'POST':
        if "newslater" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            page_contact = models.Contacts.objects.create(name=name, email=email, message=message)
            if page_contact:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                            
    Имя пользователя:  {name}
    Почта: {email}
    Сообщение: {message}

    """)

    return render(request, 'index.html', {'settings': settings,
                                           'about': about,
                                           'categories': categories,
                                           'projects': projects,
                                           'skills': skills,
                                           'video': video,
                                           'partners': partners,
                                           'review': review,
                                           'news': news})

