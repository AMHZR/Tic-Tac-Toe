from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    # Example:
    url(r'^$',index,name='index'),
    url(r'^tic-tac-toe$',game,name='play'),
    
    
)