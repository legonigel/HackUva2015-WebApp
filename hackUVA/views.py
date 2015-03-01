from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from allaccess.views import OAuthRedirect

# Create your views here.


class AdditionalPermissionsRedirect(OAuthRedirect):
    
	def get_additional_parameters(self, provider):
        if provider.name == 'facebook':
            # Extra permissions
            return {'scope': 'public_profile,user_friends'}
