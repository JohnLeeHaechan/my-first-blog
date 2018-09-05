from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
    path('', views.mainIndex, name='index'),
    path('detail/', views.detail, name='detail'),
#    path('detail/photo/<int:year>/<int:month>/<int:day>', views.photo, name='photo')
    path('detail/photo/2018/08/22/devil.jpeg', views.photo, name='photo')
]
