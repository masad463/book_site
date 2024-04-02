from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.sitemaps.views import sitemap
from django.urls import path, reverse_lazy
from . import views
from django.views.decorators.cache import cache_page
from .sitemaps import BookSitemap

sitemaps = {
    'book_sitemap': BookSitemap,
}

urlpatterns = [
    path("", views.IndexBook.as_view(), name="home"),
    path('login/', LoginView.as_view(next_page='profile',
                                     redirect_authenticated_user=True),
         name='login'),
    path('success/', views.SuccessCreate.as_view(), name='success'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('search/', views.search, name='search'),
    path('book_detail/<slug:book_slug>/',
         views.BookDetail.as_view(), name='book_detail'),
    path('catalog/', cache_page(60)(views.CatalogBooks.as_view()),
         name='catalog'),
    path('category/<int:pk>/', cache_page(60)(views.CategoryDetail.as_view()),
         name='category_detail'),
    path('recent-books/', cache_page(60)(views.RecentBooksView.as_view()),
         name='recent_books'),
    path('comment/<int:comment_id>/delete/', views.delete_comment,
         name='delete-comment'),
    path('password-change/', views.UserPasswordChange.as_view(),
         name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
         name='password_change_done'),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name="users/password_reset_form.html",
             email_template_name="users/password_reset_email.html",
             success_url=reverse_lazy("password_reset_done")
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name="users/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name="users/password_reset_confirm.html",
             success_url=reverse_lazy("password_reset_complete")
         ),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(
             template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),
    path('author_book/', cache_page(60)(views.author_book_view),
         name='author_book'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('author_books/<str:author_name>/',
         cache_page(60)(views.AuthorBooksListView.as_view()),
         name='author_books'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
         name="django.contrib.sitemaps.views.sitemap")
]
