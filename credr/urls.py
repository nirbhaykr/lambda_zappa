from django.conf.urls import patterns, include, url
from rest_framework.authtoken import views
from invoices.views import InvoiceChangeViewSet
from rest_framework.routers import DefaultRouter

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = DefaultRouter()
router.register(r'invoices', InvoiceChangeViewSet)


urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', HomePageView.as_view(),name="about_page"),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns = urlpatterns + router.urls