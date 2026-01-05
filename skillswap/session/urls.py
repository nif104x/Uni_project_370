from django.urls import path
from session.views import *
urlpatterns = [
    path('view/', view_session, name="view_session"),
    path('accept_session/<str:s_id>/', accept_session_request, name='accept_session'),
    path('decline_session/<str:s_id>/', decline_session_request, name='decline_session'),
    path('cancel_session/<str:s_id>/', cancel_session_request, name='cancel_session'),
    path('join/<path:link>/', join, name='join')
]