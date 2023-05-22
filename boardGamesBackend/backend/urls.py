from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/add', views.add_game, name='add_game'),
    path('game/all', views.get_game, name='get_all_games'),
    path('game/get_id', views.get_game_by_id, name='get_game_by_id'),
    path('game/get_status', views.get_game_by_status, name='get_game_by_status'),
    path('game/delete', views.delete_game, name='delete_game'),
    path('game/accept', views.accept_game, name='accept_game'),
    path('user/add', views.add_user, name='add_user'),
    path('user/all', views.get_users, name='get_all_users'),
    path('user/get_id', views.get_user_by_id, name='get_user_by_id'),
    path('user/delete', views.delete_user, name='delete_user'),
    path('meeting/add', views.add_meeting, name='add_meeting'),
    path('meeting/all', views.get_meeting, name='get_all_meetings'),
    path('meeting/user', views.get_meeting_by_user_id, name='get_meeting_by_user_id'),
    path('meeting/get_id', views.get_meeting_by_id, name='get_meeting_by_id'),
    path('meeting/delete', views.delete_meeting, name='delete_meeting'),
    path('meeting/rm_user', views.remove_user_from_meeting, name='remove_user_from_meeting'),
    path('meeting/add_user', views.add_user_to_meeting, name='add_user_to_meeting'),
    path('meeting/add_date', views.add_preffered_date, name='add_preffered_date'),
    path('meeting/set_date', views.set_meeting_date, name='set_meeting_date'),
    path('meeting/get_users', views.meeting_get_users, name='get_users_from_meeting'),
    path('denied', views.permission_denied, name='denied'),
    path('authorize', views.auth, name='authorize')
]