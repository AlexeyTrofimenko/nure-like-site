# <img src="https://i.imgur.com/is6XZAN.png" width="32"> ІДЗ з ФМПІЗ (Веб-розробка)

## Скріншоти застосунку

![Site](https://i.imgur.com/LBmH63O.png)

![Admin panel](https://i.imgur.com/zIJNeVT.png)

## Установка та запуск (Linux)

Переконайтеся, що у вас встановлений Python версії **3.8** або новіше та `pip`.

```
python --version
```

```
pip --version
```

Дотримуйтесь наведених нижче інструкцій, щоб встановити залежності та запустити проект.

### Створення та активація віртуального оточення

```
python3 -m venv venv
```

```
source venv/bin/activate
```

### Встановлення залежностей

```
pip install -r requirements.txt
```

```
npm install -D tailwindcsste
```

```
npx tailwindcss init
```

```
python manage.py tailwind install
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
python manage.py tailwind start
```

### Запуск серверу

```
python manage.py runserver
```

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
