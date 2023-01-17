# Notification micro service
<hr />

Cette application est un microservice en charge de l'envois des notification (__emails, sms, push notifications__).


### Technologies utilisées
>- Python 3.8+
>- Celery 5+
>- Redis
>- Django rest framework


### Procédure d'Installation 
1. Clonage du projet en local
>`git clone git@gitlab.com:cryptoechangeur/microservices/notification-service.git`.

2. Installation des dépendances
> `cd notification_service` <br/>
> `pip install -r requirements.txt` <br/>

3. Configuration des variables d\'environement<br/>
Créer un fichier `.env` à la racine du projet et ajouter le __SECRET_KEY__, le __CELERY_BROKER_REDIS_URL__. 
- Le __SECRET_KEY__ correspond à la clé secrete de l'application django. généré par la commande:<br/>
`python -c "import secrets; print(secrets.token_urlsafe())"`.


- Le __CELERY_BROKER_REDIS_URL__ correspond à l'URL de Redis server installé au préalable sur la machine.

> *<u>Exemple de fichier __.env__</u> :* <br/>
> DEBUG=True <br/>
> SECRET_KEY = 'bfQspVSh90eG3yrQo8lBZjKLfkDCsjwXvA9Gmc12cUo' <br/>
> CELERY_BROKER_REDIS_URL='redis://127.0.0.1:6379'



### Démarage du service 
> `python manage.py makemigrations`<br/>
> `python manage.py migrate`<br/>
> `python manage.py runserver`<br/>

### Démarage Celery
> `celery -A notification_service worker --loglevel=info`


### Routes URL
> *http://localhost:8000/apis/v1/notifications/email/* <br/>
> *http://localhost:8000/apis/v1/notifications/sms/*

Tous est ready!
