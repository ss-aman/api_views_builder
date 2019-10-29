==============
API VIEWS BUILDER
==============

api_viewset_maker is a Django APP, when working with django-rest-framework management commands in it are capable to make all API VIEWSETS automatically for existing models in the app.

How To Use
----------

1. Add "api_viewset_maker" to INSTALLED_APPS ::

    INSTALLED_APPS = [
        ...
        "api_viewset_maker",
    ]

2. For making viewsets of all models in selected apps execute command `python manage.py make_viewset_apps '<app1>' '<app2>' '<app3>'`.

3. For making viewsets of selected models in a app execute command `python manage.py make_viewset_models '<app_name>' '<model1>' '<model2>'` 

4. After execution commands you will see 3 more files in app, 'rest_serializers.py', 'rest_views.py', 'rest_urls.py', now in project urls add path of rest_urls::
	path('', include('app_name.rest_urls')),


