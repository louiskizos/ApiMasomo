from django.urls import path
from .views import *


urlpatterns = [
    path('', etablissemntView, name='tout_etablissement'),
    path('Tout_etablissement/', tout_etablissement, name='Tout_etablissement'),
    
    
    path('Test/', test, name='Test'),
    path('Test_post/', test_post, name='Test_post'),
    path('Test_details/<int:pk>/', recherche_get.as_view()),
    path('Create/', CreateApiViewTest.as_view()),
    path('Update/<int:pk>/', UpdateApiViewTest.as_view()),
    path('Delete/<int:pk>/', DeleteApiView.as_view())
]
