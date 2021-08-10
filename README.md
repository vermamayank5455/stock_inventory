<h4> Inventory management software </h4>

This is an inventory management system written in Python 3.6.5 and Django 2.0.7 and datatables is a Jquery plugin. </br>
The local installation of python 32/64bit is provided with the project as "python-3.7.0.exe/python-3.7.0-amd64.exe".  </br>
Also the local installation of DJango is provided as "django-master" which can be run as "python setup.py install". </br>






A simple inventory management system built with Django. Users can add stock item and generate bills. All data is stored in database and are rendered in real time. </br>

To run project, run the following commands in the project's directory to create the database. When running the software for the first time, it is necessary to run each command for each app in the project.  </br>


cd inventory </br>
python manage.py makemigrations </br>
python manage.py migrate </br>

Use the following command to create an admin user </br>
python manage.py createsuperuser </br>

Use the following command to run the server </br>

python manage.py runserver </br>

Go to </br>
http://127.0.0.1:8000/admin-se/   

And login 
Login with the superuser user created
