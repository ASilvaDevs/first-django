from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post, name='post'),
    path('exemplo1', views.exemplo1, name='exemplo1'),
    path('exemplo2', views.exemplo2, name='exemplo2'),
]
