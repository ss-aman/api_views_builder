API Viewset Maker
=================

``api_viewset_maker`` is a Django application that automatically generates
Django REST Framework serializers, viewsets, and URL routes for your existing
Django models. It removes repetitive boilerplate and accelerates API
development with simple management commands.

Features
--------

- Automatically generates:

  - ``rest_serializers.py``
  - ``rest_views.py``
  - ``rest_urls.py``

- Supports:

  - Generating viewsets for **all models** in selected apps
  - Generating viewsets for **specific models** in a single app

- Fully compatible with Django REST Framework
- Safe and repeatable — updates only generated files


Installation
------------

Add the app to your project's ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        "api_viewset_maker",
    ]


Usage
-----

Generate Viewsets for All Models in Selected Apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command:

.. code-block:: bash

    python manage.py make_viewset_apps 'app1' 'app2' 'app3'


Generate Viewsets for Selected Models in a Specific App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the command:

.. code-block:: bash

    python manage.py make_viewset_models 'app_name' 'Model1' 'Model2'


Integrating Generated Routes
----------------------------

After running the commands, the following files will be created inside each
target app:

- ``rest_serializers.py``
- ``rest_views.py``
- ``rest_urls.py``

To expose the generated REST API endpoints, include the app’s ``rest_urls`` in
your main ``urls.py``:

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path("", include("app_name.rest_urls")),
    ]


How It Works
------------

``api_viewset_maker`` inspects your Django models and automatically:

1. Creates a ``ModelSerializer`` for each model.
2. Creates a ``ModelViewSet`` associated with the serializer.
3. Registers the generated viewsets in a DRF router.
4. Writes everything to:

   - ``rest_serializers.py``
   - ``rest_views.py``
   - ``rest_urls.py``

This results in ready-to-use REST API endpoints without manually writing serializers, viewsets, or routing.


Ideal For
---------

- Projects containing many models
- Teams requiring consistent, auto-generated API layers
- Rapid prototyping
- Avoiding repetitive serializer and viewset creation

