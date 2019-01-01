# Django developer test

This project is a user profile management for developer evaluation. It contains backend and front-end

- Backend: [Django](https://www.djangoproject.com/) + [Django REST Framework](https://www.django-rest-framework.org/)
- Front-end: [Vue.js](https://vuejs.org/) + [Bootstrap+Vue](https://bootstrap-vue.js.org/)

### Installation

Clone repository

```sh
$ git clone https://github.com/benvasseur/mg_test.git
$ cd mg_test
```

Backend installation

```sh
$ cd server
$ python3 manage.py runserver 8000
```

Front-end installation: Open new terminal and go to project root

```sh
$ cd client
$ npm i
$ npm run dev
```

Now you can open http://localhost:8080/ and use the application.

### List of APIs

All the apis can be test here:

- [User list](http://localhost:8000/api/users/)
- [User details](http://localhost:8000/api/users/2)
- [User profile picture upload](http://localhost:8000/api/users/picture/2)
- [Login](http://localhost:8000/api/auth/login)
- [User registration](http://localhost:8000/api/auth/register)