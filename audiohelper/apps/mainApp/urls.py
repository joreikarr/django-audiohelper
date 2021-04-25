from django.conf.urls.static import static
from django.urls import path

from audiohelper import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.regist, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('cabinet', views.cabinetPage, name='cabinet'),
    path('download/<str:fileName>', views.download_file, name='download'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)