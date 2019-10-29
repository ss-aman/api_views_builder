from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps


class Command(BaseCommand):
    help = 'give apps name and models names in list as argument to create Model ViewSet for particular app\'s models'
    app_not_exist_error = 'specified app not registered in INSTALLED_APPS'
    model_not_exist_error = 'specified some models do not exist in app {}'
    success_message = "Successfully Made ModelViewSets for given app's models"

    def add_arguments(self, parser):
        parser.add_argument('app', type=str)
        parser.add_argument('models', nargs='+', type=str)

    def handle(self, *args, **options):
        from api_viewset_maker.rest_helper.detect_models import create_model_viewset
        arg_app = options['app']
        arg_models = options['models']

        app = [app for app in apps.get_app_configs() if app.name in [arg_app]]
        if not app:
            raise CommandError(self.app_not_exist_error)
        app = app[0]
        model_exists = {i.__name__: i for i in app.get_models() if i.__name__ in arg_models}
        model_non_exist = [i for i in arg_models if i not in model_exists.keys()]
        if model_non_exist:
            raise CommandError(self.model_not_exist_error.format(str(model_non_exist)))

        create_model_viewset(app.name, model_exists)
        self.stdout.write(self.style.SUCCESS(self.success_message))
