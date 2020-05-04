from django.urls import path
from . import views

app_name = 'poll_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:poll_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('vote_first/<int:poll_pk>', views.VoteFirst, name='vote_first'),
    path('vote_second/<int:poll_pk>', views.VoteSecond, name='vote_second'),
    path('random/',views.PickRandom, name='random'),
    path('create_comment/<int:poll_pk>', views.createComment, name='create_comment'),
]