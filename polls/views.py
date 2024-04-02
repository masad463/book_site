from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, \
    CreateView
from django.views.generic.edit import FormView, UpdateView
from .forms import CommentForm, UserPasswordChangeForm, BookForm, \
    RegisterForm, ProfileUserForm
from .models import Book, Comment, Category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model
from .utils import DataMixin


class IndexBook(DataMixin, ListView):
    """Главная страница"""
    model = Book
    template_name = 'main.html'
    context_object_name = 'books'
    title_page = 'Главная страница'

    def get_queryset(self):
        return Book.objects.filter(status='published')


class BookDetail(DataMixin, DetailView):
    """Данные о книге"""
    model = Book
    template_name = 'blog/book_detail.html'
    context_object_name = 'book'
    title_page = ''
    slug_url_kwarg = 'book_slug'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = context['book']
        comments = (book.comment_set.order_by('-time_add')
                    .select_related('author'))
        paginator = Paginator(comments, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            comments_page = paginator.get_page(page)
        except PageNotAnInteger:
            comments_page = paginator.get_page(1)
        except EmptyPage:
            comments_page = paginator.get_page(paginator.num_pages)

        context['comments'] = comments_page
        context['form'] = CommentForm
        context['author_name'] = book.author
        context['title'] = book.title

        return context

    # добавление комментария
    def post(self, request, *args, **kwargs):
        book = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.author = request.user
            comment.save()
            return redirect('book_detail', book_slug=book.slug)
        kwargs['object'] = book  # передаем объект книги в аргументах
        return super().get(request, *args, **kwargs)


@login_required
def delete_comment(request, comment_id):
    """Удаление комментария пользователем"""
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    book_slug = comment.book.slug  # сохраняем book_id для перенаправления

    if request.method == 'POST':
        comment.delete()
        return redirect('book_detail', book_slug=book_slug)

    return render(request, 'users/comment_confirm_delete.html',
                  {'comment': comment})


def search(request):
    """Поиск книг на сайте"""
    query = request.GET.get('q')
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    if not books.exists():
        no_results_message = 'Не было найдено ни одной книги'
        return render(request, 'main.html',
                      {'no_results_message': no_results_message})

    return render(request, 'main.html', {'books': books})


class CatalogBooks(DataMixin, TemplateView):
    """Каталог(категории)"""
    template_name = 'blog/catalog.html'
    title_page = 'Каталог'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryDetail(DataMixin, DetailView):
    """Отображение списока книг определённой категории"""
    model = Category
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['category']
        books = category.get_books()
        context['books'] = books
        context['title'] = category.name
        return context


class RecentBooksView(ListView):
    """5 самых последних добавленных книг"""
    model = Book
    extra_context = {
        'title': 'Новинки',
    }
    template_name = 'header/recent_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status='published').order_by('-created_at')[:5]


class RegisterPage(DataMixin, FormView):
    """Страница регистрации"""
    template_name = 'registration/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    title_page = 'Регистрация'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user,
              backend='django.contrib.auth.backends.ModelBackend')
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home'))
        return super(RegisterPage, self).get(*args, **kwargs)


class AuthorBook(LoginRequiredMixin, DataMixin, CreateView):
    """Добавление книги на сайт(в неопубликованном виде)"""
    form_class = BookForm
    title_page = 'Добавьте свою книгу'
    model = Book
    template_name = 'authors/create_book.html'
    context_object_name = 'author'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.instance.image = self.request.FILES['image']
        form.instance.text_file = self.request.FILES['text_file']
        return super().form_valid(form)


author_book_view = login_required(AuthorBook.as_view())


#
class SuccessCreate(ListView):
    """Успешное добавление книги"""
    model = Book
    template_name = 'authors/success.html'


class ProfileUser(LoginRequiredMixin, UpdateView):
    """Профиль пользователя"""
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/user_profile.html'
    extra_context = {
        'title': 'Профиль пользователя',
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    """
    Класс для изменения пароля пользователя с использованием
    пользовательской формы и представления
    """
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "users/password_change_form.html"


class AuthorBooksListView(DataMixin, ListView):
    """Список книг автора"""
    model = Book
    template_name = 'authors/author_books.html'
    context_object_name = 'book_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_name = self.kwargs['author_name']
        context['title'] = author_name
        context['author'] = author_name
        return context

    def get_queryset(self):
        author_name = self.kwargs['author_name']
        return Book.objects.filter(author=author_name)
