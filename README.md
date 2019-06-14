# easy-todo-app
Easy todo app


# 1. How to start in pycharm
1. Go to Interpreter options and create new venv
2. `$ pip install django`
3. ` pip freeze > requirements.txt`
4. Create `.gitignore`
5. Create django project:
    ```
    $ mkdir backend
    $ django-admin startproject todoapp backend
    ```
6. Go to Django settings, setup Django path
7. Add Django server configuration
8. Run server and test `http://127.0.0.1:8000/`

# 2. Create first app
1. Mark `backend` as `Source Root` (right click > Mark Directory as)
2. `$ cd backend && django-admin startapp todo`
3. Add Django tests configuration
3. Do your stuff in app
4. Run `$ ./manage.py makemigrations`
5. Run `$ ./manage.py migrate`

# 3. Lets some code!

# 4. Django Rest Framework
1. https://www.django-rest-framework.org/#installation

# 5. Start with React!
1. `$ npx create-react-app todo`
2. Change folder name `todo` to `fronted`
3. `$ npm start`
