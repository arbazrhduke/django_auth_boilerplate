 - https://www.codefactor.io/repository/github/signalr/signalr/badge?style=plasti
# django_auth_boilerplate
This is a boiler plate code built for custom django user model and token authentication login for Django rest framework projects.

set up instructions

create a virtual environment as by running following command.

virtualenv -p python3.6 env

activate the virtual env by using the command.

source env/bin/activate

install all dependencies from requirements.txt file by running follwing command.

pip install -r requirements.txt

assign values to settings variables decalred .env file

you are good to go. 

Run the project by simply using the local settings by the following command.

python manage.py runserver 

alternatively you can also run by using following commands.

local:
python manage.py runserver --settings django_auth_boilerplate.settings.local

production:
python manage.py runserver --settings django_auth_boilerplate.settings.production 


