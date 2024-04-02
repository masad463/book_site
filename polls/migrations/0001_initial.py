# Generated by Django 4.2.2 on 2024-03-10 04:18

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="users/%Y/%m/%d/",
                        verbose_name="Фотография",
                    ),
                ),
                (
                    "date_birth",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="Slug"),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Краткое описание",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="images/cover/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=("png", "jpg", "webp", "jpeg")
                            )
                        ],
                        verbose_name="Обложка",
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        blank=True, max_length=190, null=True, verbose_name="Автор"
                    ),
                ),
                (
                    "genre",
                    models.CharField(blank=True, max_length=80, verbose_name="Жанр"),
                ),
                (
                    "public_date",
                    models.IntegerField(
                        blank=True, default=2000, verbose_name="Дата выхода"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("published", "Опубликовано"),
                            ("draft", "Неопубликовано"),
                        ],
                        default="draft",
                        max_length=10,
                        verbose_name="Статус поста",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="Время добавления"
                    ),
                ),
                (
                    "text_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="book_text",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=("doc", "docx")
                            )
                        ],
                        verbose_name="Текст книги",
                    ),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default=None, max_length=100, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(max_length=255, verbose_name="Тема письма"),
                ),
                ("email", models.EmailField(max_length=255, verbose_name="email")),
                ("content", models.TextField(verbose_name="Содержимое письма")),
                (
                    "time_sent",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата отправки"
                    ),
                ),
                (
                    "user_ip",
                    models.GenericIPAddressField(
                        blank=True, null=True, verbose_name="IP отправителя"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Обратная связь",
                "verbose_name_plural": "Обратная связь",
                "ordering": ["-time_sent"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        default="", max_length=1000, verbose_name="Комментарий"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments_author",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор комментария",
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.book"
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("books", models.ManyToManyField(to="polls.book")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Корзина",
                "verbose_name_plural": "Корзина",
            },
        ),
        migrations.AddField(
            model_name="book",
            name="category",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.category",
                verbose_name="Категория",
            ),
        ),
    ]