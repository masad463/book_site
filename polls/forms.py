import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from .models import Comment, Book
from django.conf import settings


class CommentForm(forms.ModelForm):
    """Форма комментария"""
    content = forms.CharField(label='Комментарий', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Comment
        fields = ['content']


class RegisterForm(UserCreationForm):
    """Форма регистрации"""
    username = forms.CharField(label="Логин", widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    email = forms.CharField(label="E-mail", widget=forms.EmailInput(
        attrs={'class': 'form-input'}))

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повтор пароля",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class UserForgotPasswordForm(PasswordResetForm):
    """
    Запрос на восстановление пароля
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(SetPasswordForm):
    """
    Изменение пароля пользователя после подтверждения
    """

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserPasswordChangeForm(PasswordChangeForm):
    """Смена пароля"""
    old_password = forms.CharField(label="Старый пароль",
                                   widget=forms.PasswordInput(
                                       attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль",
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля",
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-input'}))


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control', 'autocomplete': 'off'})


class BookForm(forms.ModelForm):
    """Форма добавления книги"""
    author = forms.CharField(label='Автор', max_length=100)
    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox,
                               public_key=settings.RECAPTCHA_PUBLIC_KEY,
                               private_key=settings.RECAPTCHA_PRIVATE_KEY,
                               label='ReCAPTCHA')

    class Meta:
        model = Book
        fields = ['title', 'image', 'genre', 'author', 'text_file']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileUserForm(BaseForm):
    """Форма профиля"""
    photo = forms.ImageField(label='Фотография', required=False,
                             widget=forms.FileInput)
    username = forms.CharField(disabled=True, label='Логин',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail',
                            widget=forms.TextInput(
                                attrs={'class': 'form-input'}))
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(
        years=tuple(range(this_year - 100, this_year - 5))))

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name',
                  'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }
