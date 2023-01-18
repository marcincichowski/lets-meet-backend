from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_game, name='add'),
    path('all', views.get_game, name='all'),
    path('delete', views.delete_game, name='delete'),
    path('denied', views.permission_denied, name='denied'),
    path('authorize', views.auth, name='authorize')
]