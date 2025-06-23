"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from diseases.models import Disease
from django.urls import include, path
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['id', 'sn', 'name', 'description', 'disease_ontology_description', 'uniprot', 'uniprot_description', 'mondo_id', 'disease_data_source', 'associated_disease', 'protein_count', 'direct_association_count', 'gard_rare', 'symbol', 'disease_ontology_url', 'mondosource_id']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'diseases', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('diseases/', include('diseases.urls')),
]





