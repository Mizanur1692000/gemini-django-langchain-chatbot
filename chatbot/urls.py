from django.urls import path
from .views import ChatView, EmailView

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('set_email/', EmailView.as_view(), name='set_email'),
]