## Python Django Tutorial

1. Launch VS Code Editor
2. Ctrl + P and type git
3. Select Git:clone and paste repository URL
4. Choose local directory to pull
5. open project
6. Ctrl + ` to open Terminal
7. Create virtual envvironment: 
    * $ python3 -m venv env (lowercase and no spaces)
    * $ sudo apt install python3-venv (if get errors)    
8. Activate virtualenv:
    * $ . env/bin/activate
9. Installing packages with requirements:
   open the text file, replace the == with >= , and execute:
   * (env) $ pip install -r requirements.txt --upgrade 
   update requirements:
   * (env) $ pip freeze > requirements.txt
10. Create migrations
   * (env) $ python manage.py makemigrations
11. Applying migrations:
   * (env) $ python manage.py migrate 
12. Create an admin user:
   * (env) $ python manage.py createsuperuser    
    * Username: admin
    * Email address: admin@example.com
    * Password: **********
    * Password (again): *********
    * Superuser created successfully.
13. Start the development server:
   * (env) $ python manage.py runserver
14. Open a Web browser:
    * http://127.0.0.1:8000
    * http://127.0.0.1:8000/admin
