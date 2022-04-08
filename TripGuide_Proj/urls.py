"""TripGuide_Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from member.views import CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('member/', include('member.urls')),
    path('manager/', include('manager.urls')),
    path('contents/', include('contents.urls')),
    path('board/', include('board.urls')),
    path('add/', include('add.urls')),
    path('event/', include('event.urls')),
    path('reviews/', include('reviews.urls')),
    # path('count/', include('count.urls')),
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    path(
        'email-confirmation-done/',
        TemplateView.as_view(template_name='email_confirmation_done.html'),
        name='account_email_confirmation_done',
    ),
    path('', include('allauth.urls')), # django-allauth 라이브러리 관련된 path는 "반드시" 가장 아래쪽에 있도록 해주세요.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

