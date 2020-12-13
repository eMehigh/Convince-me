"""concvinceme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from main.views import (main_view,
                        list_view,
                        chat_view,
                        create_room_view, 
                        send_message,
                        wait_for_connection,
                        )

urlpatterns = [
    path('wait-for-connection<str:name>', wait_for_connection, name="wait-for-connection"),
    path('send-message-to-user-and-back/', send_message, name = "send-message"),
    path('admin/', admin.site.urls),
    path('', main_view, name="index"),
    path('chat/<room_name>/as/<pair_name>/', chat_view, name = "chat"),
    path('chat-list/', list_view, name="chat-list"),
    path('create-room/<name>', create_room_view,
         name="create-room")
]
