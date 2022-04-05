from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "Event"

urlpatterns = [
    path("list/", views.event_list, name="list"), 
    path("detail/<int:id>/", views.event_detail, name="detail"), 
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)