# Online-Shop_Django

Onlone Shop Project
Developed by Django, Bootstrap and Docker


## General info

Work on little complete online shop with Django . . .

Some features we worked on

* docker files
* product list
* product view
* wishlist
* add to cart
* sorting system
* order
* zarinpal
* django-jalali-date
* crispy forms
* bootstrap
* registeration system (allauth)
* new user model without default model
* and ...

## Technologies

Project is created with:

* Python: 3.10.2
* Django: 4.0.2
* Docker 20.10.20
* Bootstrap 4

## Help

If you are considering a particular method, more modern technology Add to my project and send merge request, I will add
you in the credits and contributors section

## Setup

* 1 : Clone the repository:

```shell
   git clone https://github.com/MKashkouli/Online-Shop_17Dey.git
```

* 2 : Create a new virtual environment :

```shell
  python -m venv venv

```
* 3 : Activate the Venv :

( On WINDOWS)
```shell
  venv\Scripts\activate

```
(On Linux or macOS)
```shell
  source venv/bin/activate

```

* 4 : Build the Docker image:

```shell
docker-compose build 
```

* 5 : Start the containers:

```shell
docker-compose up -d

*  6 : Create the database tables:

```shell
 docker-compose exec web python manage.py migrate
```

* 7 : Create a superuser:

```shell
 docker-compose exec web python manage.py createsuperuser
```

* 8 :  install package | library from requirements.txt

```shell
 pip install -r requirements.txt
```

* 9 : Visit http://localhost:8000

## Contributors

* [MKashkouli](https://github.com/MKashkouli)

