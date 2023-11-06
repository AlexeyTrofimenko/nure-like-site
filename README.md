# <img src="https://i.imgur.com/is6XZAN.png" width="32"> ІДЗ з ФМПІЗ (Веб-розробка)

## Скріншоти застосунку

![Site](https://i.imgur.com/LBmH63O.png)

![Admin panel](https://i.imgur.com/oZnlCub.png)

## Установка та запуск (Linux)

Переконайтеся, що у вас встановлений `python` версії **3.8** або новіше та `pip`.

```
python --version
```

```
pip --version
```

Дотримуйтесь наведених нижче інструкцій, щоб встановити залежності та запустити проект.

### Створення та активація віртуального оточення

```
python -m venv env
```

```
source env/bin/activate
```

### Встановлення залежностей

```
pip install -r requirements.txt
```

### Міграція бази даних

```
python manage.py makemigrations
```

```
python manage.py migrate
```

### Створення аккаунту адміністратора

```
python manage.py createsuperuser
```

> [!NOTE]
> Використовується для роботи з адмін-панелью


### Компіляція CSS

```
python manage.py tailwind build
```

### Збір static файлів

```
python manage.py collectstatic
```

### Запуск локального серверу

```
python manage.py runserver
```

### Запуск серверу у режимі Production
```
gunicorn -b host:port core.wsgi:application
```

> [!WARNING]
> Переконайтеся, що **host** присутній у ALLOWED_HOSTS, змінна DEBUG = False, а значення змінної SECRET_KEY приховано в core/settings.py. Змінні знаходяться у файлі .env

### Посилання на інші ресурси
<img src="https://www.vectorlogo.zone/logos/digitalocean/digitalocean-tile.svg" width="32"> [Розгортання на сервісі Digital ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps)

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/2560px-Amazon_Web_Services_Logo.svg.png" width="32"> [Розгортання на сервісі Amazon AWS](https://aws.amazon.com/blogs/containers/deploy-and-scale-django-applications-on-aws-app-runner/)

## Адміністрування

Для зміни наповнення сайту за допомогою засобів адміністрування потрібно:
1. Перейти за шляхом `/admin`.
2. Увійти в систему використовуючи [аккаунт адміністратора](#створення-аккаунту-адміністратора).
3. Вибрати необхідний розділ для редагування.
4. Внести зміни та зберегти їх.

## Розробники

Студенти групи ІПЗм-23-1

- [Владислав Лапін](https://github.com/MagisterFelix)

- [Трофіменко Олексій](https://github.com/AlexeyTrofimenko)
