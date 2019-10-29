from django.apps import apps
from django.utils.text import slugify
from django.db import models

from .variables_set import *


def get_model_filter_fields(model):
    return [i.name for i in model._meta.fields if not isinstance(i, models.FileField)]


def create_file(path, str_data):
    file = open(path, 'w+')
    file.write(str_data)
    file.close()


def get_serializer_data(models_names):
    text_data = SERIALIZER_IMPORTS
    text_data += ''.join([SERIALIZER_FORMAT.format(h1=model_name_formater(i), h2=i) for i in models_names])
    return text_data


def get_view_data(models_dict):
    text_data = VIEW_SETS_IMPORTS
    text_data += ''.join([VIEW_SET_FORMAT.format(h1=model_name_formater(i), h2=i, fields=get_model_filter_fields(j))
                          for i, j in models_dict.items()])
    return text_data


def get_url_data(models_names):
    text_data = URLS_IMPORTS
    text_data += ''.join([URLS_FORMAT.format(h1=model_name_formater(i), h1_low=slugify(i)) for i in models_names])
    text_data += URLS_END
    return text_data


def create_all_files(app, models_dict):
    create_file('{}/{}'.format(app.path, SERIALIZER_FILE_NAME), get_serializer_data(models_dict.keys()))
    create_file('{}/{}'.format(app.path, VIEW_FILE_NAME), get_view_data(models_dict))
    create_file('{}/{}'.format(app.path, URL_FILE_NAME), get_url_data(models_dict.keys()))


def create_viewset_files(api_apps):
    for app in apps.get_app_configs():
        if not app.name == 'user' and app.name in api_apps:
            create_all_files(app, {model.__name__: model for model in app.get_models()})


def create_model_viewset(app_name, models_dict):
    for app in apps.get_app_configs():
        if not app.name == 'user' and app.name in [app_name]:
            create_all_files(app, models_dict)
