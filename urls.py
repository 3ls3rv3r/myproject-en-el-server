from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('myproject.polls.views',
    (r'^polls/', include('myproject.polls.urls')),
    (r'^plp/', include('myproject.polls.urls_plp')),
    (r'^admin/', include(admin.site.urls)),
    (r'^quiero', 'umkt_quiero'),
    (r'^s_captcha', 's_captcha_simple'),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)
