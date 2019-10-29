SERIALIZER_FORMAT = """
class {h1}Serializer(serializers.ModelSerializer):
	class Meta:
		model = models.{h2}
		fields = '__all__'

"""


VIEW_SET_FORMAT = """
class {h1}ViewSet(ModelViewSet):
    serializer_class = local_serializers.{h1}Serializer
    queryset = models.{h2}.objects.all()
    # filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    
    # filter_fields = []
    # search_fields = []
    # ordering_fields = []
    sample_fields = {fields}

"""


URLS_FORMAT = """
router.register('{h1_low}', rest_views.{h1}ViewSet, base_name='{h1_low}')
"""

URLS_END = """
urlpatterns = router.urls

"""

SERIALIZER_IMPORTS = """from rest_framework import serializers

from . import models

"""

VIEW_SETS_IMPORTS = """from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from . import local_serializers
from . import models

"""


URLS_IMPORTS = """from rest_framework.routers import DefaultRouter

from . import rest_views


router = DefaultRouter(trailing_slash=True)

"""


model_name_formater = lambda name: name.replace('Model', '') if 'Model' in name else name


SERIALIZER_FILE_NAME = 'local_serializers.py'
VIEW_FILE_NAME = 'rest_views.py'
URL_FILE_NAME = 'rest_urls.py'
