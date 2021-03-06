from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('companies.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)