from django.db import models

 
# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to='image_logo/',
        verbose_name='Логотип'
    )
    main_logo = models.ImageField(
        upload_to='image_logo_main/',
        verbose_name='Главное лого'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя '
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = 'Должность'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фотография'
    )
    address =models.CharField(
        max_length = 255,
        verbose_name = 'Адрес'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефон'
    )
    facebook = models.URLField(
        verbose_name = 'Facebook URL'
    )
    twitter = models.URLField(
        verbose_name = 'Twitter URL'
    )


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '1) Основная Настройка'
        verbose_name_plural = '1) Основные Настройки'


class About(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фотография'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = '2) Об о мне'
        verbose_name_plural = '2) Об о мне'

class Catigory(models.Model):
    catigory = models.CharField(
        max_length = 255,
        verbose_name = 'Название Категория'
    )

    def __str__(self):
        return self.catigory
    
    class Meta:
        verbose_name = '3) Категория'
        verbose_name_plural = '4) Категории'

class Project(models.Model):
    catigory = models.ForeignKey(Catigory, on_delete=models.CASCADE, 
                            verbose_name='Выбрать категорию'
    )
    image = models.ImageField(
        upload_to='image_products/',
        verbose_name='Фотграфия'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '5) Проект'
        verbose_name_plural = '5) Проекты'


class Skills(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '6) Скил'
        verbose_name_plural = '6) Скилы'

class SkillsPercent(models.Model):
    skills = models.ForeignKey(Skills,
                               related_name = 'skills_title',
                               on_delete=models.CASCADE)
    percent = models.CharField(
        max_length = 255,
        verbose_name = 'процент'
    )
    title1 =models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    class Meta:
        unique_together = ('skills', 'percent')

class Video(models.Model):
    video = models.URLField(
        verbose_name = 'Видео'
    )
    image = models.ImageField(
        upload_to='image_back',
        verbose_name='Фотография background'
    )

    def __str__(self):
        return self.video
    
    class Meta:
        verbose_name = '7) Видео'
        verbose_name_plural = '7) Видео'

class Partners(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фотография'
    )

    class Meta:
        verbose_name = '8) Парнер'
        verbose_name_plural = '8) Парнеры'

class Reviews(models.Model):
    review = models.TextField(
        verbose_name = 'Отзыв'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = 'Должность'
    )
    image = models.ImageField(
        upload_to='image_review/', 
        verbose_name='Фотография'
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "9) Отзыв"
        verbose_name_plural = '9) Отзывы'

class News(models.Model):
    image = models.ImageField(
        upload_to='image_news/',
        verbose_name='Фотография'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Время публикации'
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '10) Новость'
        verbose_name_plural = '10) Новости'

class Contacts(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    message = models.TextField(
        verbose_name = 'Сообщение'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '11) Обратная связь'
        verbose_name_plural = '11) Обратная связь'


