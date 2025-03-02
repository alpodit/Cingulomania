from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.hug_page, name='hug_page'),
    path('send/<int:receiver_id>/', views.send_hug, name='send_hug'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


