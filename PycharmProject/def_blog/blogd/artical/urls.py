from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.first , name='first'),
    path('heade', views.heade, name='heade'),
    path('create_head', views.create_head, name='create_head'),
    path('show_headin',views.show_heading, name='show_headin'),
    path('show_contents/<int:head_id>',views.show_contents,name='show_contents'),
    path('create_contents/<int:head_id>',views.create_contents,name='create_contents'),
    path('create_artical',views.create_artical,name='create_artical'),
    path('show_articals', views.show_articals, name='show_articals')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

