from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "Add"

urlpatterns = [
    path("<int:id>/", views.add, name="add"), 
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)