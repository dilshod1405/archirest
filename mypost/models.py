from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone


def custom_validator(value):
    valid_formats = ['png', 'jpeg', 'jpg']
    if not any([True if value.name.lower().endswith(i) else False for i in valid_formats]):
        raise ValidationError(f'{value.name} jpg, png va jpeg formatiga mos emas')


architector = 'arxitektor'
designer = '3d dizayner'
all_ = 'arxitektor va dizayner'
client = 'Buyurtmachi'

Professions = (
    ('arxitektor', architector),
    ('3d dizayner', designer),
    ('arxitektor va dizayner', all_),
    ('Buyurtmachi', client)
)


# Users
class MyUser(AbstractUser):
    avatar = models.FileField(validators=[custom_validator], verbose_name='Profil rasmi')
    login = models.CharField(max_length=50, unique=True, verbose_name='Foydalanuvchi taxallusi')
    about = models.TextField(max_length=1000, verbose_name='Foydalanuvchi haqida ma`lumot')
    role = models.CharField(choices=Professions, max_length=30, verbose_name='Foydalanuvchi sohasi')

    class Meta:
        db_table = 'Foydalanuvchi'

    def __str__(self):
        return f'{self.username}  {self.role}'


# Specialty
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Yo`nalish'

    def __str__(self):
        return f'{self.name}'


def custom_validator_file(value):
    valid_formats = ['pdf', 'dwg']
    if not any([True if value.name.lower().endswith(i) else False for i in valid_formats]):
        raise ValidationError(f'{value.name} tushmadi. Faylingiz pdf yoki dwg formatida bo`lishi lozim')


# Posts
class Post(models.Model):
    file = models.FileField(null=False, upload_to='files', validators=[custom_validator_file],
                            verbose_name='Fayl yuklash')
    image = models.ImageField(null=False, upload_to='media', verbose_name='Rasm yuklash')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    created_date = models.TimeField(auto_now=True, verbose_name='Yuklangan vaqti')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Yo`nalish')

    # category = models.ForeignKey(Category, on_delete=models.SET_NULL(), null=True, blank=True); postni o'chirmaslik

    class Meta:
        db_table = 'Postlar'

    def __str__(self):
        return f'{self.category}  :  {self.created_date}  :  {self.user}'


# Comments of posts
class CommentsModel(models.Model):
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)],
                                 verbose_name='Baholash')
    rating_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Izoh muallifi')
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField(null=False, max_length=200, verbose_name='Izoh matni')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post id raqami')

    class Meta:
        db_table = 'Izohlar'

    def __str__(self):
        return f'{self.rating_user}  :  {self.date}  :  {self.rating}  :  {self.text}'


# Chatting
class Chatting(models.Model):
    text = models.TextField(max_length=1000)
    time = models.TimeField(auto_now=True)
    from_user = models.ForeignKey(MyUser, related_name='yuboruvchi', on_delete=models.CASCADE)
    to_user = models.ForeignKey(MyUser, related_name='qabulqiluvchi', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Yozishmalar'

    def __str__(self):
        return f'{self.from_user}  -->  {self.to_user}  :  {self.time}'


architector = 'arxitektor'
designer = '3d dizayner'
constructor = 'konstruktor'

Profession = (
    ('arxitektor', architector),
    ('3d dizayner', designer),
    ('konstruktor', constructor),
)


# Vacancy
class Vacancy(models.Model):
    title_of_job = models.CharField(choices=Profession, max_length=30, verbose_name='Ish o`rinlari')
    address = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=13, null=False)
    name_of_company = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'Bo`sh ish o`rinlari'

    def __str__(self):
        return f'{self.title_of_job}  :  {self.phone}  :  {self.address}'
