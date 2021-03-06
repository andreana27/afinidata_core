"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('areas/', include('areas.urls', namespace='areas')),
    path('milestones/', include('milestones.urls', namespace='milestones')),
    path('entities/', include('entities.urls', namespace='entities')),
    path('bots/', include('bots.urls', namespace='bots')),
    path('bot_interactions/', include('bots.interaction_urls', namespace='bot_interactions')),
    path('channels/', include('channels.urls', namespace='channels')),
    path('instances/', include('instances.urls', namespace='instances')),
    path('chatfuel/', include('chatfuel.urls', namespace='chatfuel')),
    path('conversations/', include('conversations.urls', namespace='conversations')),
    path('users/', include('messenger_users.urls', namespace='messenger_users')),
    path('attributes/', include('attributes.urls', namespace='attributes')),
    path('forms/', include('forms.urls', namespace='forms')),
    path('levels/', include('levels.urls', namespace='levels')),
    path('utilities/', include('utilities.urls', namespace='utilities')),
    path('groups/', include('groups.urls', namespace='groups')),
    path('languages/', include('languages.urls', namespace='languages')),
    path('programs/', include('programs.urls', namespace='programs')),
    path('app_services/', include('app.service_urls', namespace='app_services')),
    path('sessions/', include('user_sessions.urls', namespace='sessions')),
    path('topics/', include('topics.urls', namespace='topics')),
    path('password-reset/', include('user_passwd_reset.urls', namespace='user_passwd_reset'))
]
