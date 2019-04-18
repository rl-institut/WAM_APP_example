from django.urls import path
from . import views
app_name = 'WAM_APP_example'

urlpatterns = [
    path('', views.example_view, name='index')
]
