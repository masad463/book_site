<!-- Содержимое -->
<details>
  <summary>Содержимое</summary>
  <ol>
    <li>
      <a href="#about-the-project">О проекте</a>
      <ul>
        <li><a href="#built-with">Используемые технологии</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Начало</a>
      <ul>
        <li><a href="#prerequisites">Установка</a></li>
      </ul>
    </li>
    <li><a href="#usage">Что из себя представляет проект</a></li>
  </ol>
</details>




<!-- О проекте -->
## О проекте

Данный проект представляет собой онлайн библиотеку под названием "FreeLibrary". 
На нём распологаются различные книги разных категорий в бесплатном доступе. 

"FreeLibrary" - это сайт, где вы можно абсолютно свободно и бесплатно погрузиться в мир литературы и открыть для себя множество книг
различных жанров и направлений.

### Используемые технологии

* <a href="https://www.djangoproject.com/">
    <img src="https://habrastorage.org/r/w1560/getpro/habr/post_images/1d5/28e/2cb/1d528e2cb5fbc29ad16c74e5d883c371.png" alt="Django" height="35">
  </a>
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* <a href="https://python-social-auth.readthedocs.io/en/latest/index.html">
    <img src="https://static.codingforentrepreneurs.com/media/series/python-social-auth/10b61e68-7721-43d2-bf76-cdac30fc38df.png" alt="Python Social Auth" height="35">
  </a>
* <a href="https://pypi.org/project/django-recaptcha/">
    <img src="https://avatars.githubusercontent.com/u/151521335?s=280&v=4" alt="Django captcha" height="65">
  </a>
* <a href="https://www.postgresql.org/">
    <img src="https://www.arsis.ru/wp-content/uploads/2023/04/postgres-logo-1-1.png" alt="PostgreSQL" height="88" width="145">
  </a>




<!-- Начало -->
## Начало

### Установка

1. Для начала нужно скопировать репозиторий.
   ```cmd
   git clone https://github.com/masad463/book_site
   ```
2. Установить необходимые библиотеки
   ```cmd
    pip install -r requrements.txt


<!-- Технологии реализованые в проекте -->
## Что из себя представляет проект

1. Система авторизации и регистрации
    * Авторизация через ВК
    * Авторизация через GitHub
   
2. Данные о книге
    * Название книги
    * Автор книги
    * Год первой публикации
    * Жанр
    * Краткое описание
    * Категория
    * Возможность скачать текст книги
    * Комментарии пользователей к книге
    * Изображение книги

3. Возможность удалять и добавлять комментарии к книге

4. Поиск на сайте по названию книги

5. Страница с каталогом книг(список категорий)

6. Страница с недавно добавленными книгами 

7. Добавление книги пользователем на сайт после одобрения администратора

8. Профиль пользователя
   * У пользователя есть возможность указать собственный возраст
   * Возможность смены пароля
   * Указать свою фамилию и имя
 
9. Страница с книгами автора


[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
