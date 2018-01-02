from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cart_app import views

urlpatterns = [
    url(r'^customers/$', views.CustomerList.as_view()),
    url(r'^skus/$', views.SKUList.as_view()),
    url(r'^cart_detail/$', views.CartList.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    url(r'^skus/(?P<pk>[0-9]+)/$', views.SKUDetail.as_view()),
    url(r'^cart_detail/(?P<pk>[0-9]+)/$', views.CARTDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
