from django.urls import path
from .views import signup, homepage, signin

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', homepage, name='home'),
    path('signin/', signin, name='signin'),

]
