from django.conf import settings
from django.conf.urls import patterns, include, url
from votaciones_leyes.views import PersonListView, PersonDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', PersonListView.as_view(), name='home'),
    url(r'^votaciones/(?P<slug>[-\w]+)/$', PersonDetailView.as_view(), name='votaciones'),
)
