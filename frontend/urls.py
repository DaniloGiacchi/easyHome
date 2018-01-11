from django.conf.urls import include, url
#from django.contrib.auth import views as auth_views
import backend
from . import views
from django.contrib.auth.decorators import login_required
"""from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')"""

"""url(r'^$', views.frontend_home, name='frontend_home'),"""
app_name='frontend'

urlpatterns = [	
	
		url(r'^$', views.frontend_home, name='frontend_home'),
	#url(r'^about$', views.AboutPageView.as_view(), name='AboutPageView'),
	url(r'^about$', views.frontend_about, name='frontend_about'),
	#url(r'^contact$', views.frontend_contact, name='frontend_contact'),
	url(r'^contact$', views.frontend_contact.as_view(), name='frontend_contact'),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/profile', views.ProfilePageView.as_view(), name='profile'),
]