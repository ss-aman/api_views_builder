from django.core.management.base import BaseCommand, CommandError
from django.apps import apps


class Command(BaseCommand):
    help = 'give apps names in list as argument to create Model ViewSet for apps'
    error = 'Some Specified Apps not exist in INSTALLED_APPS - {}'
    success_message = 'Successfully Made ModelViewSets for defined Apps'

    def add_arguments(self, parser):
        parser.add_argument('apps', nargs='+')

    def handle(self, *args, **options):
        from api_viewset_maker.rest_helper.detect_models import create_viewset_files
        apps_list = [app.name for app in apps.get_app_configs()]
        arg_apps = options['apps']

        existing_apps = [app for app in apps_list if app in arg_apps]
        non_existing_apps = [app for app in arg_apps if app not in existing_apps]

        if non_existing_apps:
            raise CommandError(self.error.format(str(non_existing_apps)))
        create_viewset_files(existing_apps)
        self.stdout.write(self.style.SUCCESS(self.success_message))
