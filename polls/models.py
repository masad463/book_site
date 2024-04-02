from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify


def translit_to_eng(s: str) -> str:
    eng_to_ru = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
                 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
                 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
                 'ч': 'ch',
                 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r',
                 'ю': 'yu', 'я': 'ya'}

    return "".join(
        map(lambda i: eng_to_ru[i] if eng_to_ru.get(i, False) else i,
            s.lower()))


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True,
                              null=True, verbose_name='Фотография')
    date_birth = models.DateTimeField(blank=True, null=True,
                                      verbose_name='Дата рождения')


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название',
                            default=None, db_index=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_books(self):
        return self.book_set.all().prefetch_related('category')


class Book(models.Model):
    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Неопубликовано')
    )
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="Slug")
    description = models.CharField(max_length=1000,
                                   verbose_name='Краткое описание', null=True,
                                   blank=True)
    image = models.ImageField(
        upload_to='images/cover/',
        blank=True,
        verbose_name='Обложка',
        validators=[
            FileExtensionValidator(
                allowed_extensions=('png', 'jpg', 'webp', 'jpeg')
            )
        ]
    )

    author = models.CharField(max_length=190, verbose_name='Автор', null=True,
                              blank=True)
    genre = models.CharField(max_length=80, verbose_name='Жанр', blank=True)
    public_date = models.DateField(
        verbose_name='Дата выхода',
        blank=True,
        default='2001-01-01'
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True, default=None,
                                 verbose_name='Категория')
    status = models.CharField(choices=STATUS_OPTIONS, default='draft',
                              verbose_name='Статус поста', max_length=10)
    created_at = models.DateTimeField(verbose_name='Время добавления',
                                      default=datetime.now)
    text_file = models.FileField(
        upload_to='book_text',
        blank=True, null=True,
        verbose_name='Текст книги',
        validators=[
            FileExtensionValidator
            (allowed_extensions=('doc', 'docx')
             )
        ]
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.title))
        super().save(*args, **kwargs)


class Comment(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор комментария',
                               on_delete=models.CASCADE,
                               related_name='comments_author')
    content = models.TextField(max_length=1000, default='',
                               verbose_name='Комментарий')
    time_add = models.DateTimeField(
        verbose_name='Время добавления',
        default=datetime.now)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.author}: {self.content}'
